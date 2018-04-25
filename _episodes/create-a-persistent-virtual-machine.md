---
layout: episode
title: "Creating a persistent virtual machine"
teaching: 15
exercises: 15
questions:
- "What makes a virtual machine persistent?"
- "What are the differences between ['p'](../reference#persistent-flavor) and ['c'](../reference#compute-flavor) flavors?"
- "What is CPU oversubscription?"
- "Why are 'p' flavors oversubscribed?"
objectives:
- "Understand difference between ephemeral and persistent storage"
- "To be able to create a persistent virtual machine"
keypoints:
- "`p` flavors or [**persistent flavors**](../reference#persistent-flavor) can have their [**VCPUs oversubscribed**](../reference#cpu-oversubscription) by up to 8 times."
- "A [**volume**](../refernece#volume) is a virtual hard drive allowing its contents to persist from one VM to the next."
- "`p` flavors should typically boot from a volume."
- "A `p` flavor not booting from a volume will have an unusably small root disk."
---

In general a persistent virtual machine is a long running virtual machine that maintains settings and files from one session to the next (they persist). While a non-persistent virtual machine implies that it is only created when you need it and settings and files from previous sessions are lost (they do not persist). In the case of the Compute Canada cloud this difference is reflected by the two main flavor types, the [**persistent flavors**](../reference#persistent-flavor) starting with a `p` and [**compute flavors**](../reference#compute-flavor) starting with a `c`. In the previous episode we discussed briefly the differences between `p` and `c` flavors, here we will dive deeper into these differences.

To better understand the difference between `p` and `c` flavors it is useful to discuss the details of how they behave differently. As mentioned earlier, `p` flavors are expected to be running services such as a website which need to perform actions upon request and may have significant time between requests. However, such a server must remain running regardless of whether it is performing a task or not as it never knows when a request might be made and must be ready to meet that request. This suggests that there is likely a significant period of time when the virtual machine is not performing any tasks and if it were to share a CPU with other virtual machines this would make more efficient use of the underlying hardware allowing more virtual machines to run on the same hardware. The Compute Canada cloud does allow [**CPU oversubscription**](../reference#cpu-oversubscription) up to 8 times for `p` flavors. This means that it is possible to share a single CPU with up to 8 virtual machines. For the most part this is probably fine as a persistent virtual machine running a website may very well spend most of the time doing nothing so that it is very unlikely that many of those 8 virtual machines will need to perform a task at the same time. If for some reason they do need to perform a task at the same time nothing terrible will happen, it will just mean that the response time to perform that task will be diminished. The benefits of being able to run 8 times as many websites greatly outweighs the small possibility of slowness upon occasion.

Another significant difference is that `p` flavors are expected to use a [**volume**](../reference#volume) as an *Instance Boot Source*. A volume plays much the same role as a hard drive in a physical computer in that you can attach a volume to virtual computer format it with a file system and store files on it. It can also exist beyond the life time of the virtual machine. You can terminate a virtual machine and retain volumes attached to it after the fact and then create a new VM which boots from the same volume. You can also specify the size of a volume which allows you to have much larger file systems for your operating system. In addition volumes are protected against hardware failure with 3x replication of data. Meaning that if a physical hard drive failes containing your volume data, two more would have to fail in short order for your data to be lost.

In the last episode we created a virtual machine which booted from an image and did not make use of a volume so where did this machine boot from? When booting from an image a virtual disk is created on the local drive of the physical computer running the virtual machine, also referred to as an [**ephemeral disk**](../reference#ephemeral-disk) as this virtual disk exists only as long as the virtual machine. When the virtual disk is created the data contained in the selected disk image was copied onto this virtual disk. The size of this virtual disk is fixed for `c` flavors at 20GB. In the case of `p` flavors, while you technically can also boot them from an image, the virtual disk that is created is only a tiny bit bigger than the original disk image. If you try to write much to the filesystem of a `p` flavor VM booted from an image you will quickly exceed the capacity of the file system. `p` flavors were designed to be booted from a volume.

## Creating a persistent VM

Now lets create a persistent VM which boots from a volume. Start by creating a VM in the same way as last time, again making sure to include your name in your VM's name but do not launch it yet. Select the flavor `p1-1.5gb` and select  for *Instance Boot Source* a source which is from a volume. Options which boot from a volume are:

* **Boot from volume:** this option will allow you to create a new VM booting from a pre-existing volume.
* **Boot from image (creates a new volume):** this option will allow you to create a new volume from a selected disk image and boot form it. You can also specify the size of the volume with this option.
* **Boot from volume snapshot (creates a new volume):** this option will allow you to create a new volume from an existing volume snapshot and boot from the newly created volume. We have not talked about volume snapshots yet, but they can be thought of as a disk image created from a volume.

In our case we do not have any existing volumes or volume snapshots, so this leaves only one option:
* Choose *Boot from image (creates a new volume)* for the *Instance Boot Source*. 
* Choose the `Ubuntu-16.04-Xenial-x64-2017-02` image as before.
* Set the *Device size* to 10GB.
* **DO NOT** check the *Delete on Terminate* box.<br/>This will cause the volume to be deleted if the VM is.
* Also select a *Key Pair* and *Security Groups* on the *Access & Security* tab.
* Then click the *Launch* button.

> ## Forgetting a key
> If you forget to select a key-pair OpenStack may choose one for you if you only have one key-pair. If you have more than one it might not select a key-pair for you. If you end up with a VM which didn't have a public key injected into it you will not be able to connect to the VM and you will have to delete and recreate it.
{: .callout}

## Associate a floating IP
Once we have created a persistent VM we will also need to associate a public IP with it as we did in the previous episode so that we can connect to it.

In the following episodes we will use this VM to setup a basic web server allowing us to server HTML files and tomorrow we will use it to create a WordPress site.

> ## Volume Name
> You just created a new persistent VM booting from a volume. What is the name of that volume?
> > ## Solution
> > Go to *Volumes* and find the volume attached the VM you just created. The name will be an ugly string of numbers and characters like `95f62a65-39b9-4c69-a319-2fcfaaa85f3a`. When a volume is created as part of VM creation, as was the case above, it names the volume after its unique ID. Every object, volume, VM, IP, router, etc. in OpenStack has a unique ID that can be used to reference it. This means you can have two volumes or VMs with the same name but are still distinct and can be distinguished with their IDs.
> {: .solution}
{: .challenge}

> ## Volume Device Label
> What is the device label that the volume is attached on? The key word here is **on**.
> > ## Solution
> > Go to *Volumes* and find the volume attached the VM you just created. Under then *Attached To* column in the row for your volume it will tell you which device label the volume will have within the VM. In the case of a boot volume this label is usually `/dev/vda`. If the volume was added as a second or third volume to store data this device label would be `/dev/vdb` or `/dev/vdc` respectively and so on as fourth and fifth volumes are added. This device label allows you to make a connection with the drives you see in your VM with the volumes in listed in the OpenStack dashboard.
> {: .solution}
{: .challenge}
