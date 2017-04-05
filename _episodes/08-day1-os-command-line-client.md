---
layout: episode
title: "OpenStack command line client"
teaching: 60
exercises: 0
questions:
- "Why use OpenStacks command line client?"
objectives:
- "View various OpenStack resources using CLI"
- "Create an image from a volume"
- "Download an image to a local machine"
- "Create a new virtual machine"
keypoints:
- "A Keypoint 0"
---

In this episode we will see how to use command line tools to work with our OpenStack project. These tools allow us to perform the same actions we perform in the GUI, and more, on the command line. So why would you want to use the command line when there is a nice GUI? There are two main reasons:

* There are some things which can not be done with the GUI. Such as downloading an image of a volume for safe keeping.
* Automating repetitive tasks. What if you wanted 30 VMs but didn't want to spend several hours creating them all? Or to create a backup of your VM every night at midnight without having to stay awake till midnight everything to manually create the image.

To use the OpenStack command line clients they need to be installed. They can be installed and used to work with your OpenStack project from any computer connected to the Internet, though a Linux machine is likely the easiest place to install them. To get started lets create a VM in which we can use the command line clients.

Go to *Instances*->*Launch Instance* and specify *Instance Name* as `<your name>-test-oscli` and replace `<your name>` with your name spaces. Then select *Flavor* `c1-7.5gb-30` or `c1-3.75gb-36`. For *Instance Boot Source* choose `Boot from image` and then select the *Image Name* `Ubuntu-16.04-Xenial-x64-2017-03`. Next select the *Access & Security* tab choose your *Key Pair* and the *default* security group and click *Launch*. Then associate a floating IP with your newly created VM. To do this click on the drop down menu next to your newly created VM on the *Instances* panel and select *Associate Floating IP*. If there is not an available IP address int eh *IP Address* drop down menu click the *+* button next to it to allocate a new floating IP and then choose it in the drop down box.

The next step is to connect to your newly created VM with SSH as we have done before. In the terminal on your laptop type

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

/usr/bin/xauth:  file /home/ubuntu/.Xauthority does not exist
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

At this point we should probably upgrade packages which can be upgraded with `sudo apt upgrade -y` and reboot the VM. However, in the interest of time we will omit this step. The `sudo apt update` step however, is often required for the Ubuntu package manager to have the most update information about where to get packages from and to be able to install them. So if this step is skipped installation of software packages can fail.

To install the OpenStack command line clients lets first search for the correct package name with 
~~~
$ apt-cache search openstack
~~~
{: .bash}
~~~
ceilometer-agent-central - ceilometer central agent
ceilometer-agent-compute - ceilometer compute agent

...

python3-openstack-doc-tools - tools used by the OpenStack Documentation project - Python 3.x
python3-openstack.nose-plugin - nosetests output to mimic the output of openstack's run_tests.py - Python 3.x
python3-openstackclient - OpenStack Command-line Client - Python 3.x
python3-openstackdocstheme - extension support for Sphin OpenStack doc - Python 3.x
python3-openstacksdk - SDK for building applications to work with OpenStack - Python 3.x

...

zaqar-server - OpenStack Queueing as a Service - API server
glance-store-common - OpenStack Image Service store library - common files
~~~
{: .output}

In this case we can see that the package `python3-openstackclient` provides the OpenStack Command-line Client for Python 3. So we can install this package with
~~~
$ sudo apt install python3-openstackclient
~~~
{: .bash}
~~~
sudo: unable to resolve host chris-geroux-test-oscli
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:

...

After this operation, 42.6 MB of additional disk space will be used.
Do you want to continue? [Y/n]
~~~
{: .output}

At this point type `Y` followed by return.
~~~
Get:1 http://nova.clouds.archive.ubuntu.com/ubuntu xenial/main amd64 libjpeg-turbo8 amd64 1.4.2-0ubuntu3 [111 kB]
Get:2 http://nova.clouds.archive.ubuntu.com/ubuntu xenial/main amd64 liblcms2-2 amd64 2.6-3ubuntu2 [137 kB]
Get:3 http://nova.clouds.archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-pyparsing all 2.0.3+dfsg1-1ubuntu0.1 [35.5 kB]

...

Setting up python3-openstackclient (2.3.0-2) ...
update-alternatives: using /usr/bin/python3-openstack to provide /usr/bin/openstack (openstack) in auto mode
Processing triggers for libc-bin (2.23-0ubuntu7) ...
~~~
{: .output}

and now the OpenStack command line clients are installed.



---
PREREQUISITES

---
OUTLINE

* Setup
  * Using a VM in the cloud
  * Install CL client
  * Put OS RC file on VM
    * good opportunity to mention some tools for getting data into VM (e.g. winSCP/Cyberduck/Some Linux SFTP client?)
* Introduce commands in the context of saving an image of their persistent VM
  * give a reference for all commands:
    * https://docs.computecanada.ca/wiki/OpenStack_Command_Line_Clients#Command_groups
    * Also an OS reference
  * `server`
    * `list`
    * `stop` or `delete`
  * `volume`
    * `list`
  * `image`
    * `list`
    * `create`
    * `save`
  * `server`
    * `start` or `create`
  * `ip` (should already have an IP address)
    * `floating list`
    * `floating create`
    * `floating add`

  
