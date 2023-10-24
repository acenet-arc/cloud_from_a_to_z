---
layout: episode
title: "Creating a keypair"
teaching: 25
exercises: 10
questions:
- "What is a shell?"
- "What is SSH?"
- "What are key-pairs and how do you create one?"
- "How do you view and set file permissions?"
objectives:
- "Learn how to use the shell."
- "Learn some basic Linux commands."
- "Get a rough overview of a Linux filesystem."
- "Create a key pair."
- "Understand the basics of Linux file permissions."
keypoints:
- "A [**shell**](../reference#shell) is a text based method for interacting with a computer."
- "[**SSH**](../reference#ssh) is a Secure SHell that allows remote interaction with a computer."
- "An SSH [**key pair**](../reference#key-pair) allows a user to be authenticated on a remote computer."
- "The [**Linux**](../reference#linux) filesystem is a tree with <code>/</code> at the root and directories creating branches."
- "The [**cd**](../reference#cd) command is used to change directories."
- "The [**pwd**](../reference#pwd) command is used to display the current working directory."
- "The [**ls**](../reference#ls) command is used to list the directory structure."
- "The [**ssh-keygen**](../reference#ls) command is used to create key pairs."
- "The [**cat**](../reference#ls) command is used print the contents of a file to the terminal."
- "The [**chmod**](../reference#chmod) command is used change the file mode or permissions."
- "The [**private key**](../reference#private-key), <code>id_rsa</code>, must only be readable and writable by the file's owner."
start: true
start_time: 780
---

Now that you have an overview of OpenStack and have clicked around the dashboard it is time to create our first virtual machine. To create a virtual machine, we would click the *Launch Instance* button on the Instances panel, but before we do that there is one thing we need to take care of first and that is creating a key (and lock) to access our newly created virtual machine. The key will allow only the person possessing it to access the VM. You wouldn't want just anyone connected to the Internet to access your newly created VM. While creating a virtual machine we need to select a lock, corresponding to a key we posses, to be put on the virtual machine.

We have already been using SSH to issue commands on a shared remote computer to build our Jekyll sites and connected using a username, password and the IP address of the remote computer. However, when we create our own virtual machines we will have administrative access to those machines. This greater control, should be accompanied with greater security and using an ssh key pair will improve our ssh security greatly.

> ## Password Authentication & Brute force attacks
> In the shared VMs we used in the beginning of this workshop we used password authentication rather than ssh keys mainly to keep things simple when we started out. In order keep the VM secure a program called [fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page) was installed and configured on this VM. This program bans any IPs with multiple failed ssh connection attempts.
>
> This was to thwart ssh **brute force attacks**. A brute force attack is when many usernames and passwords are attempted, usually in an automated way, to try and gain access. Brute force attacks are exceedingly common and often in a few minutes to days any computer accessible publicly over ssh will receive a brute force attack. SSH keys are the best way to thwart these attacks, but if password authentication is really needed it must be combined with some method of mitigating brute force attacks such as fail2ban.
>
> Another great way of controlling access is to restrict which IP address can connect to your VM. We will see how to do that shortly. In general though, it is best have security in layers. If one layer should fail, another layer will prevent access.
{: .callout}

