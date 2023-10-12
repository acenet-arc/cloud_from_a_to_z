---
layout: page
title: "Instructor Notes"
permalink: /guide/
---

To create a VM for students to use for creating their first jekyll site use the `cloud_init_webserver.yml` file in the [cloud-init-files](../cloud-init-files/) folder when creating the VM to perform setup. Copy and paste the contents of that file into "Customization Script" under the "Configuration" tab in the popup while creating a VM in OpenStack. In the last line of the `cloud_init_webserver.yml` (`["python3","./setup_jekyll_and_guest_accounts.py","1"]`) change the `1` to the number of guest accounts you would like. With a `p16-24gb` flavor VM, 30 guest users is a very comfortable number. As for storage, 1GB per user is also quite comfortable. With 30 guest users per VM, I went with 50GB root volume, should be more than enough space given that the site we are working with will only be a few MB.

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

When participants create their own VMs they will create a p1-1.5gb VM, with a 20GB root volume.

**Total per participant**:

* 1 VCPUs
* 1.5 GB RAM
* 1 Floating IPs
* 20 GB storage
* 1 Volume
