---
layout: episode
title: "Installing OpenStack CL client"
teaching: 15
exercises: 0
questions:
- "Why use OpenStacks command line client?"
- "How do we start using the CL client?"
objectives:
- "Install OpenStack command line client."
- "Download OpenStack RC file"
keypoints:
- "The CL client can be used to manager your OpenStack project from any computer connected to the Internet."
- "The OpenStack RC file provides settings to connect the CL client with your cloud project."
- "The `source` command is used to apply settings in a file to your shell environment."
---

In this episode we will setup the OpenStack command line tools to work with our OpenStack project. These tools allow us to perform the same actions we perform in the GUI, and more on the command line. Why would you want to use the command line when there is a nice GUI? There are two main reasons:

* There are some things which can not be done with the GUI. Such as downloading an image of a volume for safe keeping.
* Automating repetitive tasks. What if you wanted 30 VMs but didn't want to spend several hours creating them all? Or to create a backup of your VM every night at midnight without having to stay awake each night till midnight to manually create the image.

To use the OpenStack command line clients they need to be installed. They can be installed and used to work with your OpenStack project from any computer connected to the Internet, though a Linux machine is likely the easiest place to install them. To get started lets create a VM in which we can use the command line clients.

Our first use of the command line tools will be to backup our persistent VM which we installed Apache on. So we will need to run the command line tools on a separate VM to save an image of our persistent VM's volume for safe keeping. Go to *Instances*->*Launch Instance* and specify *Instance Name* as `<your name>-test-oscli` and replace `<your name>` with your name with spaces replaced with "-". Then select *Flavor* `c1-7.5gb-30` or `c1-3.75gb-36`. For *Instance Boot Source* choose `Boot from image` and then select the *Image Name* `Ubuntu-16.04-Xenial-x64-2017-03`. Next select the *Access & Security* tab choose your *Key Pair* and the *default* security group and click *Launch*. Then associate a floating IP with your newly created VM. To do this click on the drop down menu next to your newly created VM on the *Instances* panel and select *Associate Floating IP*. If there is not an available IP address in the *IP Address* drop down menu click the '+' button next to it to allocate a new floating IP and then choose it in the drop down box. If you have exceeded your quota of float IP address, we may need to borrow it from your persistent VM temporarily.

The next step is to connect to your newly created VM with SSH as we have done before. In the terminal on your workstation type
~~~
$ ssh ubuntu@206.12.11.13
~~~
{: .bash}
~~~
Enter passphrase for key '/home/mobaxterm/.ssh/id_rsa':
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-71-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@chris-geroux-test-oscli:~$
~~~
{: .output}

as was the case when setting up a web server we must first update the package database on our newly created virtual machine with
~~~
$ sudo apt update
~~~
{: .bash}
~~~
sudo: unable to resolve host chris-geroux-test-oscli
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Hit:2 http://nova.clouds.archive.ubuntu.com/ubuntu xenial InRelease

...

Reading state information... Done
15 packages can be upgraded. Run 'apt list --upgradable' to see them.
~~~
{: .output}

At this point we should probably upgrade packages which can be upgraded with `sudo apt upgrade -y` and reboot the VM. However, in the interest of time we will omit this step. Skipping this step is not too large a concern as this VM will only be used temporarily. The `sudo apt update` step however, is often required for the Ubuntu package manager to have the most update information about where to get packages from and to be able to install them. So if this step is skipped installation of software packages can fail.

To install the OpenStack command line clients lets first search for the correct package name with 
~~~
$ apt search openstack
~~~
{: .bash}
~~~
Sorting... Done
Full Text Search... Done
aodh-api/xenial-updates 2.0.5-0ubuntu1 all
  OpenStack Telemetry (Ceilometer) Alarming - API server

aodh-common/xenial-updates 2.0.5-0ubuntu1 all
  OpenStack Telemetry (Ceilometer) Alarming - common files

...

python3-openstack.nose-plugin/xenial 0.11-2 all
  nosetests output to mimic the output of openstack's run_tests.py - Python 3.x

