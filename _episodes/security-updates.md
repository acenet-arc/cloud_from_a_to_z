---
layout: episode
title: "Applying updates"
teaching: 15
exercises: 5
questions:
- "How do you perform administrative tasks on a Linux server?"
- "How do you keep a Linux server updated?"
objectives:
- "Learn about Ubuntu's package manager."
- "Learn how to run commands as an administrator."
- "Install software updates."
keypoints:
- "Use the `sudo` command to run commands following it as an administrator."
- "Use `sudo apt update` to update the package list."
- "Use `sudo apt upgrade` to upgrade packages."
- "Reboot after updates have been installed by running the `reboot` command."
- "You may need to repeat the `apt update`, `apt upgrade`, reboot process a few times to ensure all updates have been applied."
---

Any computer connected to the Internet is vulnerable to attacks. One of the easiest ways to help protect your cloud VM against these attacks is applying updates regularly.

If you are not already connected from your workstation via SSH to the VM that you created in the previous episode do so now. For review, that should look something like this:
~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
~~~
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-1011-kvm x86_64)
.
.
.
ubuntu@john-smith:~$
~~~
{: .output}

We will use both the [**`sudo`**](../reference#sudo) and [**`apt`**](../reference#apt) commands to apply updates to the VM. The `sudo` command gives us, temporarily, super user or administrator privileges just for the command it has been given as an argument. The username of the administrative user on many Linux systems is `root` so operating system files and directories are often owned by the `root` user. Depending on the file permissions you may need to become the `root` user temporarily using `sudo` to edit or even read these files or directories. The `apt` command is used to install, update, and remove Ubuntu software packages. It needs super user permissions because it modifies operating system files and you wouldn't want ordinary users to do this either intentionally or by mistake. You might have noticed that when you connect to a VM for the first time it actually says there are no packages to be updated. This does not actually mean that all packages are up-to-date but that the Operating system just does not know that any packages can be updated. To remedy this we use the `apt update` command which updates the packages database.
~~~
$ sudo apt update
~~~
{: .bash}
~~~
Get:1 http://security.ubuntu.com/ubuntu focal-security InRelease [107 kB]
Hit:2 http://persistent-01.clouds.archive.ubuntu.com/ubuntu focal InRelease
Get:3 http://persistent-01.clouds.archive.ubuntu.com/ubuntu focal-updates InRelease [111 kB]
Get:4 http://persistent-01.clouds.archive.ubuntu.com/ubuntu focal-backports InRelease [98.3 kB]
Get:5 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [338 kB]
.
.
.
Fetched 17.4 MB in 7s (2515 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
145 packages can be upgraded. Run 'apt list --upgradable' to see them.
~~~
{: .output}

We will use the `-y` option with the `apt upgrade` command which tells it not to ask for confirmation and just assume we said "yes" to any questions it may ask us.
~~~
$ sudo apt upgrade -y
~~~
{: .bash}

~~~
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
.
.
.
Found initrd image: /boot/initrd.img-5.4.0-1011-kvm
Found Ubuntu 20.04.1 LTS (20.04) on /dev/vda1
done
Processing triggers for initramfs-tools (0.136ubuntu6.3) ...
update-initramfs: Generating /boot/initrd.img-5.4.0-1026-kvm
~~~
{: .output}

At this point, it is a very good idea to [**reboot**](../reference#reboot) our virtual machines. Sometimes before updating certain packages other packages on which they depend must first be updated and in effect. This can require a reboot.

~~~
$ sudo reboot
~~~
{: .bash}

This will disconnect us from our VM and we will need to wait some time (~ 1 minute) for the VM to finish rebooting before trying to reconnect.
~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
~~~
Using username "ubuntu".
Authenticating with public key "rsa-key-20160303"
Passphrase for key "rsa-key-20160303":
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1026-kvm x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Oct 14 16:12:09 UTC 2020

  System load:  0.53              Processes:             68
  Usage of /:   7.8% of 19.21GB   Users logged in:       0
  Memory usage: 8%                IPv4 address for ens3: 192.168.181.26
  Swap usage:   0%

0 updates can be installed immediately.
0 of these updates are security updates.

Last login: Wed Oct 14 15:26:10 2020 from 198.90.95.246
~~~
{: .output}

When we log back in it tells us there are no updates available. Sometimes this isn't the case depending the details of the updates you just installed. There are times when updates may depend on other updates which require a reboot before they are fully installed and functional. This process of update, upgrade, reboot can sometimes take a few iterations until all the packages have been upgraded.


> ## Automating Upgrades
> On newer version of Ubuntu, such as 20.04, automatic updates are enabled, however this still often requires at least a reboot of the VM periodically as it doesn't do this for you automatically unless specifically configured to do so.
{: .callout}

> ## Sudo
> If `touch file_name` is a command that creates a file named `file_name` what output will the next two commands generate. If the user `ubuntu` runs those commands.
> ~~~
> $ sudo touch file_name
> $ ls -l
> ~~~
> {: .bash}
> 
> 1. `-rw-rw-r--  1 ubuntu ubuntu 0 Oct 15 19:33 file_name`
> 2. `-rw-rw-r--  1 root   root   0 Oct 15 19:33 file_name`
> 3. `-rw-rw-r--  1 ubuntu root   0 Oct 15 19:33 file_name`
> 4. `-rw-rw-r--  1 root   ubuntu 0 Oct 15 19:33 file_name`
> 
> > ## Solution
> > 
> > 1. No, even though the command `sudo` is run as the `ubuntu` user, it will run the `touch` command which generates the file as the `root` or administrative user.
> > 2. yes, the `touch` command will be run as the `root` user which has the primary group `root`. The primary group of the user who creates the file is the default group for the new file or directory.
> > 3. No, 
> > 4. No
> {: .solution}
{: .challenge}