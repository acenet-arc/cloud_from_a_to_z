---
layout: episode
title: "Cloud-config"
teaching: 30
exercises: 0
questions:
- "What does cloud-init do?"
objectives:
- "Learn how to provide a cloud-config file to cloud-init."
keypoints:
- "A Keypoint 0"
start: false
---

Lets revisit the `wordpress.yaml` file, however this time only looking at lines other than the Bash script.

~~~
#cloud-config
package_update: true
package_upgrade: true
packages:
  - apache2
  - mysql-server
  - php
  - libapache2-mod-php
  - php-mcrypt
  - php-mysql
  - php-curl
  - php-gd
  - php-mbstring
  - php-xml
  - php-xmlrpc
write_files:
  - content: |
      #
      # Bash script content here ...
      #
    path: /tmp/bootstrap-wp.sh
    permissions: "0755"
runcmd:
  - bash /tmp/bootstrap-wp.sh
~~~
{: .YAML}

The first line begins with a `#` and from the last episode we know that this line is a comment. However, when the **cloud-init** program reads in the file it looks at the first line even though it is a comment to figure out what it should do with the file. As was mentioned earlier, you can pass different types of files to cloud-init, we could pass a plain Bash script to cloud-init if we wanted to. In this case however, we are passing a **cloud-config** file and this comment at the top tells could-init how to interpret the file.

The next line is a YAML key value pair, with the key being `package_update` and a value of `true`. This tells cloud-init that it should update the package list on the VM. The next line `package_upgrade: true` indicates the cloud-init should then upgrade the packages (e.g. `sudo apt upgrade` on Ubuntu). Cloud-init knows how to upgrade packages on different Linux operating systems. On Ubuntu, as we did previously `sudo apt upgrade` upgrades the packages, but on CentOS for example the command is `yum update`.  Cloud-init knows how to carry out tasks on a variety of Linux operating systems so your cloud-config files will work across operating systems (though your Bash scripts may not). The next line `packges:` is the key (or name) for the following sequence, which lists package names you wish to install. While the installation of these packages is operating system independent, the package names are often not operating system independent. This list of packages should look familiar from our previous manual installs of Apache, MySQL, and PHP.

At this point there are only two sequences left in this cloud-config file, a `write_files` sequence, and a `runcmd` sequence. The `write_files` sequence tells cloud-init what files to create. The properties of a file are given in a set of mappings for the different "file" items in the sequence. The `content` key specifies what the content of the file should be. In this case we have used the block formating mentioned previously so that we can have multiple lines in the content of the file. The `path` key gives the location the file should be created in, including the file name. Finally the `permissions` key indicates what permissions the file should have. In this case the file has been given a permission of `0755` which corresponds to `-rwxr-xr-x` (see [this website](https://www.cyberciti.biz/faq/unix-linux-bsd-chmod-numeric-permissions-notation-command/) for details about numerical representations of file permissions).

The `runcmd` sequence lists a sequence of commands to run. Note that it can be important which order commands are run in and YAML sequences respect the order of items in the sequence so commands listed first will be executed first. The first and only command is `bash /tmp/bootstrap-wp.sh` which runs the bash script which was created with the `write_files` item. Even though the `write_files` and `runcmd` sequences are part of a set of mappings, in which order is not necessarily respected, cloud-init takes steps to ensure that files are created and packages are installed before commands are run.

At this point we should understand all the parts of the `wordpress.yaml` cloud-config file including the Bash script to install and configure WordPress on our VM. 

There are additional tasks which can be accomplished with cloud-init such as adding users and groups or running commands earlier in the boot sequence. To see more of the possibilities available with cloud-init browse through [cloud-config examples](https://cloudinit.readthedocs.io/en/latest/topics/examples.html)
