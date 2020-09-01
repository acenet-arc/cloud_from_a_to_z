---
layout: episode
title: "Creating a keypair"
teaching: 15
exercises: 15
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
---

Now that you have an overview of OpenStack and have clicked around the dashboard it is time to create our first virtual machine. To create a virtual machine, we would click the *Launch Instance* button on the Instances panel, but before we do that there is one thing we need to take care of first and that is creating a key (and lock) to access our newly created virtual machine. The key will allow only the person possessing it to access the VM. You wouldn't want just anyone connected to the Internet to access your newly created VM. While creating a virtual machine we need to select a lock, corresponding to a key we posses, to be put on the virtual machine.

Before we create a key and lock lets take one more step back to talk about how we will connect to and interact with our virtual machines as this will influence how we use our key. When we use our laptop or desktop computer we have a graphical interface which we click around and windows you type in to get your computer to do what you want. You might not know it but you can also run a [**terminal**](../reference#terminal) or [**shell**](../reference#shell) program and type [**commands**](../reference#command) to get your computer to do things. The things done in the shell in some cases can be seen in the graphical interface. For example you can use the shell to create directories and files which you can see in a graphical file system viewer (e.g. Windows Explorer or Finder). We will use the shell to interact with our virtual machines. Also often virtual machines run a [**Linux**](https://en.wikipedia.org/wiki/Linux) operating system, which is a family of free, open-source, operating systems. In this course we will focus specifically on the [**Ubuntu**](../reference#ubuntu) distribution of Linux.

In addition to the shell just mentioned there is a shell called **Secure Shell** or [**SSH**](../reference#ssh) for short which is a shell to interact remotely with machines to send commands and get the output back. SSH [**encrypts**](../reference#encryption) information sent between your local computer and a remote computer using a shared key. Encryption is a way of transforming text or data which is readable and understandable by anyone into text and data which is only understandable if one posses the key. SSH authentication keys (different from the shared key used to encode the messages) come in pairs, one public (think of this as a lock) and one private (think of this as the key). The [**public key**](../reference#public-key) is used to encrypt a message which contains the shared key that can only be decoded by the owner of the [**private key**](../reference#private-key). In this way the machine sending a message encoded using the public key can be sure that the machine responding has the private key which can decode the message. In this way the key pair can be used to authenticate or verify that the user is who they claim to be. A shared key sent in the message allows the two machines to send and receive sensitive information which only they can decode. Having the information sent between machines is important if any sensitive information, say a password, is sent as it is very possible that someone could eavesdrop on the data sent across the Internet to/from the remote machine.

Lets make a pair of SSH authentication keys we can use to connect to our virtual machines. Start up your shell (a.k.a. a terminal) and you will see a [**prompt**](../reference#prompt). A prompt is usually some text and characters to indicate that the shell is waiting for you to enter a command. In this lesson we will use the "`$`" to indicate a prompt which is likely somewhat different from what you see in your shell.

> ## Accessing your terminal
>
> **Windows**: startup mobaXterm and then click *Start local terminal*
>
> **Mac**: search in *spotlight* for terminal click on search result *terminal*
>
> **Linux**: if using a newer version of Ubuntu try searching for *terminal* with unity's search tool (usually in the top left of the screen on the tool bar)
{: .callout}

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

The `pwd` command's output is the **present working directory**. In this case `/home/cgeroux`. This directory known as a **home directory** where settings, files and programs for the user `cgeroux` are kept. The string `/home/cgeroux` is known as a path which indicates a specific file or directory within a file system. File systems have a tree like structure, starting at the root of the file system (`/`) and branching out from there. Each new directory creates a new branch in the file system. Directories are seperated in a path by forward slashes, `/` so that a directory inside another one can be represented like `/home` in this case, the `home` directory is inside the root directory `/`.  Adding another directory in depth to the path we have `/home/cgeroux` which is a directory inside the `home` directory.

To change your **present working directory** there is a command called `cd` for change directory. It takes one **argument** which specifies which directory to change to.
~~~
$ cd /home
$ pwd
~~~
{: .bash}
~~~
/home
~~~
{: .output}
as you can see the `pwd` command now tells you that you are in the directory `/home`. Lets now move back to our home directory. Your home directory name will be different from mine and be the output from the first execution of `pwd`.
~~~
$ cd /home/cgeroux
~~~
{: .bash}

There is a common file system layout across most Linux systems. The below figure shows an overview of some of the more relevant directories within a Linux file system for this lesson, however there are more directories than are shown here.

![file system](../fig/filesystem-truncated.svg)

* `/home`: home directories of users
* `/bin`: essential user command binaries (e.g. `ls`,`cat`,`bash`, ...)
* `/etc`: settings and configurations for the system
* `/var`: variable data files (e.g. `logs` and website data `www`)
* `/dev`: device files, (e.g. hard drive, usb, and cd-rom devices)

> ## Home Directory Variation
>
> The home directory path will look different on different operating systems. On Linux it might look like `/home/cgeroux` but on windows using mobaXterm it might look like `/home/mobaxterm` or on a Mac like `/Users/cgeroux`.
{: .callout}

So far we have been using what are known as **absolute paths**. An absolute path is a path which starts with a `/` that is they start from the root of the file system. Absolute paths reference the same location no matter where they are used. There are also paths known as **relative paths** which are relative to your current working directory. These can either start with a `.` to indicate the current directory (e.g. `./Documents/pictures`), or the can just start with the directory name (e.g. `Documents/pictures`). This is different from an absolute directory which always begins with a `/`. 

In addition to the `.` shorthand for the current directory there is a `..` shorthand for parent directory of the current directory. Lets try moving up to the parent directory using a relative path using the `..` shorthand.
~~~
$ cd ..
$ pwd
~~~
{: .bash}
~~~
/home
~~~
{: .output}
Then back to our home directory.
~~~
$ cd cgeroux
~~~
{: .bash}

The command to create a new key pair is `ssh-keygen` but before we run it lets have a look at the manual pages for the command by typing
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
Many commands have manual pages, so executing the command `man <some-command-name>` will display information about that command, how to use it, and the options available for that command. Options for a command are specified after the command with a `-` followed directly by the option identifier for example, `-a`. If you scroll down the manual pages (by pressing the down arrow key) and read the description, you will notice that this command creates a key in the `~/.ssh` directory. The `~` is a synonym for your home directory (e.g. `/home/cgeroux`) and the `.` at the beginning of the directory name indicates that the directory or file is hidden. The command `ls` is used to list the file structure, or in other words list files and directories inside a directory given as an argument to the command. If no argument is given `ls` will list the files and directories inside the current directory. Hidden files will not be shown by the `ls` command unless the `-a` option is used. 

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

Notice that in addition to the hidden directory `.ssh` we also have hidden directories `.` and `..` as well as others. The `.` and `..` are special directories. The double dot is a shortcut for the parent directory, or the directory which contains your home directory. The single dot is a shortcut for the directory its self, your home directory, as was mentioned when talking about relative paths. The single dot can be used to reference the current directory by starting the path with a `.` (e.g. `./MyDocuments`).

If you do have a `.ssh` folder, have a look inside.
~~~
$ ls ~/.ssh/
~~~
{: .bash}
~~~
id_rsa       id_rsa.pub   known_hosts
~~~
{: .output}
Notice that the a forward `/` is used to separate directories. In this case the `.ssh` directory is inside the home directory `~` (or in this case `/home/cgeroux`). If you have a pair of files `id_rsa` and `id_rsa.pub` or `id_dsa` and `id_dsa.pub` you already have a key pair and you can skip the next steps which create a new key pair and just use the key pair you already have.

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
Your public key can be given out freely, but remember to keep your private key secret.

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

> ## Absolute vs Relative Paths
>
> If the present working directory is `/Users/amanda/data/`,
> which of the following commands could Amanda use to navigate to her home directory,
> which is `/Users/amanda`?
>
> 1. `cd .`
> 2. `cd /`
> 3. `cd /home/amanda`
> 4. `cd ../..`
> 5. `cd ~`
> 6. `cd home`
> 7. `cd ~/data/..`
> 8. `cd`
> 9. `cd ..`
>
> > ## Solution
> > 1. No: `.` stands for the current directory.
> > 2. No: `/` stands for the root directory.
> > 3. No: Amanda's home directory is `/Users/amanda`.
> > 4. No: this goes up two levels, i.e. ends in `/Users`.
> > 5. Yes: `~` stands for the user's home directory, in this case `/Users/amanda`.
> > 6. No: this would navigate into a directory `home` in the current directory if it exists.
> > 7. Yes: unnecessarily complicated, but correct.
> > 8. Yes: shortcut to go back to the user's home directory.
> > 9. Yes: goes up one level.
> {: .solution}
{: .challenge}

> ## Relative Path Resolution
>
> Using the filesystem diagram below, if `pwd` displays `/Users/thing`,
> what will `ls ../backup` display?
>
> 1.  `../backup: No such file or directory`
> 2.  `2012-12-01 2013-01-08 2013-01-27`
> 3.  `2012-12-01/ 2013-01-08/ 2013-01-27/`
> 4.  `original pnas_final pnas_sub`
>
> ![File System for Challenge Questions](../fig/filesystem-challenge.svg)
>
> > ## Solution
> > 1. No: there *is* a directory `backup` in `/Users`.
> > 2. No: this is the content of `Users/thing/backup`,
> >    but with `..` we asked for one level further up.
> > 3. No: see previous explanation.
> >    Also, we did not specify `-F` to display `/` at the end of the directory names.
> > 4. Yes: `../backup` refers to `/Users/backup`.
> {: .solution}
{: .challenge}

> ## File permissions
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
{: .challenge}