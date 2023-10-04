---
layout: page
title: Globus
permalink: /globus/
---

These instructions walk you through the process of setting up [Globus](https://www.globus.org/) on your cloud VM. Globus is a service for fast, reliable, secure data movement. See also [Compute Canada docs](https://docs.alliancecan.ca/wiki/Globus) for Globus.

**(Note that this assumes you have a running Ubuntu instance on the CC Cloud with a python installation. Make adjustments for an alternative OS or location.	You'll need to change the elements in << >> as well since these are variables. Remember to remove the the <<'s and >>'s when making these substitutions.)**

1. Log into globus.alliancecan.ca.
2. Select the "ENDPOINTS" panel from the left hand menu bar then click on the "Create a personal endpoint" at the top right of the screen.
3. Give your endpoint a name, and generate a setup key, and copy this to your clipboard and perhaps also save it to a text file incase you need to use your clipboard for other things before the key is needed.
4. Log in the VM using ssh:
	~~~
	$ ssh ubuntu@<<206.167.180.99>>
	~~~
	{: .bash}
5. On the VM download the globus connect personal tar file:
	~~~
	$ wget https://downloads.globus.org/globus-connect-personal/v3/linux/stable/globusconnectpersonal-latest.tgz
	~~~
	{: .bash}
6. Untar the file:
	~~~
	$ tar -xzvf globusconnectpersonal-latest.tgz
	~~~
	{: .bash}	
7. cd into the directory (the version number will likely be different):
	~~~
	$ cd globusconnectpersonal-2.2.1/
	~~~
	{: .bash}
8. Setup the Globus Connect Personal instance using the key from step 3:
	~~~
	$ ./globusconnectpersonal -setup <<2df1e93e-45f9-42a1-a321-591e4c0b941>>
	~~~
	{: .bash}
	If you see an error like `/usr/bin/env: ‘python’: No such file or directory` you will need to install python with something like `sudo apt install python`.
9. Start the Globus Connect Personal instance: 
	~~~
	$ ./globusconnectpersonal -start
	~~~
	{: .bash}
	If you want the instance to run in the background _and_ to be robust against hangups then use:
	
	~~~
	$ nohup ./globusconnectpersonal -start &
	~~~
	{: .bash}

# How to add a volume / directory outside the home directory.

What you have done so far will give you access to the home directory on the system and all the subfolders within it. If you would like to grant access to directories outside the scope of the home directory or remove access to directories within the scope of the home directory then you'll need to do some further configuration.	We'll break this down into two steps. The first is creating, attaching, and mounting a new volume. The second is configuring Globus to access that volume. We'll do step one in this section and step two in the next.

1. Go to the _Volumes_ tab within the OpenStack dashboard and create a volume with the settings that make sense for your research.	Typically this will be a "no image" volume with a total size in gigabytes just slightly larger than the amount of data you expect the volume to hold.
2. From the "more" button to the right of the newly created volume choose "Edit Attachments" and attach the volume to the appropriate instance that you are running.
3. Now that the drive is attached we will need to mount it but before we do that we'll need to format it.	 This process will take place within the instance/VM that the volume has been attached to so log in there now.
4. Run the partition editor with the list-flag enabled to see all the currently mounted partitions/drives:
	~~~
$ sudo parted -l
	~~~
	{: .bash}
	  
	~~~
	sudo: unable to resolve host globus-volume-test
	Model: Virtio Block Device (virtblk)
	Disk /dev/vda: 2147MB
	Sector size (logical/physical): 512B/512B
	Partition Table: msdos
	
	Number	Start		End			Size		Type		 File system	Flags
	 1			1049kB	2147MB	2146MB	primary	 ext4					boot
	
	
	Error: /dev/vdb: unrecognised disk label	
	~~~
	{: .output}
	
	Note that if you see something like "sudo: unable to resolve host globus-volume-test" you can just ignore this artifact of how the drive was created.	 If you want to fix it this can be done by following the instructions [HERE](http://askubuntu.com/questions/59458/error-message-when-i-run-sudo-unable-to-resolve-host-none) or searching the web for alternative explanations.
	
5. Note the error message produced in the previous command.	 Part of this message will tell you the name of the volume device that we have just created which we have not yet formatted.	In this case it is "/dev/vdb" ("vdb" stands for "volume device b").	 "unrecognized disk label" means that the system doesn't know what sort of format the drive has so we'll need to fix this.	Now that we know the name of the volume device we run `parted` again:
	
	~~~
$ sudo parted /dev/vdb
(parted) help
	~~~
	{: .bash}
	
6. The dollar sign `$` prompt will have been replaced by `(parted)` to show that we are in the `parted` tool.	 If you would like to know what options are available you can run:
7. What we would like to do is make a label for the device we specified in step #5 so we run:
	~~~
	(parted) mklabel gpt
	~~~
	{: .bash}
	
	"gpt" is the most common label type used by modern Linux machines so that's why we chose it.	 If you'd like to see all the label types available then just run `mklabel` without specifying a label type.
	
8. Now that we have a label we need to partition the device. We do this with:
	
	~~~
(parted) mkpart
	~~~
	{: .bash}
	
9. You will be asked for a partition name.	Might as well leave this blank:
	
	~~~
Partition name?	 []?
	~~~
	{: .bash}
	
10. You will be asked what file system type you'd like to use.	ext4 is new and robust and works well with ubuntu so we'll use it even though the default is ext2:
	
	~~~
File system type?	 [ext2]? ext4 
	~~~
	{: .bash}

11. You will be asked for where the file system should start and end.	 On the assumption that you want to use the entire device as a single drive we will have the file system take up the entire device:
	
	~~~
Start? 0%
End? 100%	 
	~~~
	{: .bash}
	
12. If you'd like to see the progress so far then you can run:
	
	~~~
	(parted) print
	~~~
	{: .bash}
	~~~
	Model: Virtio Block Device (virtblk)
	Disk /dev/vdb: 2147MB
	Sector size (logical/physical): 512B/512B
	Partition Table: gpt

	Number	Start		End			Size		File system	 Name	 Flags
	 1			1049kB	2146MB	2145MB
	~~~
	{: .output}
	
13. We're done with `parted` so we quit:
	
	~~~
	(parted) quit
	~~~
	{: .bash}
	~~~
	Information: You may need to update /etc/fstab.
	~~~
	{: .output}
	
14. The information given on quitting isn't entirely true, we really only need to update /etc/fstab, which is the file system table in this instance if we want this volume to _always_ be mounted whenever we reboot/restart the instance.	 We'll get to how to set this up. More important right now is to actually mount the volume. We'll do this by:
	
	~~~
	$ sudo mkfs.ext4 /dev/vdb1
	~~~
	{: .bash}
	~~~
	mke2fs 1.42.9 (4-Feb-2014)
	Filesystem label=
	OS type: Linux
	Block size=4096 (log=2)
	Fragment size=4096 (log=2)
	Stride=0 blocks, Stripe width=0 blocks
	131072 inodes, 523776 blocks
	26188 blocks (5.00%) reserved for the super user
	First data block=0
	Maximum filesystem blocks=536870912
	16 block groups
	32768 blocks per group, 32768 fragments per group
	8192 inodes per group
	Superblock backups stored on blocks: 
		32768, 98304, 163840, 229376, 294912

	Allocating group tables: done
	Writing inode tables: done
	Creating journal (8192 blocks): done
	Writing superblocks and filesystem accounting information: done 
	~~~
	{: .output}

15. Now that we are done with all the formatting we'll make a directory to mount the volume to.	 Here we'll create the directory in the `/mnt` directory and call it `vol2` but you can really put it anywhere you would like and call it anything you would like (as long as you appropriately account for this shift in the rest of these instructions):
	
	~~~
sudo mkdir /mnt/vol2
	~~~
	{: .bash}
	
16. Now we mount the volume to the directory:
	
	~~~
sudo mount /dev/vdb1 /mnt/vol2
	~~~
	{: .bash}
	
	`vbd1` is the name of the first partition on the volume vbd and we are making it the case that while this partition is mounted when we look in the directory /mnt/vol2 we will see all the contents of this partition. Give that we set the partition to take up the entire volume we'll see everything on it.
	
	So, anything we now do inside /mnt/vol2 will be done to the volume we originally created at the very beginning of this process. If we unmount or disassociate the volume from the instance then the data will be kept and ready for the next mount, just like a USB drive.
	
17. If we want to have the volume mounted automatically everytime we reboot/restart the instance (usually a really good idea) then we need to modify /etc/fstab (as indicated in step 13).	To do with we need to use a text editor to add a line to a file.	For simplicity we will use `nano` here:
	
	~~~
$ sudo nano /etc/fstab
	~~~
	{: .bash}
	
	This will open for us a program that will allow us to edit the content of the file system table.	Currently it likely looks like the following:
	
	~~~
LABEL=cloudimg-rootfs /         ext4  defaults   0 0
	~~~
	{: .output}

	Based on what we have done so far to this we will add a line to make the file look like the following:
	
	~~~
LABEL=cloudimg-rootfs /         ext4  defaults   0 0
/dev/vdb1             /mnt/vol2 ext4  defaults   0 0
	~~~
	{: .output}
	
	Do not worry about having each piece of the line align with the line above, all that matters is that there is white space between each component.
	
	When this is done hold the control key and press x to begin the exit procedure.	 Because the file has been changed you will be asked if you want to save it.	Choose y for "Yes".	 When asked what file name to use just press enter and accept the default, which will be the name of the original file, overwriting it.
	
18. It is a good idea to test the change to /etc/fstab, we'll do this by unmounting our new volume and then telling the system to mount everything in /etc/fstab.	 If we've done everything correctly there will be no errors, as follows:
	
	~~~
	$ sudo umount /mnt/vol2
	$ sudo mount -a
	$ sudo df -h
	~~~
	{: .bash}
	~~~
	Filesystem   Size   Used  Avail Use%  Mounted on
	/dev/vda1    2.0G   844M   1.1G  46%  /
	none         4.0K      0   4.0K   0%  /sys/fs/cgroup
	udev         745M    12K   745M   1%  /dev
	tmpf         150M   340K   150M   1%  /run
	none         5.0M      0   5.0M   0%  /run/lock
	none         750M      0   750M   0%  /run/shm
	none         100M      0   100M   0%  /run/user
	/dev/vdb1    2.0G   3.0M   1.9G   1%  /mnt/vol2
	~~~
	{: .output}
	
	The last line of output from the `df` command shows that our newly partitioned file system, /dev/vdb1, has been remounted to the directory /mnt/vol2.
	
# Configuring Accessible Directories
If you have been following along from the beginning and everything has worked you now have globus personal running on your instance and an external volume attached.	We'll use this volume as an example for showing you how to set Globus to access directories outside of those that are subdirectories of your home directory.	If you have not created this volume you can just use any directory outside the home directory that you have system-level access permissions to.

How to do this is [detailed on the Globus website](https://docs.globus.org/faq/globus-connect-endpoints/#how_do_i_configure_accessible_directories_on_globus_connect_personal_for_linux) but we'll run through an example here just the same.

Note that if you have a volume ready to go, you don't want to play around with configuration files, and you know how to mount volumes already then you can cheat a little by simply mounting the volume within the home directory.

The last thing to note before we get into the details of this is that you cannot access a directory with Globus that you do not normally have access to.	When using Globus to access system whatever is more restrictive, the Unix permissions or the Globus permissions, will take precedence.

So, let's pick up from the end of the last section, where we now have a new volume mounted at /mnt/vol2 and we'd like to have Globus access that directory.

1. Access permissions in Globus are stored as a hidden text file inside the users home directory.	 We need to edit that file to change the permissions. We'll use `nano` to add a line to give permission to Globus to access /mnt/vol2:

	~~~
$ nano ~/.globusonline/lta/config-paths
	~~~
	{: .bash}

2.	When nano opens the file it should look like the following:
	
	~~~
~/,0,1
	~~~
	{: .output}
	
	We see now that the file is a line by line list of the directories that Globus has access to and the permissions associated with each.	The current line gives access to the home directory (~/) and by default all its subfolders.	 The permissions on this access are that the folder is _not_ shareable, as indicated by the first value, which is a zero, but that it _is_ writable, as indicated by the second value, which is a one.
	
	To add our new volume as a readable and writable directory via Globus we modify the file to read as follows:
	
	~~~
~/,0,1
/mnt/vol2,0,1
	~~~
	{: .output}
	
	If we wanted to share the volume via Globus we'd write:
	
	~~~
~/,0,1
/mnt/vol2,1,1
	~~~
	{: .output}
	
	Similarly, if we wanted to share the directory but keep it read only we'd have written:
	
	~~~
~/,0,1
/mnt/vol2,1,0
	~~~
	{: .output}
	
	When this is done hold the control key and press x to begin the exit procedure.	 Because the file has been changed you will be asked if you want to save it.	Choose y for "Yes".	 When asked what file name to use just press enter and accept the default, which will be the name of the original file, overwriting it.
