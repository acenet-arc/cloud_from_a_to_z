---
layout: episode
title: "Create a first virtual machine"
teaching: 15
exercises: 15
questions:
- "A question"
objectives:
- "Create a VM which you can log into"
keypoints:
- "a key point"
---

## Creating a first virtual machine
Now we will create your first virtual machine and connect to it using SSH. To do so go to the OpenStack dashboard and select from the left hand menu *Compute*->*Instances* and click *Launch Instance* button in the top right of the panel. 

You are presented with a panel consisting of multiple tabs of fields to fill in. There are many optional fields which can allow additional functionality, but for this first exposure will stick to the basics.

First up is the **Availability Zone**. In theory this could allow you to chose how available you would like your VM to be. This would be done by launching your VM on hosts in a different availability zone which have certain hardware or software configurations which make them less susceptible to outages. However, on the Compute Canada cloud there is only one availability zone so there is no need to choose anything but the default.

Next is **Instance Name** where you specify the name of your virtual machine. OpenStack will attempt to use this name as the hostname of your virtual machine. However, if the instance name you provided is not a valid hostname OpenStack will modify it so that it is valid and use the modified version for your hostname while still referring to your VM in the OpenStack dashboard by the instance name you provided.

> ## What is a valid hostname?
> A good description of a valid hostname is given in this [wikipedia page section]( https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames). The official specifications for hostnames are given in two Internet standards requests for comments documents [RFC-952](https://tools.ietf.org/html/rfc952), and [RFC-1123](https://tools.ietf.org/html/rfc1123).
>
{: .callout}

Next you choose the **Flavor** or your VM. The flavor of your VM specifies the hardware profile your VM will have. Compute Canada cloud uses a consistent naming scheme across their clouds to describe the hardware profile.  Examples of VM flavors are `p1-0.75gb` and `c1-3.75gb-36` and the different components of the name correspond to different hardware features.

* Flavors beginning with a **p** indicates a persistent VM. Persistent VMs are expected to run for long periods of time and provide services such as websites. We will explore persistent VMs in more detail in the next episode.

* Flavors beginning with a **c** indicates a compute VM. Compute VMs are expected to run for shorter periods of time and be temporary. These VMs are expected to make heavy use of the CPU during their total existence with nearly 100% usage, unlike persistent VMs which may only do something ever once and a while when some one makes a request for the service they provide.

* The number after the 'p' or 'c' indicates the number of virtual central processing units (VCPUs)

* The number after then first '-' indicates the amount of RAM in GB for example the flavor `c1-3.75gb-36` has 3.75 GB of RAM

* The final number, which only occurs in flavors starting with a `c`, is the size in GB of an extra virtual disk in addition to the disk that the virtual machine's operating system resides. This extra disk can be used to store temporary data, but will be lost once the virtual machine is terminated unless special care has been taken to save it else where.

For this example choose the `c1-3.75gb-36` flavor. Which is a compute flavor with 1VCPU, 3.75GB of RAM and a 36 GB of extra temporary disk storage.

Then we have **Instance Count** which simply indicates how many virtual machines you wish to create. For this example choose 1.

Next is **Instance Boot Source** which indicates from where your virtual machine will boot its operating system. There are several options to choose from, but for this example we will choose *Boot from image*. This choice indicates that we want to select a virtual disk image as our boot source. The combination of the flavor we chose above and the boot source we chose instructs OpenStack to create a new virtual disk of 20GB and copy the selected virtual disk image to it. This virtual disk will reside on the host machine's disk and contain the operating system files for the virtual machine. 

Next we need to choose an **Image Name** which will form the starting point for our virtual machine. Usually this means choosing an operating system for your virtual machine. For this example we will choose the `Unbuntu-16.04-Xenial-x64-2017-03` image. This an image containing the Ubuntu Linux operating system, version 16.04.

The final piece of information we need to provide before creating a VM is the public key we created in the previous episode to allow you to connect to the VM you create. To do this select the *Access & Security* tab. Then since you can add a public key to your OpenStack account by clicking the "+"  next to the *Select a key pair* drop down box. Then copy and paste in your public key. You can view your public key by going to your terminal where you created your key pair in the last episode and running the command

~~~
$ cat .ssh/id_rsa.pub
~~~
{: .bash}
~~~
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxo6H/dDFLunQOUKnTUxNfHTsDfARFdFjqyJrf2udOBAzm7hg/w4SaHAqF1b1DvmGhwKwXW6lXYkdsiA5d4IK/Cg8GZ7l74J1QTQ+e6JkdvOmVlTGnu6PTesd++6jZUeiF9Im0ksGPTYo8QH/5k1eHUMwWpUh9xfX0Z56IdUyNxx+/QaeCc61sUvIPf+w2Vm/zC44C+v5OX4lDWlamLf2b0u6be5L99UXWN8741354auMP8qVMidRq8jQjUmlto30b/2H9bMFGQ63eEApEnhe6s+qdxVlbLkKHT2H905ydXf4knAY3TGlgylBNbXjeiJEp9mKlQ5LnIi6rayxzDrIv cgeroux@Caelia
~~~
{: .output}

and copying this text into the *Public Key* text field on the OpenStack dashboard. Provide a *Key Pair Name* which will distinguish this key from other keys you might have, something like `laptop-key` or `work-desktop-key`. Then click the *Import Key Pair* button to add that public key to your OpenStack account. This public key can then be selected from the drop down box *Select a key pair*. This public key can also be used for other future virtual machines also.

Before launching your first VM make sure to check the radio box under *Security Groups* next to the *default* security group. This will add your VM to the default **security group**. A security group contains rules that allow traffic into and out of your virtual machine. By selecting the default security group we can set rules to allow access to your virtual machine.

Finally click the *Launch* button at the bottom of the *Launch Instance* panel to create your first virtual machine!

## Connecting to a virtual machine



> ## Create a VM with an invalid hostname
>
> What does the hostname become if you create a VM with an instance name which isn't a valid hostname such as `_test` or `test!abs`?
{: .challenge}

---
OUTLINE

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
