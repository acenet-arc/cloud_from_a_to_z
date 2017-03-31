---
layout: episode
title: "Create a first virtual machine"
teaching: 60
exercises: 0
questions:
- "What are keypairs used for?"
objectives:
- "Create a key pair"
- "Create a VM which you can log into"
keypoints:
- "A Keypoint 0"
---

Now that you have an overview of OpenStack and have clicked around the dashboard it is time to create our first virtual machine. To create a virtual machine, we would click the "Launch Instance" button on the Instances panel, but before we do that there is at least one thing which we need to take care of first and that is, create a key to access our newly created virtual machine. Before we create a virtual machine we need to select a key to be injected into it which we can use to access the virtual machine.

## Accessing a Virtual Machine
Before we create a virtual machine we need to think about how we will access and use it. When you use your laptop or desktop computer you have a graphical interface which you click around and windows you type in to get your computer to do what you want. You might not know it but you can also run a terminal or **shell** program and type **commands** to get your computer to do things. The things done in the shell in some cases can be seen in the graphical interface. For example you can use the shell to create directories and files which you can see in the graphical file system viewer (e.g. Windows Explorer or Finder). We will use the shell to interact with our virtual machines. 

There is a shell called **Secure Shell** or **SSH** for short which is used to make remote connections between machines. SSH encrypts information sent between your local computer and a remote computer using a shared key. Encryption is a way of transforming text or data which is readable and understandable by anyone into text and data which is only understandable if one posses the key. SSH authentication keys (different from the shared key used to encode the messages) come in pairs, one public and one private. The public key is used to encrypt a message which contains the shared key that can only be decoded by the owner of the private key. The shared key sent in the message allows the two machines to send and receive sensitive information which only they can decode.

Lets make a pair of SSH authentication keys we can use to connect to our virtual machines. Start up your shell (a.k.a. a terminal) and you will see a **prompt**. A prompt is usually some text and characters to indicate that the shell is waiting for you to enter a command. In this lesson we will use the "`$`" to indicate a prompt which is likely somewhat different from what you see in your shell.

~~~
$
~~~
{: .bash}

First lets find out where we are by typing the command `pwd`, then press the Enter key to send the command to the shell. 
~~~
$ pwd
~~~
{: .bash}
~~~
/home/cgeroux
~~~
{: .output}
More specifically, when we type `pwd` and press the Enter key, the shell:
1. finds a program called `pwd`,
2. runs that program,
3. displays that program's output, then
4. displays a new prompt to tell us that it's ready for more commands.
The `pwd` command's output is the **present working directory**. In this case `/home/cgeroux`. This is known as a **home directory** where settings, files and programs for the user `cgeroux` are kept.

> ## Home Directory Variation
>
> The home directory path will look different on different operating systems. On Linux it might look like `/home/cgeroux` but on windows using mobaXterm it might look like `/home/mobaxterm` or on a Mac like `/Users/cgeroux`.
{: .callout}

The command to create a new key pair is `ssh-keygen` but before we run it lets have a look at the manual pages for the program by typing
~~~
$ man ssh-keygen
~~~
{: .bash}
~~~
SSH-KEYGEN(1)                                  BSD General Commands Manual                                 SSH-KEYGEN(1)

NAME
     ssh-keygen — authentication key generation, management and conversion

SYNOPSIS
     ssh-keygen [-q] [-b bits] [-t dsa | ecdsa | ed25519 | rsa | rsa1] [-N new_passphrase] [-C comment]
                [-f output_keyfile]
     ssh-keygen -p [-P old_passphrase] [-N new_passphrase] [-f keyfile]
     ssh-keygen -i [-m key_format] [-f input_keyfile]
     ssh-keygen -e [-m key_format] [-f input_keyfile]
     ssh-keygen -y [-f input_keyfile]
...
~~~
{: .output}
If you scroll down and read the description, you will notice that this command creates a key in the `~/.ssh` directory. The `~` is a synonym for your home directory and the `.` at the beginning of the directory name indicates that the directory is hidden. In the sense that the command `ls` will not show this directory unless the `-a` option is used. 

