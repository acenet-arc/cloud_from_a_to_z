---
layout: episode
title: "Creating a virtual machine"
teaching: 15
exercises: 15
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
Now we will create your first virtual machine and connect to it using SSH. To do so go to the OpenStack dashboard and select from the left hand menu *Compute*->*Instances* and click *Launch Instance* button in the top right of the panel. 

You are presented with a panel consisting of multiple tabs of fields to fill in. There are many optional fields which can allow additional functionality, but for this first exposure will stick to the basics.

**Availability Zone:** In theory this could allow you to chose how available you would like your VM to be. This would be done by launching your VM on hosts in a different availability zone which have certain hardware or software configurations which make them less susceptible to outages. However, on the Compute Canada cloud there is only one availability zone so there is no need to choose anything but the default.

**Instance Name:** specify the name of your virtual machine. OpenStack will attempt to use this name as the hostname of your virtual machine. However, if the instance name you provided is not a valid hostname OpenStack will modify it so that it is valid and use the modified version for your hostname while still referring to your VM in the OpenStack dashboard by the instance name you provided. As some of use might be sharing a project, please include your name in the instance name, something like `your-name-first-vm`.

> ## What is a valid hostname?
> A good description of a valid hostname is given in this [wikipedia page section]( https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames). The official specifications for hostnames are given in two Internet standards requests for comments documents [RFC-952](https://tools.ietf.org/html/rfc952), and [RFC-1123](https://tools.ietf.org/html/rfc1123).
> The summary of the wikipeida page is, hostnames must be less than 64 characters long, contain only numbers letters and dashes (`-`).
{: .callout}

**Flavor**: The [**flavor**](../reference#flavor) of your VM specifies the hardware profile your VM will have. Compute Canada cloud uses a consistent naming scheme across their clouds to describe the hardware profile.  Examples of VM flavors are `p1-1.5gb` and `c1-7.5gb-30` and the different components of the name correspond to different hardware features.

* Flavors beginning with a `p` indicates a persistent VM. Persistent VMs are expected to run for long periods of time and provide services such as websites. We will explore persistent VMs in more detail in the next episode. 

* Flavors beginning with a `c` indicates a compute VM. Compute VMs are expected to run for shorter periods of time and be temporary. These VMs are expected to make heavy use of the CPU during their total existence with nearly 100% usage, unlike persistent VMs which may only do something ever once and a while when some one makes a request for the service they provide.

* The number after the 'p' or 'c' indicates the number of virtual central processing units (VCPUs)

* The number after then first '-' indicates the amount of RAM in GB for example the flavor `c1-7.5gb-30` has 7.5 GB of RAM

* The final number, which only occurs in flavors starting with a `c`, is the size in GB of an extra virtual disk in addition to the disk that the virtual machine's operating system resides. This extra disk can be used to store temporary data, but will be lost once the virtual machine is terminated unless special care has been taken to save it else where.

For this example choose the `c1-7.5gb-30` flavor. Which is a compute flavor with 1VCPU, 7.5GB of RAM and a 30 GB of extra temporary disk storage.

**Instance Count:**  indicates how many virtual machines you wish to create. For this example choose 1.

**Instance Boot Source**: indicates from where your virtual machine will [**boot**](../reference#boot) its operating system. There are several options to choose from, but for this example we will choose *Boot from image*. This choice indicates that we want to select an [**ephemeral disk**](../reference#ephemeral-disk) as our boot source. The combination of the flavor we chose above and the [**boot source**](../reference#boot-source) we chose instructs OpenStack to create a new virtual disk of 20 GB and copy the selected virtual disk image to it. This virtual disk will reside on the host machine's disk and contain the operating system files for the virtual machine. 

**Image Name:** specifies an [**image**](../reference#image) which forms the starting point for our virtual machine. Usually this means choosing an operating system for your virtual machine. But it could include additional software packages and configurations also. We will choose the `Unbuntu-16.04-Xenial-x64-2017-03` image which contains the Ubuntu Linux operating system, version 16.04.

**Key Pair:** The final piece of information we need to provide before creating a VM is the public key we created in the previous episode to allow you to connect to the VM you create. Select the *Access & Security* tab, then you can add a public key to your OpenStack account by clicking the "+"  next to the *Select a key pair* drop down box. Then copy and paste in your public key into the text field. You can copy your public key text by going to your terminal where you created your key pair in the last episode and running the command

~~~
$ cat .ssh/id_rsa.pub
~~~
{: .bash}
~~~
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxo6H/dDFLunQOUKnTUxNfHTsDfARFdFjqyJrf2udOBAzm7hg/w4SaHAqF1b1DvmGhwKwXW6lXYkdsiA5d4IK/Cg8GZ7l74J1QTQ+e6JkdvOmVlTGnu6PTesd++6jZUeiF9Im0ksGPTYo8QH/5k1eHUMwWpUh9xfX0Z56IdUyNxx+/QaeCc61sUvIPf+w2Vm/zC44C+v5OX4lDWlamLf2b0u6be5L99UXWN8741354auMP8qVMidRq8jQjUmlto30b/2H9bMFGQ63eEApEnhe6s+qdxVlbLkKHT2H905ydXf4knAY3TGlgylBNbXjeiJEp9mKlQ5LnIi6rayxzDrIv cgeroux@Caelia
~~~
{: .output}

and copying this text into the *Public Key* text field on the OpenStack dashboard. Provide a *Key Pair Name* which will distinguish this key from other keys you might have, something like `laptop-key` or `work-desktop-key`. Then click the *Import Key Pair* button to add that public key to your OpenStack account. This public key can then be selected from the drop down box *Select a key pair*. This public key can also be used for other future virtual machines also.

Before launching your first VM make sure to check the check box under *Security Groups* next to the *default* security group. This will add your VM to the *default* security group. A [**security group**](../reference#security-group) contains [**security rules**](../reference#security-rule) that allow traffic into and out of your virtual machine. By selecting the default security group we can set rules to allow access to your virtual machine.

Finally click the *Launch* button at the bottom of the *Launch Instance* panel to create your first virtual machine!

## Associating a Floating IP with a VM
To connect to your virtual machine you will need to associate a [**Public IP**](../reference#public-ip) with your virtual machine. Doing so will create a pointer from a publicly accessible IP to your virtual machine. This publicly accessible IP is also known as a [**Floating IP**](../reference#floating-ip) as this IP can "float" from one virtual machine to another. The public IP associated with your VM allows other machines to connect to your VM across the Internet. This is different from the private or local IP your VM gets by default, which only identifies the virtual machine on the local network. To associate a floating IP with your newly created virtual machine click on the drop down menu on the right side of your newly create virtual machine and select *Associate Floating IP*. This will bring up a panel to select an IP Address. Chances are you will not yet have a floating IP added to your project. To add a new floating IP click the *+* button next to the drop down box *Select an IP address*. Select a *Pool* to allocate the floating IP from. There will likely be only one. Then select *Allocate IP*. This will then take you back the previous panel and you can select the newly allocated floating IP from the drop down box. For *Port to be associated* your newly created VM should already be selected as indicated by the name of your VM and its private IP address. Then click *Associate*. The floating IP we just associated with your newly created VM will be the IP address we use to connect to your VM.

## Adding SSH Security Rule
To connect to the virtual machine we will be using SSH which communicates on port 22. To allow SSH connections into your virtual machine you will have to add a security rule to the *default* security group to allow it. To do this go to the *Access & Security* panel and click the *Manage Rules* button on the right in the row of the *default* security group. This will bring up a new panel showing all the rules for this security group. To allow traffic inbound on port 22 click the *+ Add Rule* button in the top right which brings up a new panel. For the *Rule* drop down select *SSH*. For *Remote* select *CIDR*. [**CIDR**](../reference#cidr) stands for Classless Inter-Domain Routing and is a way of specifying ranges of IP address. There is a [convenient tool](http://www.ipaddressguide.com/cidr) for converting an IP range into CIDR notation. It is usually best to limit the VM to as small a set of IPs as is reasonable. From a previous episode we looked up our IP address at [whatismyipaddress.com](https://whatismyipaddress.com/?u=TRUE), use this IP to enter into the CIDR tool to for both the lower and upper IPs in the range and enter the resulting CIDR rule into the *CIDR* text field and click *Add* to add the new rule.

## Connecting to a virtual machine

Once your virtual machine's status as viewed on the *Instances* OpenStack dashboard panel is *Active* you can connect to your virtual machine using SSH. To do so run the following command

~~~
$ ssh ubuntu@206.12.11.12
~~~
{: .bash}
in this command `ubuntu` is the username of the user you are connecting to the virtual machine as and `206.12.11.12` is the floating IP address of your newly created virtual machine.
~~~
Warning: Permanently added '206.12.11.12' (RSA) to the list of known hosts.
Enter passphrase for key '/home/mobaxterm/.ssh/id_rsa':
Welcome to Ubuntu 16.04.2 LTS (GNU/Linux 4.4.0-71-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

/usr/bin/xauth:  file /home/ubuntu/.Xauthority does not exist
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@test:~$
~~~
{: .output}

At the bottom of the output you can see the prompt `ubuntu@test:~$` this is now a shell prompt on the newly created virtual machine. Notice that the username we used to connect `ubuntu` is part of the prompt letting you know who the virtual machine thinks you are. Also notice `test` which is the hostname of your virtual machine, as mentioned earlier this derived from the Instance Name you give to your virtual machine. Finally the `~` indicates what directory you are currently in. In this case you are in the user `ubuntu`'s home directory.

From this point you can start working with or configuring your virtual machine with additional capability above and beyond those included in the basic Ubuntu operating system provided by the image we selected when creating our virtual machine. The things you can do with your new VM are only limited by your imagination, time, and OpenStack quota. Some examples of what you could do with your OpenStack VMS, run python scripts to scrape twitter data, run a wordpress site to publish articles, or do large scale text processing with Spark.

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

> ## Create a VM with an invalid hostname
>
> What does the hostname become if you create a VM with an instance name which isn't a valid hostname such as `_test` or `test!abs`?
> > ## Solution
> > the instance name will be modified such that it is a valid host name be removing the invalid characters. So `_test` will become `test` and `test!abs` will become `testabs`.
> {: .solution}
{: .challenge}
