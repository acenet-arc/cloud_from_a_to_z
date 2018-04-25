---
layout: episode
title: "Applying updates"
teaching: 15
exercises: 0
questions:
- "How can can you keep a Linux software updated?"
- "How can I fix the 'sudo: unable to resolve host' message?"
objectives:
- "Use a terminal based editor to edit a file."
- "Learn about Ubuntu's package manager."
- "Learn how to run commands as an administrator."
- "Install software updates."
keypoints:
- "Use `sudo apt update` to update the package list."
- "Use `sudo apt upgrade` to upgrade packages."
- "Reboot after updates have been installed."
- "You may need to repeat the `apt update`, `apt upgrade`, reboot process a few times to ensure all updates have been applied."
---

Any computer connected to the Internet is vulnerable to attacks. One of the easiest ways to help protect your cloud VM against these attacks is applying updates regularly.

If you are not already connected from your workstation via SSH to the VM that you created in the previous episode do so now. For review, that should look something like this:
~~~
[you@yourworkstation]$ ssh -i <your_priv_key> ubuntu@<your_floating_ip>
~~~
{: .bash}
~~~
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-67-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.



Last login: Thu Mar 16 22:04:19 2017 from 24.86.86.43
~~~
{: .output}

We will use both the [**`sudo`**](../reference#sudo) and [**`apt`**](../reference#apt) commands to apply updates to the VM. The `sudo` command gives us, temporarily, super user or administrator privileges just for the command it has been given as an argument. The `apt` command is used to install, update, and remove Ubuntu software packages. It needs super user permissions because it modifies operating system files and you wouldn't want ordinary users to do this either intentionally or by mistake. You might have noticed that when you connect to a VM for the first time it actually says there are no packages to be updated. This does not actually mean that all packages are up-to-date but that the Operating system just does not know that any packages can be updated. To remedy this we use the `apt update` command which updates the packages database.
~~~
$ sudo apt update
~~~
{: .bash}
~~~
sudo: unable to resolve host test
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

Notice the first line of the output `sudo: unable to resolve host test` this message results from a missing line in the `/etc/hosts` file, which maps the IP of the VM to its hostname. The message can be ignored without harm but is easily fixed. The hostname is displayed as part of the command prompt after you connect to your VM. For example, I called my VM **wordpress-vm** so my VM command prompt looks like this
~~~
ubuntu@wordpress-vm:~$
~~~
{: .bash}

To edit the `/etc/hosts` file we will use the shell based editor `nano`. This editor allows you to edit text files directly in the shell without a GUI. It displays the text of the file in the terminal and lets you navigate around the file with the arrow keys. Once you find a place you wish to edit you can start typing to insert new text.

~~~
$ sudo nano /etc/hosts
~~~
{: .bash}
~~~
  GNU nano 2.5.3                               File: /etc/hosts

127.0.0.1 localhost

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts

                                          [ Read 9 lines (Warning: No write permission) ]
^G Get Help     ^O Write Out    ^W Where Is     ^K Cut Text     ^J Justify      ^C Cur Pos      ^Y Prev Page    M-\ First Line
^X Exit         ^R Read File    ^\ Replace      ^U Uncut Text   ^T To Spell     ^_ Go To Line   ^V Next Page    M-/ Last Line
~~~
{: .output}

The line beginning `127.0.0.1` is the start of the file, lines above that display information about the file you are editing and the version of nano you are using. At the bottom you can see the tasks you can perform such as `Write Out` which writes the edits you made to a file. To perform this action you would press the Ctrl key and the `O` key at the same time (that is what the `^O` represents ctrl+O). It will prompt you to change the file name (press enter to keep the same name). In our case we want to add the text `wordpress-vm` (or what ever the hostname of your VM is) at the end of the line starting `127.0.0.1`. `127.0.0.1` is a special IP  used to identify the current VM within the current VM. This means that it can not be used by another VM to refer to this VM. After the hostname is added to the end of the first line press `Ctrl+X` to exit. Be sure to answer `y` to "Save modified buffer?" to save the edits made to the file. Then press return to write to the edited file to the original file name and exit nano.

With that out of the way, lets install the updated packages. We will use the `-y` option with the `apt upgrade` command which tells it not to ask for confirmation and just assume we said "yes" to any questions it may ask us.
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

At this point, it is a very good idea to [**reboot**](../reference#reboot) our virtual machines. Sometimes before updating certain packages other packages on which they depend must first be updated and in effect. This can require a reboot.

~~~
$ sudo reboot
~~~
{: .bash}

This will disconnect us from our VM and we will need to wait some time (~ 1 minute) for the VM to finish rebooting before trying to reconnect.
~~~
$ ssh ubuntu@206.167.181.126
~~~
{: .bash}
~~~
Using username "ubuntu".
Authenticating with public key "rsa-key-20160303"
Passphrase for key "rsa-key-20160303":
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-71-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

43 packages can be updated.
12 updates are security updates.


Last login: Mon May  1 21:02:47 2017 from 173.212.77.86
~~~
{: .output}

Notice that, even though we installed updates, when we reboot and reconnect it shows that there are more updates which can be applied. This process can take a few iterations until all the packages have been upgraded.  Repeat the steps
  1. `sudo apt update`
  2. `sudo apt upgrade`
  3. `sudo reboot`
  4. reconnect to VM

until the `sudo apt update` command indicates that no more updates are available with output like
~~~
...

Reading state information... Done
All packages are up to date.
~~~
{: .output}


> ## Automating Upgrades
> It is possible to setup upgrades to happen automatically, but this is beyond the scope of this course. You are encouraged to the [Ubuntu automatic updates](https://help.ubuntu.com/lts/serverguide/automatic-updates.html) page describing how to enable automatic updates.
{: .callout}