python3-openstackclient/xenial 2.3.0-2 all
  OpenStack Command-line Client - Python 3.x

python3-openstackdocstheme/xenial 1.2.5+dfsg1-1 all
  extension support for Sphin OpenStack doc - Python 3.x

...

zaqar-common/xenial 2.0.0-1 all
  OpenStack Queueing as a Service - common files

zaqar-server/xenial 2.0.0-1 all
  OpenStack Queueing as a Service - API server
~~~
{: .output}

In this case we can see that the package `python3-openstackclient` provides the OpenStack Command-line Client for Python 3. Python is a programing language which is used heavily by OpenStack. In fact the command line tools are written with Python, and there is a Python application programing interface (API) which allows you to write programs in Python which can perform actions on your OpenStack projects. Python 3 is the current major version of Python, though Python 2 is still frequently used. We can install this package with
~~~
$ sudo apt install python3-openstackclient -y
~~~
{: .bash}
~~~
sudo: unable to resolve host chris-geroux-test-oscli
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:

...

Setting up python3-openstackclient (2.3.0-2) ...
update-alternatives: using /usr/bin/python3-openstack to provide /usr/bin/openstack (openstack) in auto mode
Processing triggers for libc-bin (2.23-0ubuntu7) ...
~~~
{: .output}

and now the OpenStack command line clients are installed.

The next step is to tell the command line clients how to connect to your OpenStack project which is done with an OpenStack RC file. This file needs to be downloaded from the OpenStack dashboard. Go to *Compute* -> *Access & Security* select the *API Access* tab and click the *Download OpenStack RC File*. We will then need to move this file onto your VM. There are a number of ways to do this such as using [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) and there are both command line and GUI clients for performing SFTP file transfers. However, to keep things simple we will just copy and paste using the `nano` editor. Start editing a new settings file with
~~~
$ nano ~/openstackrc.sh
~~~
{: .bash}

Then open the downloaded file with a "plain text" editor (wordpad in windows) or use the `cat` command to select the text and copy and paste it into the terminal running `nano`. Then press 'ctrl + X', answer 'yes', and press return to save the file and exit nano. Verify that the file was created as expected by running
~~~
$ cat ~/openstackrc.sh
~~~
{: .bash}
~~~

...

# If your configuration has multiple regions, we set that information here.
# OS_REGION_NAME is optional and only valid in certain environments.
export OS_REGION_NAME="regionOne"
# Don't leave a blank variable, unset it if it was empty
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi
~~~
{: .output}
The last few lines of the `~/openstackrc.sh` file should look like the above if everything went well.

The final step before we can start working with the command line clients is to source the `~/openstackrc.sh` file you just created using the `source` command. Sourcing a file applies all the settings contained in that file to your current shell. When you source the file it will ask you for your OpenStack password as it doesn't contain your password. This file contains settings such as your OpenStack project, the URL of the OpenStack cloud, and the username and password for the OpenStack cloud.
~~~
$ source ~/openstackrc.sh
~~~
{: .bash}
When you exit the shell the settings you applied will be lost. When you open a new shell you will again need to source the `~/openstackrc.sh` file and provide your password again.

As a quick test to ensure everything is setup correctly run
~~~
$ openstack server list
~~~
{: .bash}
~~~
+--------------------------------------+-------------------------+--------+-----------------------------------------------+
| ID                                   | Name                    | Status | Networks                                      |
+--------------------------------------+-------------------------+--------+-----------------------------------------------+
| c5f5abfc-9b3a-4634-9e19-68e9e7988085 | chris-geroux-test-oscli | ACTIVE | cgeroux_network=192.168.220.206               |
| eedd4101-7f03-4833-9dd7-8434dcb7a197 | chris-geroux-persistent | ACTIVE | cgeroux_network=192.168.220.205               |
+--------------------------------------+-------------------------+--------+-----------------------------------------------+
~~~
{: .output}
If everything worked this command should list all the VMs in your project. We are now ready to start using the OpenStack command line clients to start performing tasks.
