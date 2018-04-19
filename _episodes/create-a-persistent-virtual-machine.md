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

Now lets create a persistent VM which boots from a volume. Start by creating a VM in the same way as last time, again making sure to include your name in your VM's name but do not launch it yet. Select the flavor `p1-1.5gb` and select  for *Instance Boot Source* a source which is from a volume. Options which boot from a volume are:

* **Boot from volume:** this option will allow you to create a new VM booting from a pre-existing volume.
* **Boot from image (creates a new volume):** this option will allow you to create a new volume from a selected disk image and boot form it. You can also specify the size of the volume with this option.
* **Boot from volume snapshot (creates a new volume):** this option will allow you to create a new volume from an existing volume snapshot and boot from the newly created volume. We have not talked about volume snapshots yet, but they can be thought of as a disk image created from a volume.

In our case we do not have any existing volumes or volume snapshots, so this leaves the *Boot from image (creates a new volume)* option so lets choose that *Instance Boot Source*. Lets choose the `Ubuntu-16.04-Xenial-x64-2017-02` image as before and a *Device size* of 10GB. **DO NOT** check the *Delete on Terminate* box as this will cause the volume to be deleted if the VM is. Also do not forget to switch to the *Access & Security* tab to select a *Key Pair* and *Security Groups* before clicking the *Launch* button because if a key pair is not selected you will not be able to connect to the VM and you will have to delete and recreate it.

Once we have created a persistent VM we will also need to associate a public IP with it so that we can connect and also verify that we can indeed connect to the VM by `ssh`ing into the VM.

In the following episodes we will use this VM to setup a basic web server allowing us to server HTML files and tomorrow we will use it to create a WordPress site.

> ## Boot a `p`-flavor VM from an Image
>
> If you create a `p`-flavor VM booting from an image how big is the root file system. **Hint**: run the command `df -h` to display the disk size and usage once connected to the VM. Be sure to terminate this VM as you can do little with it due to the small disk size.
{: .challenge}