Lets check to see if you have a `.ssh` folder already in your home directory
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
if you do, have a look inside
~~~
$ ls ~/.ssh/
~~~
{: .bash}
~~~
id_rsa       id_rsa.pub   known_hosts
~~~
{: .output}
if you have a file pair `id_rsa` and `id_rsa.pub` or `id_dsa` and `id_dsa.pub` you already have a key pair and you can skip the next steps which create a new key pair and just use the key pair you already have.

To create a key pair run the command
~~~
$ ssh-keygen -t rsa -b 2048
~~~
{: .bash}
~~~
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mobaxterm/.ssh/id_rsa):
~~~
{: .output}
It is asking where to store the keypair, in this case lets just use the default location by pressing the `<return>` key. Then you will get
~~~
Created directory '/home/mobaxterm/.ssh'.
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
Your identification has been saved in /home/mobaxterm/.ssh/id_rsa.
Your public key has been saved in /home/mobaxterm/.ssh/id_rsa.pub.
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
now you have a key pair saved in the `.ssh` folder we can use with the cloud. To
verify lets take a look in the folder
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
Your public key can be given out freely, but remember to keep your private key secret. One final thing I would like to point out about keys is their file permissions. Run the command
~~~
$ ls -l ~/.ssh/
~~~
{: .bash}
~~~
-rw-r--r--    1 cgeroux  UsersGrp      1766 Mar 31 15:12 id_rsa
-rw-r--r--    1 cgeroux  UsersGrp       396 Mar 31 15:12 id_rsa.pub
~~~
{: .output}
to show the permissions on the files inside the `.ssh` folder. The file permissions are displayed in the far left column. Possible file permissions are `r` for read, `w` for write, and `x` for execute. You will notice the dashes which indicate unset permissions. The first `-` will be a `d` if the item is a directory next followed by the three permissions (rwx) for the owner (in this case the user `cgeroux`). Next are the permissions for the group the file belongs to (in this case `UsersGrp`) and finally the permissions for everyone else. In this case you can see that the private key `id_rsa` is actually readable by any user on this computer. Since you should keep your private key private it is good practice to set the permissions on this file to be readable only by the owner of the file. This can be done using the `chmod` command.
~~~
$ chmod og-r ~/.ssh/id_rsa
~~~
{: .bash}
this will remove read (-r) permissions for others (o) and members of the files group (g). Now running
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
However while mobaXterm appears much like a fully functioning Linux terminal there are some limitations. For example this chmod command does not always have an effect. However, on Mac and Linux machines the correct result should be observed. The `.ssh` directory should also have restricted permissions so that only the owner has read permissions.
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
If these permissions are to open the command we use to connect to other computers may complain. 
> ## File permissions variations
>
> In the case of mobaXterm the ssh command does not require strict permissions, however on Linux machines or Macs the `ssh` command does require stricter permissions before it will allow you to connect using a private key.
{: .callout}

---
PREREQUISITES
* need to know `ls`, `ls -l`
 * should maybe also know a bit more
    * `rm`
    * `mkdir`
    * `cat`
* file permissions
  * user, group, everyone
  * wrx
  * `chmod`
* need to know about `.ssh` folder
  * `authorized_keys`
  * `known_hosts`
  * `id_rsa`
  * `id_rsa.pub`

---
OUTLINE

* Key pairs
  * Describe key pairs and what they are for
    * need to mention about SSH
  * Creating one using the OS dashboard
  * Creating one on the client (Windows/Linux/Mac) and importing it into OS
    * `ssh-keygen`
* Launch a VM
  * Name: Valid host names apply
  * Flavor: describe meaning of flavor names
  * Boot Source: Image, will talk about other boot sources more later (e.g. persistent VMs)
  * Image Name:
  * Select a key pair
  * Keep default security group
  * Post creation, mention quickly, e.g. allows you to automatically configure your VM using a script (e.g. update OS, install software etc.) will be discussed more later (e.g. cloudInit).
* Network
  * Private IP vrs. Public IP
  * Allocating a Public IP
  * Associating it with the VM
  * Security Groups add SSH rule
* Connecting
  * SSH using key pair
    * Windows -> Putty/MobaXterm
    * Linux/Mac -> use built in terminal
