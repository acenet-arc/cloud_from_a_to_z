---
layout: episode
title: "Creating a persistent virtual machine"
teaching: 20
exercises: 10
questions:
- "How do you create a virtual machine?"
- "What is an OpenStack flavor?"
- "What is a floating IP?"
- "How can I allow SSH traffic into my virtual machine?"
objectives:
- "Create a VM."
- "Associate a floating IP with a VM."
- "Add security rules to allow traffic into a VM."
- "Connect to a VM using SSH."
keypoints:
- "The [**flavor**](../reference#flavor) of a VM prescribes the hardware profile of the VM."
- "A [**boot source**](../reference#boot-source) specifies from what the VM should [**boot**](../reference#boot)."
- "A [**public key**](../reference#public-key) must be inject into the VM in order to connect to it."
- "A [**floating IP**](../reference#floating-ip) must be added to a VM to connect to it from outside the local network in the cloud."
- "[**Port**](../reference#port) 22 must be opened in the security rules to allow [**SSH**](../reference#ssh) to connect to the VM."
- "A [**security group**](../reference#security-group) controls which ports to allow traffic in and out on."
---

## Creating a virtual machine
Now we will create your first virtual machine and connect to it using SSH.

To do so go to the OpenStack dashboard and select from the left hand menu *Compute*->*Instances* and click *Launch Instance* button in the top right of the panel.

You are presented with a panel consisting of multiple tabs of fields to fill in. There are many optional fields which can allow additional functionality, but for this first exposure will stick to the basics.

### Details tab