SSH keys come in pairs, one public (think of this as a lock) and one private (think of this as the key). The [**public key**](../reference#public-key) is used to encrypt a message which can only be decoded by the owner of the [**private key**](../reference#private-key). In this way the machine sending a message encoded using the public key can be sure that the machine responding has the private key which can decode the message is in possession of the private key. In this way the key pair can be used to authenticate or verify that the user is who they claim to be or at the very least that they posses the matching private key.

Lets make a pair of SSH authentication keys we can use to connect to our virtual machines.

The command to create a new key pair is `ssh-keygen` which creates a key in the `~/.ssh` directory. The `~` is a synonym for your home directory (e.g. `/home/cgeroux`) and the `.` at the beginning of the directory name indicates that the directory or file is hidden. Hidden files will not be shown by the `ls` command unless the `-a` option is used.

Lets check to see if you have a `.ssh` folder already in your home directory.
~~~
$ ls -a ~
~~~
{: .bash}
~~~
.                         .bashrc                  .viminfo
..                        .gitconfig                Desktop
.aptcyg                   .python_history           LauncherFolder
.bash_history             .ssh                      MyDocuments
~~~
{: .output}

> ## `.` and `..` directories
> Notice that in addition to the hidden directory `.ssh` we also have hidden directories `.` and `..` as well as others. The `.` and `..` are special directories. The double dot is a shortcut for the parent directory, or the directory which contains your home directory (e.g. `/home/`). The single dot is a shortcut for the directory its self, your home directory (e.g. `/home/cgeroux`). The single dot can be used to reference the current directory by starting the path with a `.` (e.g. `./MyDocuments`). Remember when we did `cd ..` to go up one directory? How about when we talked about relative directories `./Documents/pictures`. Both of these use the `..` and `.` shortcuts.
{: .callout}

If you do have a `.ssh` folder, have a look inside.
~~~
$ ls ~/.ssh/
~~~
{: .bash}
~~~
id_rsa       id_rsa.pub   known_hosts
~~~
{: .output}
Notice that the a forward `/` is used to separate directories. In this case the `.ssh` directory is inside the home directory `~` (or in this case `/home/cgeroux`). If you have a pair of files `id_rsa` and `id_rsa.pub` you already have a key pair. If you **remember the passphrase**, if it has one, you can skip the next steps which create a new key pair and just use the key pair you already have.

> ## Have an `id_rsa` key pair but forget the passphrase?
> Lets rename your existing `id_rsa` and matching `id_rsa.pub` to new file names to save key in case you need it later.
> ~~~
> $ mv ~/.ssh/id_rsa ~/.ssh/old_id_rsa
> $ mv ~/.ssh/id_rsa.pub ~/.ssh/old_id_rsa.pub
> ~~~
> {: .bash}
> This way we won't overwrite the existing key when we create a new one so that if you find you need it later you still have the key.
{: .callout}

## Creating a key-pair

**Only create a new key-pair if you don't already have a key**

To create a key pair run the command
~~~
$ ssh-keygen -t rsa -b 2048
~~~
{: .bash}
~~~
Generating public/private rsa key pair.
Enter file in which to save the key (/home/cgeroux/.ssh/id_rsa):
~~~
{: .output}
It is asking where to store the keypair, in this case lets just use the default location by pressing the `<return>` key. Then you will get
~~~
Created directory '/home/cgeroux/.ssh'.
Enter passphrase (empty for no passphrase):
~~~
{: .output}
at which point you should enter a passphrase which will be required to 'unlock' the private key. A passphrase is different from a password in that it can contain multiple words. The longer the passphrase the better, though at some point it gets a pain to type frequently.
~~~
Enter same passphrase again:
~~~
{: .output}
then reneter the passphrase and
~~~
Your identification has been saved in /home/cgeroux/.ssh/id_rsa.
Your public key has been saved in /home/cgeroux/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:WKM/Rx7bBCqPH7DLuXww3xnu0YqL+H1enJHFER1zt/4 cgeroux@Caelia
The key's randomart image is:
+---[RSA 2048]----+
|              o=+|
|             . .*|
|        o .   o. |
|       + o . o.  |
|      = S o +  . |
|      oB o.B o  .|
|      o+=o=o*   E|
|     + *o==+     |
|    ..Oo==+      |
+----[SHA256]-----+
~~~
{: .output}
now you have a key pair saved in the `.ssh` folder we can use with the cloud.

-----------------------------

To verify lets take a look in the folder
~~~
$ ls ~/.ssh/
~~~
{: .bash}
~~~
id_rsa      id_rsa.pub
~~~
{: .output}

This key pair consists of the private key (the file `~/.ssh/id_rsa`) and a public key (the file `~/.ssh/id_rsa.pub`). You can have a look at the contents of the key files using an editor or a command called `cat` which just prints the contents of a file to the terminal.
~~~
$ cat ~/.ssh/id_rsa.pub
~~~
{: .bash}
~~~
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxo6H/dDFLunQOUKnTUxNfHTsDfARFdFjqyJrf2udOBAzm7hg/w4SaHAqF1b1DvmGhwKwXW6lXYkdsiA5d4IK/Cg8GZ7l74J1QTQ+e6JkdvOmVlTGnu6PTesd++6jZUeiF9Im0ksGPTYo8QH/5k1eHUMwWpUh9xfX0Z56IdUyNxx+/QaeCc61sUvIPf+w2Vm/zC44C+v5OX4lDWlamLf2b0u6be5L99UXWN8741354auMP8qVMidRq8jQjUmlto30b/2H9bMFGQ63eEApEnhe6s+qdxVlbLkKHT2H905ydXf4knAY3TGlgylBNbXjeiJEp9mKlQ5LnIi6rayxzDrIv cgeroux@Caelia
~~~
{: .output}
Your public key can be given out freely, **but remember to keep your private key secret**.

We will use this public key in the next episode when we create our first virtual machine.

### Key file and directory permissions

One final item we should cover about keys is their file permissions. If the file permissions, specifically of the .ssh directory and the private key, are too open the command we use to connect to a VM will complain about this and not allow us to connect. To see what the current file permissions are run the `ls` command with the `-l` option to show the permissions on the files inside the `.ssh` folder.
~~~
$ ls -l ~/.ssh/
~~~
{: .bash}
~~~
-rw-r--r--    1 cgeroux  UsersGrp      1766 Mar 31 15:12 id_rsa
-rw-r--r--    1 cgeroux  UsersGrp       396 Mar 31 15:12 id_rsa.pub
~~~
{: .output}
The file permissions are displayed in the far left column. Possible file permissions are `r` for read, `w` for write, and `x` for execute. You will notice the dashes which indicate unset permissions. The first `-` will be a `d` if the item is a directory, followed by the three permissions (rwx) for the user who owns the file (in this case the user `cgeroux`). Next are the permissions for the group the file belongs to (in this case `UsersGrp`) and finally the permissions for everyone else. In this case you can see that the private key `id_rsa` is actually readable by any user on this computer. Since you should keep your private key private it is good practise to set the permissions on this file to be readable only by the owner of the file. This can be done using the `chmod` command.
~~~
$ chmod og-r ~/.ssh/id_rsa
~~~
{: .bash}
The above command will remove (`-`) read (`r`) permissions for others (`o`) and users who are members of the file's group (`g`). You can also specify changes in permissions for the user which owns the file with `u` and add permissions by using a `+` instead of the `-` as well as specify multiple permissions at once (e.g. `chmod u+rwx <file-name>`).

Issuing the `ls` command again shows the changes to the permissions.
~~~
$ ls -l ~/.ssh
~~~
{: .bash}
~~~
total 3
-rw-------    1 cgeroux  UsersGrp      1766 Mar 31 15:12 id_rsa
-rw-r--r--    1 cgeroux  UsersGrp       396 Mar 31 15:12 id_rsa.pub
~~~
{: .output}
> ## MobaXTerm file permissions
> While mobaXterm appears much like a fully functioning Linux terminal there are some limitations, likely due to the fact that it is actually running on Windows. For example this chmod command does not always have an effect. However, on Mac and Linux machines the correct result should be observed.
{: .callout}

The `.ssh` directory should also have restricted permissions so that only the owner has read permissions.
~~~
$ chmod og-rx ~/.ssh
$ ls -al ~/
~~~
{: .bash}
~~~
drwxr-xr-x    1 cgeroux  UsersGrp         0 Mar 31 15:42 .
drwxr-xr-x    1 cgeroux  UsersGrp         0 May 18  2016 ..
drwxr-xr-x    1 cgeroux  UsersGrp         0 Jun 11  2016 .aptcyg
-rw-r--r--    1 cgeroux  UsersGrp     56801 Mar 31 16:09 .bash_history
-rw-r--r--    1 cgeroux  UsersGrp         0 Sep 12  2016 .bashrc
-rw-r--r--    1 cgeroux  UsersGrp        83 May 19  2016 .gitconfig
-rw-r--r--    1 cgeroux  UsersGrp        20 Sep  1  2016 .python_history
drwx------    1 cgeroux  UsersGrp         0 Mar 31 15:42 .ssh
-rw-r--r--    1 cgeroux  UsersGrp     10302 Mar  3 11:22 .viminfo
lrwxrwxrwx    1 cgeroux  UsersGrp        32 May 18  2016 Desktop -> /drives/C/Users/cgeroux/Desktop/
lrwxrwxrwx    1 cgeroux  UsersGrp        28 May 18  2016 LauncherFolder -> /drives/C/PROGRA~2/MOBAXT~1/
lrwxrwxrwx    1 cgeroux  UsersGrp        33 May 18  2016 MyDocuments -> /drives/C/Users/cgeroux/DOCUME~1/
~~~
{: .output}
If these permissions are too open the command we use to connect between computers may complain.
> ## SSH File permissions variations
>
> In the case of mobaXterm the `ssh` command does not require strict permissions, however on Linux machines or Macs the `ssh` command does require stricter permissions before it will allow you to connect using a private key. In addition depending on the details of your windows operating system and version of mobaXterm you may or may not actually be able to change file permissions within mobaXterm.
{: .callout}

Now we have a key pair we can use to connect to our the VM we will create in the next episode.

> ## Read file permissions
> Given the following output from an `ls -l` command
> ~~~
> -rw---xrw-  1 jsmith smiths     0 Oct 15 19:33 file-name
> ~~~
> {: .output}
> who can read the file, select all that apply
>
> 1. the owner `jsmith`
> 2. the group `smiths`
> 3. the owner `smiths`
> 4. other users
>
> > ## Solution
> >
> > 1. yes: the file permissions for the owner of the file `jsmith` are `rw-`, which contains the `r`, or read permission.
> > 2. no: the file permissions the group `smiths` are `--x`, which does not contain the read permission, `r`.
> > 3. no: `smiths` is the group the file belongs to, not the user who owns the file. The file's group, `smiths`, does not have read permission.
> > 4. yes: the file permissions for all other users on the computer are `rw-` which does contain the read permission, `r`.
> >
> {: .solution}
{: .challenge}

<!-- > ## File permissions
>
> The `touch` command can be used to create a new empty file or to change the time which the file was last modified if it already exists. Use the `touch` command to create a new file.
> ~~~
> $ touch ~/file-name
> ~~~
> {: .bash}
> Then view and adjust the file permissions so that only "others" (`o`) have read/write access. Can you as the owner still read the file?
> > ## Solution
> >
> > ~~~
> > $ chmod ug-rwx ~/file-name
> > $ cat ~/file-name
> > ~~~
> > {: .bash}
> > ~~~
> > cat: /home/cgeroux/test.txt: Permission denied
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge} -->
