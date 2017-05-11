---
layout: episode
title: "Automating with cloud-init"
teaching: 180
exercises: 0
questions:
- "What does CloudInit do?"
objectives:
- "List of objectives"
keypoints:
- "A Keypoint 0"
start: true
start_time: 540
---

We have worked through all the steps to configure and setup a WordPress site manually. This gave us exposure to the various components that make up many common web applications. Now image if you wanted to setup many WordPress sites or other commonly used website applications it could take a great deal of time, on the order of a day each if everything goes well. Also, if these website applications are so common would it not be nice to have a way to automate all that monotonous manual setup? In fact if someone automated that process you, as well as others, could save considerable time not just in the setup but also in having to figure out all the steps required to do the setup. In fact if the process was automated you may not have to think much at all about things like MySQL and PHP and just start using the web application once the installation finishes.

There are two main methods that this problem could be solved. The first method is only a very slight alteration on what was done yesterday. Once all the manual setup has been completed all that work can be saved in an image. Then the image could be reused to create new VMs. However this does not completely solve the problem because there will still be some manual steps required. For example, you would not want the same passwords to be used on all the WordPress sites, especially since anyone who had access to that image would also know those preset passwords. This could be a severe security issue. This method is OK when the image is not widely distributed and you are willing to manually changed database passwords and other passwords and keys used in the setup however this would then mean that anyone using the image would  have to know at least some of the steps required to create the image in the first place. This would limit the ease with which others could reuse the image. This method would also still require the setup of SSL certificates as a separate manual step as they can not be shared between VMs.

As you might have guessed there is a better solution, [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html). Cloud-init is a set of python scripts and utilities which run various setup operations during the initial boot of your virtual machine. This can be used to automate the setup steps we performed yesterday. For common tasks such as installing packages it is not much harder than listing the names of the packages you wish to install and cloud-init will install them for you. You can also do things like configure the language and time-zone of the VM's operating system. You can add users to your VM and inject their public keys so they can login as soon as the VM has finished its first time setup. You can create files and run commands. If those files are scripts you can run them to perform various tasks such as editing configuration files, creating passwords and keys and anything you can write a script to do.