**Instance Name:** specify the name of your virtual machine. OpenStack will attempt to use this name as the [**hostname**](../reference#hostname) of your virtual machine. However, if the instance name you provided is not a valid hostname OpenStack will modify it so that it is valid and use the modified version for your hostname while still referring to your VM in the OpenStack dashboard by the instance name you provided. As some of us are sharing a project, please include your name in the instance name. If you name was `John Smith` you might use something like `john-smith`. That way it will be obvious who's VM is who's.

> ## What is a valid hostname?
> A good description of a valid hostname is given in this [wikipedia page section](https://en.wikipedia.org/wiki/Hostname#Syntax). The official specifications for hostnames are given in two Internet standards requests for comments documents [RFC-952](https://tools.ietf.org/html/rfc952), and [RFC-1123](https://tools.ietf.org/html/rfc1123).
> The summary of the wikipedia page is, hostnames must be less than 64 characters long, contain only numbers letters and dashes (`-`).
{: .callout}

**Description:** optionally enter a description of the VM.

**Availability Zone:** this allows you some control over where your VM is run. For example if you want to have less of a chance that two VMs will be unavailable at the same time it maybe helpful to put them into different availability zones. For now we will leave it as `Any Availability Zone`.

**Count:** this specifies the number of VMs to create. We want to create only 1 VM so leave it at `1`.

### Source tab
Here we pick what the VM boots from. Booting means to start a computer and put it into a state in which it is ready to operate. When we say it will boot from something, that means it will use the data and programs on that disk or file to start running.

You can create a VM which boots from an Image, volume, or snapshot. Since we don't have any existing volumes or snapshots we will choose an image as a boot source. Because we are creating a persistent VM we will want to create a new volume onto which the selected image will be copied. Persistent VMs are designed to work best with volumes where data is more permanent than other options. 20 GB is a good size to hold our operating system and some programs and files we might want to work with. We also want to be able to delete our VM and keep our volume. I would highly recommend always selecting "No" for "Delete Volume on Instance Delete" as there are situations where having these to decoupled can be very handy, for example injecting a new public key if you accidentally lost your private key.

**Select Boot Source:** Image

**Create New Volume:** Yes

**Volume Size(GB):** 20

**Delete Volume on Instance Delete:** No

Select the `Ubuntu-22.04.2-Jammy-x64-2023-02` image by clicking on the arrow pointing upwards next to it so that it appears under `Allocated`.

### Flavor tab
The [**flavor**](../reference#flavor) of your VM specifies the hardware profile your VM will have. Alliance clouds use a consistent naming scheme across their clouds to describe the hardware profile.  Examples of VM flavors are `p1-1.5gb` and `c1-7.5gb-30` and the different components of the name correspond to different hardware features.

* Flavors beginning with a `p` indicates a [**persistent flavor**](../reference#persistent-flavor). Persistent flavors or VMs are expected to run for long periods of time, provide web services such as websites and are run on hardware which is well suited to these workloads.

* Flavors beginning with a `c` indicates a [**compute flavor**](../reference#compute-flavor). Compute flavors or compute VMs are expected to run for shorter periods of time and be temporary. These VMs are expected to make heavy use of the CPU during their total existence with nearly 100% usage, unlike persistent VMs which may only do something ever once and a while when some one makes a request for the service they provide.

* The number after the 'p' or 'c' indicates the number of virtual central processing units ([**VCPUs**](../reference#vcpu))

* The number after then first '-' indicates the amount of RAM in GB for example the flavor `c1-7.5gb-30` has 7.5 GB of [**RAM**](../reference#ram)

* The final number, which only occurs in flavors starting with a `c`, is the size in GB of an extra [**ephemeral disk**](../reference#ephemeral-disk) in addition to the disk that the virtual machine's operating system resides. This extra disk can be used to store temporary data, but will be lost once the virtual machine is deleted unless special care has been taken to save it else where.

We will use the `p1-1.5gb` flavor. Click the arrow pointing up in the row for that flavor.

**Flavor**: `p1-1.5gb`

> ## Flavor variations
> If you are on a different Compute Canada cloud, such as East cloud, you might have a different set of flavors, however you should still be able to pick something relatively close to this one. For example on East cloud a `p1-0.75gb` flavor has about half the RAM but the same number of VCPUs and is also a persistent flavor. For this workshop this flavor will work just as well.
{: .callout}

### Networks tab
Arbutus cloud now supports both IPv4 and the newer IPv6 protocols. Each of these protocols is associated with a different network within an OpenStack project. In this workshop will stick to using the older IPv4 protocols. However, this means we must select the network name which contains the project name (e.g. `def-training-cloud`) rather than the *IPv6-GUA* network.

### Key Pair tab

The final piece of information we need to provide before creating a VM is the public key we created in the previous episode to allow you to connect to the VM you create. Click on the `Import Key Pair` to bring up a dialogue allowing you to specify the key pair name, type, and the public key itself. You can copy your public key text by going to your terminal on your laptop where you created your key pair in the last episode and running the command

~~~
$ cat .ssh/id_rsa.pub
~~~
{: .bash}
~~~
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxo6H/dDFLunQOUKnTUxNfHTsDfARFdFjqyJrf2udOBAzm7hg/w4SaHAqF1b1DvmGhwKwXW6lXYkdsiA5d4IK/Cg8GZ7l74J1QTQ+e6JkdvOmVlTGnu6PTesd++6jZUeiF9Im0ksGPTYo8QH/5k1eHUMwWpUh9xfX0Z56IdUyNxx+/QaeCc61sUvIPf+w2Vm/zC44C+v5OX4lDWlamLf2b0u6be5L99UXWN8741354auMP8qVMidRq8jQjUmlto30b/2H9bMFGQ63eEApEnhe6s+qdxVlbLkKHT2H905ydXf4knAY3TGlgylBNbXjeiJEp9mKlQ5LnIi6rayxzDrIv cgeroux@Caelia
~~~
{: .output}

and copying this text into the *Public Key* text field on the OpenStack dashboard. Provide a *Key Pair Name* which will distinguish this key from other keys you might have, something like `laptop-key` or `work-desktop-key` and the *Key Type* is 'SSH Key'.

Then click the *Import Key Pair* button to add that public key to your OpenStack account. This public key can then be selected from list of key pairs below by clicking on the up arrow next to the key-pair name. This public key can also be used for other future virtual machines and across projects.

Finally click the *Launch Instance* button at the bottom of the *Launch Instance* panel to create your first virtual machine!

## Associating a Floating IP with a VM
To connect to your virtual machine you will need to associate a [**Public IP**](../reference#public-ip) with your virtual machine. Doing so will create a pointer from a publicly accessible IP to your virtual machine. This publicly accessible IP is also known as a [**floating IP**](../reference#floating-ip) perhaps because the IP can "float" from one virtual machine to another. The public IP associated with your VM allows other machines to connect to your VM across the Internet. This is different from the [**private**](../reference#private-ip) or local IP your VM gets by default, which only identifies the virtual machine on the local network within your cloud project.

To associate a floating IP with your newly created virtual machine:
* Click on the drop down menu on the right side of your newly create virtual machine and select *Associate Floating IP*.<br/>
This will bring up a panel to select an IP Address. Chances are you will not yet have a floating IP added to your project.<br/>
<br/>
  To add a new floating IP:
  * Click the *+* button next to the drop down box *IP Address*.
  * Select a *Pool* to allocate the floating IP from. There will likely be only one.
  * Select *Allocate IP*. This will then take you back the previous panel and you can select the newly allocated floating IP from the drop down box.<br/>
<br/>
* Check that the *Port to be associated* already has your newly created VM selected.
* Click *Associate*.

The floating IP we just associated with your newly created VM will be the IP address we use to connect to your VM.

> ## Different usage of the word "Port"
> Earlier we talked about ports as numbers indicating a type of service for example a website or the HTTP service being associated with the port number 80. In this case the OpenStack dashboard is using the word port to refer to a virtual machine. Unfortunately this vagueness of how the word port is used can be a bit confusing.
{: .callout}

## Adding SSH Security Rule
To connect to the virtual machine we will be using SSH which uses port 22. To allow SSH connections into your virtual machine you will have to add a security rule to the *default* security group to allow it. To do this:
* Go to the *Network* panel by selecting it form the lefthand menu. Then click *Security Groups*, again from the left hand menu, and in the row for the *default* security group click the *Manage Rules* button on the right. <br/>
This will bring up a new panel showing all the rules for this security group.
* Click the *+ Add Rule* button in the top right which brings up a new panel.
* For the *Rule* drop down select *SSH* near the bottom of the list.
* For *Description* add a description of the machine we are allowing to connect (e.g. "Chris Geroux's laptop")
* For *Remote* select *CIDR*.<br/>

> ## CIDR
> [**CIDR**](../reference#cidr) stands for Classless Inter-Domain Routing and is a way of specifying ranges of IP address. There is a [convenient tool](http://www.ipaddressguide.com/cidr) for converting an IP range into CIDR notation.
{: .callout}

It is usually best to limit access to VMs to as small a set of IPs as is reasonable. From a previous episode we looked up our IP addresses at [ipv4.icanhazip.com](https://ipv4.icanhazip.com), use the IP address you get from this site to enter into the *CIDR* box followed by a `/32`. The `/32` we added to the end of your IP address indicates that all 32 bits of an IP address of a machine trying to access a VM in this security group should match the IP given. A single CIDR rule can allow multiple IP address to connect by adjusting the number of bits that must match, starting from the most significant or left most bit.

## Connecting to a virtual machine

Once your virtual machine's status as viewed on the *Instances* OpenStack dashboard panel is *Active* you can connect to your virtual machine using SSH. To do so run the following command

~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
in this command `ubuntu` is the username of the user you are connecting to the virtual machine as and `206.12.11.12` is the floating IP address of your newly created virtual machine.
~~~
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Oct 11 16:06:19 UTC 2022

  System load:  0.689453125       Processes:             94
  Usage of /:   7.1% of 19.20GB   Users logged in:       0
  Memory usage: 12%               IPv4 address for ens3: 192.168.0.207
  Swap usage:   0%

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@john-smith:~$
~~~
{: .output}

At the bottom of the output you can see the prompt `ubuntu@john-smith:~$` this is now a shell prompt on the newly created virtual machine. Notice that the username we used to connect `ubuntu` is part of the prompt letting you know who the virtual machine thinks you are. Also notice `john-smith` which is the hostname of your virtual machine, as mentioned earlier this derived from the Instance Name you give to your virtual machine. Finally the `~` indicates what directory you are currently in. In this case you are in the user `ubuntu`'s home directory.

From this point you can start working with or configuring your virtual machine with additional capability above and beyond those included in the basic Ubuntu operating system provided by the image we selected when creating our virtual machine. The things you can do with your new VM are only limited by your imagination, time, and OpenStack quota. Some examples of what you could do with your OpenStack VMS, run python scripts to scrape twitter data, run a wordpress site to publish articles, or do large scale text processing with Spark.

> ## Disconnecting
> To disconnect from a remote machine, or exit a shell, you can type the `exit` command.
{: .callout}


> ## What do you see in your VM's log
> The log of your virtual machine can be very helpful for understanding and debugging problems. On the *Instances* page then click on your *Instance name* and then the *Log* tab. The log shows various steps take and output generated while your VM is starting up and while running. Can you see where your public key is injected into the VM. Hint: it is put into a file called `authorized_keys`.
>
> > ## Solution
> > You should see something like the following:
> > ~~~
> > ci-info: ++++++++++Authorized keys from /home/ubuntu/.ssh/authorized_keys for user ubuntu++++++++++
> > ci-info: +---------+-------------------------------------------------+---------+------------------+
> > ci-info: | Keytype |                Fingerprint (md5)                | Options |     Comment      |
> > ci-info: +---------+-------------------------------------------------+---------+------------------+
> > ci-info: | ssh-rsa | 24:8d:e7:a6:b8:f5:02:b1:0f:89:92:85:85:eb:d5:59 |    -    | rsa-key-20160303 |
> > ci-info: +---------+-------------------------------------------------+---------+------------------+
> > ~~~
> > {: .output}
> > The comment associated with the public key is usually `<user>@<hostname>`. The Fingerprint can be used to uniquely identify the key pair and can be useful when trying to verify that a public key and a private key are part of the same pair.
> {: .solution}
{: .challenge}

> ## What does the Console tab do
> On the *Instances* page then click on your *Instance name* and then the *Console* tab. If it shows a blank or black box, try clicking on it and pressing the enter key.
> > ## Solution
> > It should show a `login:` prompt, prompting you to enter your username to login, but if you do it will ask you for a password but since we are authenticating using key pairs we don't have a password. For this reason console is not very useful for Linux VMs. If you were to create a Windows VM though the authentication process is much different and the console becomes slightly more useful.
> {: .solution}
{: .challenge}

> ## VM names to hostnames
>
> If you were to create two VMs with names of `_test` and `test!abs` what would the hostname for the VM be?
> > ## Solution
> > the VM name will be modified to remove invalid characters. So a VM name of `_test` will become a hostname of `test` and VM name of `test!abs` will become `testabs` hostname. When you log into a VM you see the hostname and not the VM name at the command prompt.
> {: .solution}
{: .challenge}
