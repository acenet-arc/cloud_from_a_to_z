---
layout: episode
title: "Automating with cloud-init"
teaching: 30
exercises: 0
questions:
- "What does cloud-init do?"
- "How can I specify a cloud-config file when creating a new VM?"
- "How can I verify that the setup worked?"
objectives:
- "Provide a cloud-config file to cloud-init."
- "View VM logs"
keypoints:
- "User data provided to a VM can be either a **cloud-config** or **script** file."
- "User data can be set using the `--user-data` on the command line or using the *Post-Creation* tab when launching a VM within horizon."
- "Cloud-init can be used to automate the initial installation of configuration of software"
- "Cloud-init runs once after the first boot of a newly crated VM"

start: true
start_time: 540
---

We have worked through all the steps to configure and setup a WordPress site manually. This gave us exposure to the various components that make up many common web applications. Now image if you wanted to setup many WordPress sites or other commonly used website applications it could take a great deal of time, on the order of half a day each if everything goes well and you know what you are doing. Also, if these website applications are so common with many people using them would it not be nice to have a way to automate all that monotonous manual setup? In fact if someone automated that process, you, as well as others, could save considerable time not just in the setup but also in having to figure out all the steps required to do the setup. In fact if the process was automated you may not have to think much at all about things like MySQL and PHP and just start using the web application once the installation finishes.

There are two main methods that could solve this problem. The first method is only a very slight alteration on what was done yesterday. Once all the manual setup has been completed all that work can be saved in an image. Then the image could be reused to create new VMs. However this does not completely solve the problem because there will still be some manual steps required. For example, you would not want the same passwords to be used on all the WordPress sites, especially since anyone who had access to that image would also know those preset passwords. This could be a severe security issue. This method is OK when the image is not widely distributed and you are willing to manually change database passwords and other passwords and keys used in the setup, however this would then mean that anyone using the image would  have to know at least some of the steps required to create the image in the first place. This would limit the ease with which others could reuse the image. This method would also still require the setup of SSL certificates as a separate manual step as they can not be shared between VMs.

As you might have guessed there is a better solution, [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html). Cloud-init is a set of python scripts and utilities which run various setup operations during the initial boot of your virtual machine. This can be used to automate the setup steps we performed yesterday. For common tasks such as installing packages it is not much harder than listing the names of the packages you wish to install and cloud-init will install them for you. You can also do things like configure the language and time-zone of the VM's operating system. You can add users to your VM and inject their public keys so they can login as soon as the VM has finished its first time setup. You can create files and run commands. If those files are scripts you can run them to perform various tasks such as editing configuration files, creating passwords and keys and anything you can write a script to do.

