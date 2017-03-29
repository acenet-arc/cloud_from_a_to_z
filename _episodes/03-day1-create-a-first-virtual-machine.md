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
Before we create a virtual machine we need to think about how we will access and use it. When you use your laptop or desktop computer you have a graphical interface which you click around and windows you type in to get your computer to do what you want. You might not know it but you can also run a terminal or **shell** program and type **commands** to get your computer to do things. The things done in the shell in some case can be seend in the graphical inerface. For example you can use the shell to create directories and files which you can see in the graphical file system viewer (e.g. Windows Explorer or Finder). We will use the shell to interact with our virtual machines. 

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
1. find a program called `pwd`,
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
