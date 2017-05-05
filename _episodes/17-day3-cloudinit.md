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

Yesterday we worked through all the steps to configure and setup a WordPress site manually. This gave us exposure to the various components that make up many common web applications. Now image if you wanted to setup many WordPress sites or other commonly used website applications it could take a great deal of time, on the order of a day each if everything goes well. Also, if these website applications are so common would it not be nice to have a way to automate all that monotonous manual setup? In fact if someone automated that process you as well as others could save considerable time not just in the setup but also in having to figure out all the steps required to do the setup. In fact if the process was automated you may not have to think much at all about things like MySQL and PHP and just start using the web application once the installation finishes.

There are two main methods that this problem could be solved. The first method is only a very slight alteration on what was done yesterday. Once all the manual setup has been completed all that work can be saved in an image. Then the image could be reused to create new VMs. However this does not completely solve the problem because there will still be some manual steps required. For example, you would not want the same passwords to be used on all the WordPress sites, especially since anyone who had access to that image would also know those preset passwords. This could be a severe security issue. This method is OK when the image is not widely distributed and you are willing to manually changed database passwords and other passwords and keys used in the setup however this would then mean that anyone using the image would  have to know at least some of the steps required to create the image in the first place. This would limit the ease with which others could reuse the image. This method would also still require the setup of SSL certificates as a separate manual step as they can not be shared between VMs.

As you might have guessed there is a better solution, [cloud-init](https://cloudinit.readthedocs.io/en/latest/index.html). Cloud-init is a set of python scripts and utilities which run various setup operations during the initial boot of your virtual machine. This can be used to automate the setup steps we performed yesterday. For common tasks such as installing packages it is not much harder than listing the names of the packages you wish to install and cloud-init will install them for you. You can also do things like configure the language and time-zone of the VM's operating system. You can add users to your VM and inject their public keys so they can login as soon as the VM has finished its first time setup. You can create files and run commands. If those files are scripts you can run them to perform various tasks such as editing configuration files, creating passwords and keys and anything you can write a script to do.

To use cloud-init you provide a file describing what you would like cloud-init to do. This file can have various formats (see []() for a list of available formats), but the two formats which we will mentioning here are:
* **User-data script** which allows you to specify a file containing a script of various commands or code you wish to execute at a very late stage in the boot sequence of the VM.
* **Cloud Config Data** which allows you to specify common operations to perform, files to create, commands to run, and more using the cloud config format.


openstack server create --flavor c1-3.75gb-36 --image Ubuntu-16.04-Xenial-x64-2017-03 --key-name thekey --user-data ./test.yaml test-wordpress-ci

openstack server create --flavor c1-3.75gb-36 --image Ubuntu-16.04-Xenial-x64-2017-03 --key-name thekey --file test-files
openstack server create --flavor c1-3.75gb-36 --image Ubuntu-16.04-Xenial-x64-2017-03 --key-name thekey --file /home/ubuntu=/home/ubuntu/openrc.hs  test-files --debug

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

  