To use cloud-init you provide a file or text describing what you would like cloud-init to do. This text or file can have various formats (see [cloud-init formats](https://help.ubuntu.com/community/CloudInit) for a list of available formats), but there are two formats which are worht mentioning here:
* **user-data script** which allows you to specify a file containing a script of various commands or code you wish to execute at a very late stage in the boot sequence of the VM.
* **cloud-config data** which allows you to specify common operations to perform (files to create, commands to run, etc.) and also less common operations by explicitly specifying the commands or scripts to run using the cloud-config format.

Before we get into the details of creating scripts or cloud-config files to use with cloud-init to configure our VMs, lets see an example of a cloud-config file in action. We will work through this example together, and create a VM with a WordPress setup similar to what we did manually in previous episodes. There are some differences however for example the steps we took in the manual install for setting up SSL certificates or running the `mysql_secure_installation` script to improve MySQL database security have been omitted. With some effort though these additional steps could be included.

When we can create a VM we pass the cloud-config or user-data file to the VM which describes to cloud-init what commands should be issued. We can pass this file either in horizon, using the *Post-Creation* tab when clicking *Launch instance*. In this case you can either select *File* or *Direct Input* for your *Script Source*. If selecting *File* you can click *Choose File* to select your file from you workstation, or if selecting *Direct Input* you can copy and paste the contents of the file into the text box.

Alternatively you can provide the cloud-config or user-data file when creating the VM with the `--user-data` option followed by the path to your script file. This is the method I will choose but feel free to use which ever method is best for you.

~~~
$ ssh ubuntu@206.12.11.13
$ source ~/openstackrc.sh
~~~
{: .bash}
~~~
Please enter your OpenStack Password:
~~~
{: .output}
~~~
$ wget https://raw.githubusercontent.com/cgeroux/DHSI-cloud-course/master/cloud-init-files/wordpress.yaml
$ openstack server create --flavor c1-7.5gb-30 --image Ubuntu-16.04-Xenial-x64-2017-03 --key-name thekey --user-data ./wordpress.yaml test-wordpress-ci
~~~
{: .bash}
~~~
+--------------------------------------+------------------------------------------------------------------------+
| Field                                | Value                                                                  |
+--------------------------------------+------------------------------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                                                 |
| OS-EXT-AZ:availability_zone          | nova                                                                   |
| OS-EXT-STS:power_state               | 0                                                                      |
| OS-EXT-STS:task_state                | scheduling                                                             |
| OS-EXT-STS:vm_state                  | building                                                               |
| OS-SRV-USG:launched_at               | None                                                                   |
| OS-SRV-USG:terminated_at             | None                                                                   |
| accessIPv4                           |                                                                        |
| accessIPv6                           |                                                                        |
| addresses                            |                                                                        |
| adminPass                            | eyv2uTCReppK                                                           |
| config_drive                         |                                                                        |
| created                              | 2017-05-11T16:11:34Z                                                   |
| flavor                               | c1-7.5gb-30 (4f61f147-353c-4a24-892b-f95a1a523ef6)                     |
| hostId                               |                                                                        |
| id                                   | abd19450-80ff-4fc7-827a-8f1a83765efd                                   |
| image                                | Ubuntu-16.04-Xenial-x64-2017-03 (e606043e-a587-4451-9849-a2bfe95db8d4) |
| key_name                             | thekey                                                                 |
| name                                 | test-wordpress-ci                                                      |
| os-extended-volumes:volumes_attached | []                                                                     |
| progress                             | 0                                                                      |
| project_id                           | b08c709bdf314bfb886b6866c9a17b40                                       |
| properties                           |                                                                        |
| security_groups                      | [{'name': 'default'}]                                                  |
| status                               | BUILD                                                                  |
| updated                              | 2017-05-11T16:11:34Z                                                   |
| user_id                              | cgeroux                                                                |
+--------------------------------------+------------------------------------------------------------------------+
~~~
{: .output}

The setup will take some time as it is performing multiple steps.

* downloading and installing updates to Ubuntu packages
* installing PHP 
* installing MySQL 
* downloading WordPress
* configuring MySQL for WordPress
* creating  unique authentication keys

So how will we know when the setup is done? We can view the progress of the setup in the VMs log. This can be viewed in horizon if you click on the VM's name in the *instances* table and the select the *log* tab. This shows the last 35 lines of the console log. To see more of the log you can either increase the number of lines to display in the text box and then click *Go* or click *View Full Log* which shows the full log text in a separate tab of your browser. Click the *Go* button can also be used to update the console log as more content can be added to the log if the setup process is still ongoing. Once the setup has completed the last few lines in this log should look something like:

~~~
[  205.098433] cloud-init[1266]: 2017-05-11 17:28:05 (11.7 MB/s) - '/tmp/latest.tar.gz' saved [8040021/8040021]
[  205.101428] cloud-init[1266]: untarring wordpress ...
[  205.399239] cloud-init[1266]: configuring database ...
[  205.406788] cloud-init[1266]: editing the wordpress configuration ...
[  205.413312] cloud-init[1266]: configuring wordpress security keys ...
[  205.473986] cloud-init[1266]: moving install from /var/www/wordpress to /var/www/html ...
         Stopping LSB: Apache2 web server...
[  OK  ] Stopped LSB: Apache2 web server.
         Starting LSB: Apache2 web server...
[  OK  ] Started LSB: Apache2 web server.
ci-info: ++++++++++Authorized keys from /home/ubuntu/.ssh/authorized_keys for user ubuntu++++++++++
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | ssh-rsa | 24:8d:e7:a6:b6:f5:02:b1:0f:89:93:85:85:eb:d5:57 |    -    | rsa-key-20160303 |
ci-info: +---------+-------------------------------------------------+---------+------------------+
<14>May 11 17:28:08 ec2: 
<14>May 11 17:28:08 ec2: #############################################################
<14>May 11 17:28:08 ec2: -----BEGIN SSH HOST KEY FINGERPRINTS-----
<14>May 11 17:28:08 ec2: 1024 SHA256:VFTVuVNq/QEmWktn/e0xwjC5Lode4G7we4rFaqh1fpo root@test-wordpress-ci (DSA)
<14>May 11 17:28:08 ec2: 256 SHA256:rH6t6IsbLS0LUKOrW5tOSOLi/TTFaks+9ejjyDWlyik root@test-wordpress-ci (ECDSA)
<14>May 11 17:28:08 ec2: 256 SHA256:ihVWQU6o8J3UQ5rmhD1btOtSVjiJHu07iKVSJgG7MV0 root@test-wordpress-ci (ED25519)
<14>May 11 17:28:08 ec2: 2048 SHA256:BYN0PdeGehQcQ68pcdlGgpDa9aE6MpjHhhZGXKw+aVU root@test-wordpress-ci (RSA)
<14>May 11 17:28:08 ec2: -----END SSH HOST KEY FINGERPRINTS-----
<14>May 11 17:28:08 ec2: #############################################################
-----BEGIN SSH HOST KEY KEYS-----
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBA+r2DSfqzparxa4+DLcW/lYytAkWXlc+SMiRzz3F3JSNb3BtdR5W//+VXSYty4h1w8upeupun2AqEokTo/h39w= root@test-wordpress-ci
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICvzjqRhyK2QgMOzBuXGSNFhwGL+qfszG1iZVpikEXr9 root@test-wordpress-ci
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCZCgUgIJrY8w3e9STo0FV4484IzsTT71R+17k7fu1++xomEEH6Sc+1LOsceHLaLXmG3PGNSemu7S5CqdQJpW0cx3ckuaRD6z0h08QzAgkqwMCDe5aDBGNQ8ziw5V/HRNKPbLgIzpyrLMATIR8ZVy6z1QzCVWSJhkaipEVCPD11JDKfPCK+KvxbSOlS8NaVbLpI41/WP/UP+UE+WSXWpFQwJc7PNNJOITRs01nLWgxzMgceq6VsdkaNOggNe1iZQKEnHoHeNcSKoBgXETzZkoTpFJM2YPd/UerCPZ9Og1FQ4U9zAg6252iHI231+6+vU7+qoqMM/H7O/vkxFD1mvYl root@test-wordpress-ci
-----END SSH HOST KEY KEYS-----
[  207.821744] cloud-init[1266]: Cloud-init v. 0.7.9 running 'modules:final' at Thu, 11 May 2017 17:25:17 +0000. Up 37.60 seconds.
[  207.823322] cloud-init[1266]: Cloud-init v. 0.7.9 finished at Thu, 11 May 2017 17:28:08 +0000. Datasource DataSourceOpenStack [net,ver=2].  Up 207.80 seconds
[  OK  ] Started Execute cloud user/final scripts.
[  OK  ] Reached target Cloud-init target.
~~~
{: .output}

> ## Cloud-init logs
> The information in the log displayed above is constructed from a the system log on the VM `/var/log/syslog`. The log  `/var/log/cloud-init-output.log` contains the stdout and stderr from cloud-init, the content of which is also included in `/var/log/syslog`. There is also a `/var/log/cloud-init.log` log which contains logging information written from cloud-init directly into this logging file (e.g. not written to stdout or stderr first, but instead directly to the logging file from cloud-init).
{: .callout}

It is also a good idea, especially in case of any problems, to browse through the entire log looking for any messages which might suggest a problem and watch for lines indicating that the various expected packages or commands were installed. If everything seems OK then add a floating IP to your newly created VM and go to `http://<your-newly-create-vms-ip>/wordpress` in a new browser tab to finalize installation.

So in the matter a of a few minutes we have used a somewhat simplified and automated version of what we have done previously to create more or less the same result, a new WordPress site on a VM. However, it is lacking an SSL certificate to encrypt data transmission. In the next episodes we will look at how this was made possible with cloud-init. Knowing how the WordPress installation was automated will allow you to generalize to the creation of automated setups for other similar software stacks.
