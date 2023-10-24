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
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)
.
.
.
ubuntu@john-smith:~$
~~~
{: .output}

## Update our software package list
We will use both the [**`sudo`**](../reference#sudo) and [**`apt`**](../reference#apt) commands to apply updates to the VM. The `sudo` command gives us, temporarily, super user or administrator privileges just for the command it has been given as an argument. The username of the administrative user on many Linux systems is `root` so operating system files and directories are often owned by the `root` user. Depending on the file permissions you may need to become the `root` user temporarily using `sudo` to edit or even read these files or directories.

The `apt` command is used to install, update, and remove Ubuntu software packages. It needs super user permissions because it modifies operating system files and you wouldn't want ordinary users to do this either intentionally or by mistake. You might have noticed that when you connect to a VM for the first time it actually says there are no packages to be updated. This does not actually mean that all packages are up-to-date but that the Operating system just does not know that any packages can be updated. To remedy this we use the `apt update` command which updates the packages database.

To illustrate what happens if you forget to include `sudo` lets first run the command omitting it
~~~
$ apt update
~~~
{: .bash}
~~~
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
W: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
W: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
~~~
{: .output}

Now with `sudo`.
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

It does seem a little funny that you should need to put a `sudo` in front of your command, as illustrated in this [xkcd comic](https://xkcd.com/149/) shown below:

[![xkcd sandwich](https://imgs.xkcd.com/comics/sandwich.png)](https://xkcd.com/149/)

but it turns out it helps prevent doing things unintentionally and improves security.

## Upgrade our software packages

Typically on a new VM you would want to update all the software on it right away as many of these updates are security fixes.

Depending on exactly how many updates need to be applied this can take quite a bit of time. With the current base Ubuntu image this can take about 30 minutes. This is prohibitively long for a workshop so **we will NOT run the comands in the rest of this episode** and instead just talk through the process.

The `apt upgrade` command is the command to use to update all the software. We can add a `-y` option to tel it to skip confirmation before performing the upgrade.

~~~
$ sudo apt upgrade -y
~~~
{: .bash}

~~~
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following NEW packages will be installed:
.
.
.
Restarting services...
 systemctl restart cron.service multipathd.service packagekit.service polkit.service rsyslog.service ssh.service udisks2.service
Service restarts being deferred:
 systemctl restart ModemManager.service
 /etc/needrestart/restart.d/dbus.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
~~~
{: .output}

Depending on exactly what software needed to be updated, it may ask if you want to restart particular services during the update process. It is best to accept the services already selected for restart, and allow the software upgrade process to restart them.

At this point, it is a good idea to [**reboot**](../reference#reboot) our virtual machines. Sometimes before updating certain packages other packages on which they depend must first be updated and in effect. This can require a reboot.

~~~
$ sudo reboot
~~~
{: .bash}

This will disconnect us from our VM and we will need to wait some time (~ 1 minute) for the VM to finish rebooting before trying to reconnect.

**HINT:** you can likely press the "up-arrow" on your keyboard while in the shell to bring back the last command you used to connect to your VM without having to retype it.
~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
~~~
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-50-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Oct 11 17:48:14 UTC 2022

  System load:  0.48193359375     Processes:             93
  Usage of /:   9.6% of 19.20GB   Users logged in:       0
  Memory usage: 12%               IPv4 address for ens3: 192.168.0.207
  Swap usage:   0%


0 updates can be applied immediately.


Last login: Tue Oct 11 16:06:30 2022 from 64.66.220.94
~~~
{: .output}

If you get
~~~
ssh: connect to host 206.12.11.12 port 22: Connection refused
~~~
{: .output}
it likely just means your VM hasn't booted back up fully yet. Wait a little longer and try again.

When we log back in it tells us there are no updates available. Sometimes this isn't the case depending the details of the updates you just installed. There are times when updates may depend on other updates which require a reboot before they are fully installed and functional. This process of update, upgrade, reboot can sometimes take a few iterations until all the packages have been upgraded.


> ## Automating Upgrades
> It is possible to setup automatic updates on most Linux distributions. For a tutorial for Ubuntu Linux see [Enabling and Disabling Unattended Upgrades in Ubuntu](https://linuxhint.com/enable-disable-unattended-upgrades-ubuntu/).
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