To use cloud-init you provide a file or text describing what you would like cloud-init to do. This text or file can have various formats (see [cloud-init formats](https://help.ubuntu.com/community/CloudInit) for a list of available formats), but the two formats which we will be using in this course are:
* **User-data script** which allows you to specify a file containing a script of various commands or code you wish to execute at a very late stage in the boot sequence of the VM.
* **Cloud Config Data** which allows you to specify common operations to perform (files to create, commands to run, etc.) and also less common operations by explicitly specifying the commands or scripts to run using the cloud config format.

Before we get into the details of creating scripts or cloud config files to use with cloud-init to configure our VMs lets see an example of cloud-config file in action. We will work through this example together, in which we create a VM with a WordPress setup similar to what we did manually in previous episodes. There are some differences however for example the steps we took in the manual install for setting up SSL certificates or running the `mysql_secure_installation` script to improve MySQL database security have been omitted. With some effort though these additional steps and others could be included.

When we can create a VM we pass the cloud config or script file to the VM which describes to cloud-init what commands should be issued. We can pass this file either in horizon, using the *Post-Creation* tab when clicking *Launch instance*. In this case you can either select *File* or *Direct Input* for your *Script Source*. If selecting *File* you can click *Choose File* to select your file from you workstation, or if selecting *Direct Input* you can copy and paste the contents of the file into the text box.

Alternatively you can provide the cloud config or script file when creating the VM with the `--user-date` option followed by the path to your script file. This is the method I will choose but feel free to use which ever method is best for you.

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

The setup will take some time as it is downloading and installing updates to Ubuntu packages, installing PHP and MySQL packages as well as downloading and installing WordPress as well as performing some setup tasks. So how will we know when the setup is done? We can view the progress of the setup in the VMs log. This can be viewed in horizon if you click on the VM's name in the *instances* table and the select the *log* tab. This shows the last 35 lines of the console log. To see more of the log you can either increase the number of lines to display in the text box and then click *Go* or click *View Full Log* which shows the full log text in a separate tab of your browser. Click the *Go* button can also be used to update the console log as more content can be added to the log if the setup process is still ongoing. Once the setup has compeleted the last few lines in this log should look something like:
~~~
           Starting Update UTMP about System Runlevel Changes...
[[0;32m  OK  [0m] Started Update UTMP about System Runlevel Changes.
[   23.237522] cloud-init[1049]:   en_US.UTF-8... done
[   23.239847] cloud-init[1049]: Generation complete.
[   23.890308] cloud-init[1049]: Cloud-init v. 0.7.9 running 'modules:config' at Thu, 11 May 2017 16:12:57 +0000. Up 22.30 seconds.
[[0;32m  OK  [0m] Started Apply the settings specified in cloud-config.
         Starting Execute cloud user/final scripts...
ci-info: ++++++++++Authorized keys from /home/ubuntu/.ssh/authorized_keys for user ubuntu++++++++++
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
ci-info: +---------+-------------------------------------------------+---------+------------------+
ci-info: | ssh-rsa | 24:8d:e7:a6:b6:f5:02:b1:0f:89:93:85:85:eb:d5:57 |    -    | rsa-key-20160303 |
ci-info: +---------+-------------------------------------------------+---------+------------------+
<14>May 11 16:12:59 ec2: 
<14>May 11 16:12:59 ec2: #############################################################
<14>May 11 16:12:59 ec2: -----BEGIN SSH HOST KEY FINGERPRINTS-----
<14>May 11 16:12:59 ec2: 1024 SHA256:Yif0FbMVgOWRNU8PcNl0UFWqIPusdJzDXrMriOOAyXA root@test-wordpress-ci (DSA)
<14>May 11 16:12:59 ec2: 256 SHA256:KWM+DG8A0aEzxhfze2WlFwyEeWEBrld1gfs1vPfHYK0 root@test-wordpress-ci (ECDSA)
<14>May 11 16:12:59 ec2: 256 SHA256:/RIOOFg5qShmg5zyhoIywzcbioy/mvOYPxeGuZtDQl0 root@test-wordpress-ci (ED25519)
<14>May 11 16:12:59 ec2: 2048 SHA256:08wCbeZjagqjmPAeRczZly2dmw/PYouiM1oHBmJVnYo root@test-wordpress-ci (RSA)
<14>May 11 16:12:59 ec2: -----END SSH HOST KEY FINGERPRINTS-----
<14>May 11 16:12:59 ec2: #############################################################
-----BEGIN SSH HOST KEY KEYS-----
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOPcP71KygROMsvE5CdCuPNelLRmWr98zEHboOdXbHIOWwDuYbR6bkHELIWVOluJ4PGauWJXuroVfBydoXSU9qw= root@test-wordpress-ci
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICFFXPFX03x0+CSe/VgKwO/Hb/cW8NIzERlta9GL24Mm root@test-wordpress-ci
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC27kSkcFzkmBPRk0WihBFWEl2GgQKyqzyaAMwCX7WsSxuq7sIkw2rcp6HzWB+Eun/Tds1d8NKzIYXL9wNAvRGbey8kL0ipzrSjHexxUThxqWiXEF7bRu8LyYE8zz9yKDW3ccA+qsAhVGOYsNvLKSO9civ78HXiL8QzA92UC53WtYVXg1z/ljkWtzB1xH+yW/a0cONQk+77TP6bCYYuQ2FUPMfmwMlqejdQ1o+1fHD5mKIpRDpkYdxr4dY9q61psGKFV7M0lOE3Mir6pyk3IUSUz1MeSOPkjJnHPeFyjUBTELd0U4ZlPyVi0mAacj4GXul4I5+HG3FyXfwrDV/dk01L root@test-wordpress-ci
-----END SSH HOST KEY KEYS-----
[   24.564745] cloud-init[1258]: Cloud-init v. 0.7.9 running 'modules:final' at Thu, 11 May 2017 16:12:59 +0000. Up 24.37 seconds.
[   24.565875] cloud-init[1258]: Cloud-init v. 0.7.9 finished at Thu, 11 May 2017 16:12:59 +0000. Datasource DataSourceOpenStack [net,ver=2].  Up 24.55 seconds
[[0;32m  OK  [0m] Started Execute cloud user/final scripts.
[[0;32m  OK  [0m] Reached target Cloud-init target.

Ubuntu 16.04.2 LTS test-wordpress-ci ttyS0

test-wordpress-ci login: 
~~~
{: .output}

It is also a good idea, especially in case of any problems, to browse through the entire log looking for any messages which might suggest a problem and watch for lines indicating that the various expected packages or commands were installed. If everything seems OK then to visit the newly installed WordPress site and finalize installation add a floating IP to your newly created VM and go to `http://<your-newly-create-vms-ip>` in a new browser tab.

Output from user data cloud init script occurs after "Starting Execute cloud user/final scripts..." in instance log in the dashboard.

---
PREREQUISITES
* Will need to describe YAML syntax and give some examples
   * YAML lint for checking syntax
   * very fussy about spaces/tabs etc.
   * YAML lint might not catch errors in write_files contents.
* file permissions (why?) Need set permissions if creating a file.
* know about installation of packages in Linux
* know about upgrading packages in Linux
* have done some OpenStack CLI (e.g. `openstack server create`)

---
OUTLINE

The [Ubuntu CloudInit](https://help.ubuntu.com/community/CloudInit) page has a description of the various ways user-data can be used to configure a VM. Here we will focus on two: user-data scripts and cloud config data.

User-data script
* runs a script, could be bash, sh, python, perl etc. provided the right requirements are met to run it on the VM
* shebang at beginning of scripts indicates how the script should be run (e.g. "#!/bin/bash")

Cloud Config Data
* begins with "#cloud-config"

Things which could be done using CloudInit
* Add more than one user
* Change the default user from (e.g. ubuntu, centos etc.)
* Install software
* Upgrade
* Show them cloud init log `tail -f /var/log/cloud-init*.log`
* Show them the log on horizon (how I usually look at it). Double check that this method and the method above contains the same information.
* Create files
* run commands (e.g. git clone etc.)
* see file in dhsi-2016-master/cloud-init/step2_this_version_works.yaml (some tabs were replaced, and some echos were added)
In the end want them to have a cloudInit yaml file which they can use to configure their wordpress site automatically using cloud init.

  
