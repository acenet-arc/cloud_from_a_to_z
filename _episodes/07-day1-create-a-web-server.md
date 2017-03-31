---
layout: episode
title: "Create a web-server"
teaching: 30
exercises: 0
questions:
- "What is Apache?"
- "What is LAMP?"
- "How do we install and configure Apache?"
objectives:
- "To be able to create a web-server in Compute Canada's cloud and create and access a website served from it"
keypoints:
- "TODO - coming soon..."
---

For the purposes of this course, we will install and configure an **Apache Web Server** software application. This is free, open source software that is developed and maintained by the Apache Software Foundation and is one of the most widely used web server platforms on the Internet. While most WordPress websites use Apache, alternative software, such as Nginx, could also be used.

In fact, if the purpose of your virtual machine is to run a single instance of WordPress (which is exactly what we're doing for this course), then Nginx would most likely perform much better than Apache. However, the reason that we'll stick with Apache for this course is that Nginx is a bit more complicated to administer and demands more effort to configure alongside other tools that we will require later in the course (such as PHP and SSL encryption), so again, for the purposes of this course, we'll stick with Apache.

In addition, Apache is only one of the software components that will be used to run WordPress. All dynamic web applications like WordPress require an entire web service software stack which is traditionally referred to as **LAMP**. **LAMP** is an acronym which stands for a combination of the following free and open-source operating system and other software packages. They are as follows:

- **Linux**: the operating system chosen for your virtual machine. In our case, it's Ubuntu.

- **Apache**: the web or HTTP server. It receives and delivers requests to and from users who visit your WordPress site.  

- **MySQL**: the relational database management system that stores most of the WordPress site content.

- **PHP**: the programming languages used by the WordPress developers to create their web application. PHP uses its processor module to interpret this code which is then used by Apache to generate a resulting web page.

We'll learn how to install and configure the **M** and **P** LAMP components during Day 2, when we finish creating our WordPress sites.

## How do we install and configure Apache?

### Connect vis SSH from your workstation to your virtual machine

The first thing we need to do is connect via SSH from our workstations to the virtual machine that we created in the previous section. For review, that should look something like this:

~~~
[you@yourworkstation]$ ssh -i <your_priv_key> ubuntu@<your_floating_ip>
~~~
{: .bash}

My output looks something like this (your's will differ):

~~~
[brentg@brentwg DHSI-cloud-course]$ ssh ubuntu@206.167.181.126
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-67-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

19 packages can be updated.
16 updates are security updates.



Last login: Thu Mar 16 22:04:19 2017 from 24.86.86.43
~~~
{: .output}

### Install security updates and reboot

So, the first thing we should do is ensure that all of our security updates have been installed. We will use both **sudo** and the **apt** command to accomplish this. The **sudo** command gives us super user (or administrator) privileges. The **apt** command is used to install, update, and remove Ubuntu software packages.

First, we must update the Ubuntu software packages database.

~~~
$ sudo apt update
~~~
{: .bash}

Again, your output will be different than mine. But the result will be the same.

~~~
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease [102 kB]
Hit:2 http://nova.clouds.archive.ubuntu.com/ubuntu xenial InRelease
Get:3 http://nova.clouds.archive.ubuntu.com/ubuntu xenial-updates InRelease [102 kB]
Get:4 http://nova.clouds.archive.ubuntu.com/ubuntu xenial-backports InRelease [102 kB]
Fetched 306 kB in 1s (183 kB/s)

Reading package lists... Done
Building dependency tree
Reading state information... Done
4 packages can be upgraded. Run 'apt list --upgradable' to see them.
~~~
{: .output}

Second, we need to install the updated packages. We;ll use the **-y** option which means that the operating system won't bother us for a final confirmation.

~~~
$ sudo apt upgrade -y
~~~
{: .bash}

~~~
Lots of various text...
...
...
Found kernel: /boot/vmlinuz-4.4.0-67-generic
Found kernel: /boot/vmlinuz-4.4.0-21-generic
Replacing config file /run/grub/menu.lst with new version

Updating /boot/grub/menu.lst ... done
~~~
{: .output}

At this point, it is a very good idea to reboot our virtual machines.

~~~
$ sudo reboot
~~~
{: .bash}

And then we'll wait a couple of minutes before retrying to connect once again via SSH from our workstations to our virtual machines.

### Install the Apache software package

After reconnecting, we need to install the Apache software package.

Once again, update the Ubuntu software packages database.

~~~
$ sudo apt update
~~~
{: .bash}

Then install the **apache2** Ubuntu package.

~~~
$ sudo apt install apache2 -y
~~~
{: .bash}
~~~
TODO ...
~~~
{: .output}
