---
layout: page
title: "Instructor Notes"
permalink: /guide/
---

To create a VM for students to use for creating their first jekyll site use the `cloud_init_webserver.yml` file in the [cloud-init-files](../cloud-init-files/) folder when creating the VM to perform setup. Copy and paste the contents of that file into "Customization Script" under the "Configuration" tab in the popup while creating a VM in OpenStack. In the last line of the `cloud_init_webserver.yml` (`["python3","./setup_jekyll_and_guest_accounts.py","1"]`) change the `1` to the number of guest accounts you would like. With a `p16-24gb` flavor VM, 30 guest users is a very comfortable number.

Once setup has completed have a look at the VM log to find the login password for guest accounts. Search for "Guest accounts passphrase:".

Also, before users try to create their first jekyll site, some gems need to be installed for the theme I chose.

As a sudo user on the workshop VM do the following to ensure regular users won't need to install those gems:

~~~
$ wget https://github.com/andrewbanchich/forty-jekyll-theme/archive/master.zip
$ unzip master.zip
$ cd forty-jekyll-theme-master
$ sudo bundle install
~~~
{: .bash}


then regular users should just have to do:
~~~
$ jekyll build -d /var/www/html/user01
~~~
{: .bash}

as in the workshop


------

Cloud Resources required per participant:

* 1 x c1-7.5gb-30(west) or c1-3.75gb-36(east)
* 1 Floating IP
* 1 Security group

This is the first VM they create and will later be used in CLI and cloud-init episodes.

* 1 x p1-1.5gb(west) or p1-0.75gb(east)
* 1 Floating IP
* 1 Security group
* 10 GB storage

First basic webserver will be installed on it. Then manually install WP on it and later these resources will be recycled to use cloud-init and then HOT. This VM is needed during the CLI episode (to create images of volumes and show recreating a VM).

**Total per participant**:

* 2 VCPUs
* 9 GB RAM
* 2 Floating IPs
* 2 Security group
* 10 GB storage
* 1 Volume

When creating a first VM, if participants are using guest accounts in a shared project and we discovered earlier that they have different IP address, have them enter a security rule to allow their specific IP address for SSH to the default security group.
