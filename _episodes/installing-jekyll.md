---
layout: episode
title: "Installing Jekyll"
teaching: 20
exercises: 10
questions:
- What software does Jekyll depend on?
- What are Gems?
- How is Jekyll installed?
objectives:
- Install Jekyll's dependencies.
- Configure Ruby to install Gems in your home directory.
- Install Jekyll and bundler Gems.
- Create a group to edit your server's website.
keypoints:
- Installing Gems in your home directory is preferred to system wide installation.
- The command `chown`  is used to change file and directory ownerships.
- The command `adduser` can be used to add a user to a group.
- The command `groups` can be used to list groups the current user is a member of.
- User groups can be used to allow shared access to files and directories.
start: false
---

In the previous episode I mentioned a number of static website systems, the systems I mentioned generate static websites from content you provide and are referred to as static website generators. Generally the content you provided is in the form of a text file in some format. Different static website generators have different formats they know how to read and convert into static websites. In this workshop we are going to be using the static website generator [Jekyll](https://jekyllrb.com/) which reads plain text files written in the [Markdown](https://daringfireball.net/projects/markdown/) format. We will look at the syntax of Markdown files shortly, but first lets install Jekyll on our webserver and create our first Jekyll website.

## Prerequisits
These are Ubuntu software packages which Jekyll needs to run.

* **[Ruby](https://www.ruby-lang.org/en/)**: is a programming language. This Ubuntu software package installs tools required to create and run Ruby programs. Jekyll is written in Ruby, so this is a definite requirement.
* **build-essentials**: this Ubuntu software package includes gcc, g++, make and a few commonly used software libraries. These are the [GNU](https://www.gnu.org/home.en.html) C and C++ compilers.
* **[zlib](https://zlib.net/)**: compression library.

~~~
$ sudo apt-get install ruby-full build-essential zlib1g-dev
~~~
{: .bash}

## Configure Ruby to install gems to your home directory
Ruby has its own packaging system for distributing Ruby libraries or plug-ins. One of these packages is referred to as a **Gem**. It is advisable to install these Ruby Gems into your own personal directory space. This can be beneficial if other users on the VM wish to install conflicting versions of Gems.

> ## Why would you want different versions of Gems?
> If you want to customize your Jekyll site different themes and plugins can depend on different versions of Gems. By installing Gems into a folder in your home directory you will not interfere with other people's Gems.
{: .callout}

The below commands place the text between the <code>'</code> and <code>'</code> into the file <code>~/.bashrc</code>. This is a special file which is read by the shell (a.k.a. sourced) when you first logon to the VM. You can also manually force this file to be 'sourced' using the <code>source</code> command. The first line is just a comment, note that it starts with a <code>#</code> character. The second two lines set the environment variables <code>GEM_HOME</code> and <code>PATH</code>. <code>GEM_HOME</code> is used by the Ruby package manager to know where Gems should be installed. <code>PATH</code> is a very commonly used environment variable, and it tells the operating system where to look for programs to execute. 
~~~
$ echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
$ echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
$ echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
$ source ~/.bashrc
~~~
{: .bash}

## Install Jekyll and Bundler gems
Jekyll is a Ruby Gem and can be installed with Ruby's package manager. Bundler is another Gem which aids in installing gems required by Ruby projects. Often when installing new Jekyll themes and plugins it is easiest to use Bundler to install the required Gems for those themes and plugins.
~~~
$ gem install jekyll bundler
~~~
{: .bash}

<!--Note sure I need this. Some themes I tried needed to have a newer version
of bundler, but other's do not. Maybe this should be a "break out" or something?

update bundler
~~~
$ bundle update --bundler
~~~
{: .bash}
-->

## Create and configure a group to edit your website
Currently the default web root directory <code>/var/www/html</code> of your website is only editable by the root user. This means that any user that wants to edit files in that directory must first append all commands to modify those files with the <code>sudo</code> command. This gets tedious and there is not security reason not to have these files editable by users other than root. To do this we will create a new user group <code>webeditor</code> and add the default <code>ubuntu</code> user we are logged in as to this group.

Before we create our new group, lets verify that there isn't already a group with this name used for some other purpose. To check current list of user groups look in the file <code>/etc/groups</code>. We can use the <code>less</code> command to view this file without editing it.
~~~
$ less /etc/group
~~~
{: .bash}
~~~
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
.
.
.
~~~
{: .output}
If we scrool through that list it appears we are safe. There is no group already called <code>webeditor</code>.

To create a new user group we can use the command <code>addgroup</code>
~~~
$ sudo addgroup webeditor
~~~
{: .bash}
~~~
Adding group `webeditor' (GID 1001) ...
Done.
~~~
{: .output}

Next we will use the <code>chown</code> command to change the group which the root directory of our website belongs too to be our new group and then verify that our change took place.
~~~
$ sudo chown root:webeditor /var/www/html
$ ls -l /var/www
~~~
{: .bash}
~~~
total 4
drwxr-xr-x 34 root webeditor 4096 Sep 17 16:00 html
~~~
{: .output}

As can be seen in the permissions listed in above output, these files aren't actually writable by their group. Lets use the <code>chmod</code> command to change that.
~~~
$ sudo chmod g+w /var/www/html
$ ls -al /var/www
~~~
{: .bash}
~~~
total 4
drwxrwxr-x 34 root webeditor 4096 Sep 17 16:00 html
~~~
{: .output}

When new files are created in the `html` folder, they will be owned by the user who created them, but they will also be in the user's default group, which is the same as the username of the user. This means that other user's in the `webeditor` group wouldn't be able to edit these files or directories, even though they are in the `webeditor` group. To fix this we can set the  

> ## Adding new users
> To create a new user issue the following command and replace `USERNAME` with the username you want the new user to have.
> ~~~
> $ sudo adduser --disabled-password USERNAME
> ~~~
> {: .bash}
>
> If you want this user to be able to install software or other administrative tasks you will want to give them permission to use the `sudo` command. It is generally a good security practice to limit the number of people who have administrative privileges, so give it some thought before you grant these permission to others. You can grant other users the ability to use the `sudo` command by editing a file with a special editor called `visudo`. This editor helps prevent errors in the file from removing everyone from being able to use the `sudo` command, which would actually prevent you from being able to fix the situation as editing that file requires the `sudo` command. To grant a user access to the `sudo` command run the following command to start editing the file listing sudo users
> ~~~
> $ sudo visudo -f /etc/sudoers.d/90-cloud-init-users
> ~~~
> {: .bash}
> ~~~
> # Created by cloud-init v. 20.1-10-g71af48df-0ubuntu5 on Thu, 10 Sep 2020 18:09:32 +0000
> 
> # User rules for ubuntu
> ubuntu ALL=(ALL) NOPASSWD:ALL
> ~~~
> {: .output}
> Below the last line add a new line exactly like the last line, except replacing `ubuntu` with the new user's username.
>
> Additionally to allow them to edit the files in the web root directory `/var/www/html` they would also need to be in the `webeditor` group
> ~~~
> $ sudo adduser USERNAME webeditor
> ~~~
> {: .bash}
>
> Finally you will need to get the new user to create a key pair as described earlier when you were first creating your VM and provide you with their public key which you need to place into their home directory to allow them to connect to the VM using their private key. To install the new users public key into their account, first switch to the new users account
> ~~~
> $ sudo su - USERNAME
> ~~~
> {: .bash}
> 
> Then create the `.ssh` folder and set the permissions:
> ~~~
> $ mkdir .ssh
> $ chmod o-rwx,g-rwx .ssh
> $ ls -al
> ~~~
> {: .bash}
> ~~~
> total 28
> drwxr-xr-x 3 USERNAME USERNAME 4096 Oct  1 14:14 .
> drwxr-xr-x 4 root     root     4096 Oct  1 13:38 ..
> -rw------- 1 USERNAME USERNAME   57 Oct  1 14:08 .bash_history
> -rw-r--r-- 1 USERNAME USERNAME  220 Oct  1 13:38 .bash_logout
> -rw-r--r-- 1 USERNAME USERNAME 3771 Oct  1 13:38 .bashrc
> -rw-r--r-- 1 USERNAME USERNAME  807 Oct  1 13:38 .profile
> drwx------ 2 USERNAME USERNAME 4096 Oct  1 14:14 .ssh
> ~~~
> {: .output}
> 
> Then edit a new file called `authorized_keys` in the `.ssh` folder
> ~~~
> $ nano .ssh/authorized_keys
> ~~~
> {: .bash}
> and add a single line containing the contents of their public key
> ~~~
> ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAgEAhkO+pSHhDmVNogr3hfHDV9jKCZacme+LLZk2nGYYNgPbCxOa+EmYPhLzwoqzElmUwTywMbSpOvh8C/kOOrluxcn39tcogIfnC9BxNsuZODjGFUI+xQVkys8bpMzjO2siN1JLqCAr7gAFaw/sujfu83FpYx2sYgh0RLhpr6Am065ayuVaDSANmVgeqvrbrkQyoY1YeOlVxuVnnlg54ur0C849SZedSV2ADQACrrn3heQKGpwsJ2dUwT6FXQBVdwJURTSYGSGqfnQgHhI55CK+8DG9dVJgxRv8PY8rBrrmkO/99VPhkQYMhdJKUaRGhl+WC8uL8WAo5XxnynJTvh1uoxhzoKq2zjKcdqMQAQW5wB9E3e8IxmS09HSOGBviOzIB2DPugue7x2/47OZCy1gFpJtGEcjwoFRLuSiCQW2aQgMgR2vxVEyJxv+F52r3Zsr8uiSKxh+z1Sd6ckoVOJ4wAHCWkvV48rBErhsd0+9Ra2pxd8V/b1pPOGSnC9UiY1sqc1G80vgObz2V+o/dB4SfrgYLyEeWclV6n3CXQBQ7styKYQX1jMAhfr9nAp83Liljbi6VUaznh074ItTVE2hgibmLDLqZ6V7OVFymySIcbCb/c6HlXVy9XWyR7JdeFIZn8ryFWmYk/6XmoUmtWqJt3gLQYwF0bWz4kWj5KYkl0d0= rsa-key-20160303
> ~~~
> {: .output}
> Save and exit the file. Next set the permissions on the new `authorized_keys` file
> ~~~
> $ chmod o-rwx,g-rwx .ssh/authorized_keys
> $ ls -l .ssh/
> ~~~
> {: .bash}
> ~~~
> total 4
> -rw------- 1 testuser testuser 738 Oct  1 14:18 authorized_keys
> ~~~
> {: .output}
> Finally, exit the new users account
> ~~~
> $ exit
> ~~~
> {: .bash}
{: .callout}


Lets remove the default landing page that our apache2 installation put in this folder so that when we create our new website with Jekyll it can write a new <code>index.html</code> file here without having to be run as the root user to overwrite the existing <code>index.html</code> file.
~~~
$ sudo rm /var/www/html/index.html
~~~
{: .bashrc}

The last step is to add our current user to the <code>webeditor</code> group.
~~~
$ sudo adduser ubuntu webeditor
~~~
{: .bash}
~~~
Adding user `ubuntu' to group `webeditor' ...
Adding user ubuntu to group webeditor
Done.
~~~
{: .output}

For this change to tack effect, disconnect and reconnect for the new group membership to take effect.
~~~
$ exit
~~~
{: .bash}
~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
~~~
Using username "ubuntu".
Authenticating with public key "rsa-key-20181121"
Passphrase for key "rsa-key-20181121":
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1011-kvm x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Sep 17 17:31:11 UTC 2020

  System load:  0.01               Processes:             74
  Usage of /:   12.8% of 19.21GB   Users logged in:       0
  Memory usage: 17%                IPv4 address for ens3: 192.168.0.141
  Swap usage:   0%

19 updates can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable

*** System restart required ***
Last login: Thu Sep 17 17:29:00 2020 from 198.90.95.246
~~~
{: .output}
~~~
$ groups
~~~
{: .bash}
~~~
ubuntu adm dialout cdrom floppy sudo audio dip video plugdev netdev lxd webeditor
~~~
{: .output}
Note that we are now a member of the <code>webeditor</code> group and are ready to create our first Jekyll website.

<!--Exercise ideas:
1. explore groups and permissions more
-->