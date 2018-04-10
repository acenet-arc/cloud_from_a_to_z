---
layout: episode
title: "Using the OpenStack CL client"
teaching: 45
exercises: 15
questions:
- "How do we see what OpenStack CL commands are available?"
- "How can we find out how to use OpenStack CL commands?"
- "How do we backup our persistent virtual machine?"
- "How do we download/upload images to the cloud?"
objectives:
- "Delete a virtual machine but keep the volume to allow us to make an image of the volume."
- "Create an image of that volume."
- "Create a new virtual machine booting from the volume."
- "Add a floating IP to the new virtual machine."
- "Download the image for safe keeping."
- "Delete the image on the Compute Canada cloud."
- "Upload the image from safe keeping."
keypoints:
- "`openstack help` shows the list of available commands."
- "`openstack help <command-group>` shows the list of sub commands matching `<command-group>`."
- "`openstack help <command-group> <command>` shows the help text for `<command>`."
- "It is important to keep track of the volume disk type."
---

In the last episode we setup the OpenStack CL clients and even ran a command which listed our VMs. Now we are going to dive deeper into the OpenStack CL clients starting with creating an image of our persistent VM's volume and saving it locally where we are running the commands.

When creating an image of a volume, it is best to detach it from the VM first. This ensures that no writing to the volume will occur while we are creating an image. If writing occurs while creating an image the image might be corrupted and not work correctly. If a VM boots from the volume it is not possible to simply detach the volume, instead the VM must be deleted. Deleting a VM which boots from a volume will not cause any data loss, so long as the *Delete on Terminate* option was not selected when the VM was created. We can then easily create a new VM booting from this volume to get back to where we were.

We have already seen how to list VMs but we also want to see a list of volumes so we can identify which volume to create an image of. To see a list of available OpenStack commands use the `help` command.
~~~
$ openstack help
~~~
{: .bash}
~~~
...

 volume create  Create new volume
 volume delete  Delete volume(s)
 volume list    List volumes

...
~~~
{: .output}

There is a `list` command for volumes as was the case for servers.
~~~
$ openstack volume list
~~~
{: .bash}
~~~
+--------------------------------------+----------------+-----------+------+--------------------------------------------------+
| ID                                   | Display Name   | Status    | Size | Attached to                                      |
+--------------------------------------+----------------+-----------+------+--------------------------------------------------+
| 4adf2c1c-5415-4d97-987c-f71251b673f9 |                | in-use    |   10 | Attached to chris-geroux-persistent on /dev/vda  |
+--------------------------------------+----------------+-----------+------+--------------------------------------------------+
~~~
{: .output}

We can see that the volume with `ID` `4adf2c1c-5415-4d97-987c-f71251b673f9` is connected to the VM we are interested in creating an image of. Also the volume is attached at the path`/dev/vda` within the VM. Typically volumes are labelled starting at `a` as in `vda` if a second volume was attached it would be labelled `vdb` and be attached at `/dev/vdb` and so on. Typically root volumes will be attached at `/dev/vda`. In this case the volume doesn't have a name only an `ID` but this is OK as most OpenStack CL client commands accept `ID`s in place of names. In fact it can be a bit safer to use the `ID` to identify an OpenStack resource, as more than one resource can have the same name, but they will not have the same `ID`. 

Now we need to figure out how to delete a VM. To see a list of other things we can do with servers type
~~~
$ openstack help server
~~~
{: .bash}
~~~
Command "server" matches:
  server add security group
  server add volume
  server create
  server delete
  server dump create
  server image create
  server list
  server lock
  server migrate
  server pause
  server reboot
  server rebuild
  server remove security group
  server remove volume
  server rescue
  server resize
  server resume
  server set
  server shelve
  server show
  server ssh
  server start
  server stop
  server suspend
  server unlock
  server unpause
  server unrescue
  server unset
  server unshelve
~~~
{: .output}
The `delete` should do what we want, but lets make sure we use it properly by first consulting the help for the command.
~~~
$ openstack help server delete
~~~
{: .bash}
~~~
usage: openstack server delete [-h] [--wait] <server> [<server> ...]

Delete server(s)

positional arguments:
  <server>    Server(s) to delete (name or ID)

optional arguments:
  -h, --help  show this help message and exit
  --wait      Wait for delete to complete

~~~
{: .output}
Lets also include the `--wait` option so we will know when the delete has completed by getting the prompt back.
~~~
$ openstack server delete --wait chris-geroux-persistent
~~~
{: .bash}

We can verify that the VM was deleted with the `list` command again.
~~~
$ openstack server list
~~~
{: .bash}
~~~
+--------------------------------------+-------------------------+---------+---------------------------------------------------------+
| ID                                   | Name                    | Status  | Networks                                                |
+--------------------------------------+-------------------------+---------+---------------------------------------------------------+
| 1f9560a3-b5c5-46d1-a28a-5aa2eee4edce | chris-geroux-test-oscli | ACTIVE  | cgeroux-project_network=192.168.173.63, 206.167.183.128 |
+--------------------------------------+-------------------------+---------+---------------------------------------------------------+
~~~
{: .output}
As you can see the VM is now gone. 

To create an image from a volume we use the `image create` command. Lets have a look at the help for that command
~~~
$ openstack help image create
~~~
{: .bash}
~~~
usage: openstack image create [-h] [-f {json,shell,table,value,yaml}]
                              [-c COLUMN] [--noindent] [--prefix PREFIX]
                              [--max-width <integer>] [--id <id>]
                              [--container-format <container-format>]
                              [--disk-format <disk-format>]
                              [--min-disk <disk-gb>] [--min-ram <ram-mb>]
                              [--file <file>] [--volume <volume>] [--force]
                              [--protected | --unprotected]
                              [--public | --private] [--property <key=value>]
                              [--tag <tag>] [--project <project>]
                              [--project-domain <project-domain>]
                              <image-name>

Create/upload an image

positional arguments:
  <image-name>          New image name

optional arguments:
  -h, --help            show this help message and exit
  --id <id>             Image ID to reserve
  --container-format <container-format>
                        Image container format (default: bare)
  --disk-format <disk-format>
                        Image disk format (default: raw)
  --min-disk <disk-gb>  Minimum disk size needed to boot image, in gigabytes
  --min-ram <ram-mb>    Minimum RAM size needed to boot image, in megabytes
  --file <file>         Upload image from local file
  --volume <volume>     Create image from a volume
  --force               Force image creation if volume is in use (only
                        meaningful with --volume)
  --protected           Prevent image from being deleted
  --unprotected         Allow image to be deleted (default)
  --public              Image is accessible to the public
  --private             Image is inaccessible to the public (default)
  --property <key=value>
                        Set a property on this image (repeat option to set
                        multiple properties)
  --tag <tag>           Set a tag on this image (repeat option to set multiple
                        tags)
  --project <project>   Set an alternate project on this image (name or ID)
  --project-domain <project-domain>
                        Domain the project belongs to (name or ID). This can
                        be used in case collisions between project names
                        exist.

output formatters:
  output formatter options

  -f {json,shell,table,value,yaml}, --format {json,shell,table,value,yaml}
                        the output format, defaults to table
  -c COLUMN, --column COLUMN
                        specify the column(s) to include, can be repeated

json formatter:
  --noindent            whether to disable indenting the JSON

shell formatter:
  a format a UNIX shell can parse (variable="value")

  --prefix PREFIX       add a prefix to all variable names

table formatter:
  --max-width <integer>
                        Maximum display width, 0 to disable
~~~
{: .output}
From looking at the help message you can see that the `--volume` option will create an image from a volume. Another important option to consider is `--disk-format` which specifies the disk format. The default `raw` format will copy the entire volume, so it can take up a lot of space. A more space efficient format is `qcow` and only copies the part of the volume which has data on it (for more about image formats see [OpenStack image formats](https://docs.openstack.org/developer/glance/formats.html)).
~~~
$ openstack image create --volume 4adf2c1c-5415-4d97-987c-f71251b673f9 --disk-format qcow2 chris-geroux-persistent-root
~~~
{: .bash}
~~~
'NoneType' object is not subscriptable
~~~
{: .output}
> ## Understanding CL tool errors
> The OpenStack command line tools are still relatively new and have recently as last year experienced a large redesign. As such, they aren't as polished as might be liked. If you come accross errors like `'NoneType' object is not subscriptable` as above it is possible to get more information by rerunning commands with the "--debug" option which shows extra information. If we do this for the above command we get a large amount of extra output the last few lines look like:
> ~~~
> ...
>
> Traceback (most recent call last):
>   File "/usr/lib/python3/dist-packages/openstackclient/shell.py", line 118, in run
>     ret_val = super(OpenStackShell, self).run(argv)
>   File "/usr/lib/python3/dist-packages/cliff/app.py", line 255, in run
>     result = self.run_subcommand(remainder)
>   File "/usr/lib/python3/dist-packages/openstackclient/shell.py", line 153, in run_subcommand
>     ret_value = super(OpenStackShell, self).run_subcommand(argv)
>   File "/usr/lib/python3/dist-packages/cliff/app.py", line 374, in run_subcommand
>     result = cmd.run(parsed_args)
>   File "/usr/lib/python3/dist-packages/openstackclient/common/command.py", line 38, in run
>     return super(Command, self).run(parsed_args)
>   File "/usr/lib/python3/dist-packages/cliff/display.py", line 92, in run
>     column_names, data = self.take_action(parsed_args)
>   File "/usr/lib/python3/dist-packages/openstackclient/image/v2/image.py", line 328, in take_action
>     info['volume_type'] = info['volume_type']['name']
> TypeError: 'NoneType' object is not subscriptable
> 
> END return value: 1
> ~~~
> {: .output}
> This is a python stack trace coming from the OpenStack client. This stack trace tells us that the error originates from a line of code `info['volume_type'] = info['volume_type']['name']` in the file `/usr/lib/python3/dist-packages/openstackclient/image/v2/image.py` on line `328`. If we look at the OpenStack dashboard *volumes* tab we see that there is a column for *Type* next to each volume. Unless a *type* was selected when creating the volume this field will have a *-* in it to indicate no type specified. This is the cause of this error message. If you instead create a volume with a type this error will go away. However, other than getting this message and missing the output of summary information of the image just created there appear to be no other effects of this error.
{: .callout}

At this point we have now created an image of our persistent VM's root volume and are free to rebuild our VM so it is available again. For this we can use the `server create` command; lets have a look at its help text.
~~~
$ openstack help server create
~~~
{: .bash}
~~~
usage: openstack server create [-h] [-f {json,shell,table,value,yaml}]
                               [-c COLUMN] [--noindent] [--prefix PREFIX]
                               [--max-width <integer>]
                               (--image <image> | --volume <volume>) --flavor
                               <flavor>
                               [--security-group <security-group-name>]
                               [--key-name <key-name>]
                               [--property <key=value>]
                               [--file <dest-filename=source-filename>]
                               [--user-data <user-data>]
                               [--availability-zone <zone-name>]
                               [--block-device-mapping <dev-name=mapping>]
                               [--nic <net-id=net-uuid,v4-fixed-ip=ip-addr,v6-fixed-ip=ip-addr,port-id=port-uuid>]
                               [--hint <key=value>]
                               [--config-drive <config-drive-volume>|True]
                               [--min <count>] [--max <count>] [--wait]
                               <server-name>

Create a new server

positional arguments:
  <server-name>         New server name

optional arguments:
  -h, --help            show this help message and exit
  --image <image>       Create server from this image (name or ID)
  --volume <volume>     Create server from this volume (name or ID)
  --flavor <flavor>     Create server with this flavor (name or ID)
  --security-group <security-group-name>
                        Security group to assign to this server (name or ID)
                        (repeat for multiple groups)
  --key-name <key-name>
                        Keypair to inject into this server (optional
                        extension)
  --property <key=value>
                        Set a property on this server (repeat for multiple
                        values)
  --file <dest-filename=source-filename>
                        File to inject into image before boot (repeat for
                        multiple files)
  --user-data <user-data>
                        User data file to serve from the metadata server
  --availability-zone <zone-name>
                        Select an availability zone for the server
  --block-device-mapping <dev-name=mapping>
                        Map block devices; map is
                        <id>:<type>:<size(GB)>:<delete_on_terminate> (optional
                        extension)
  --nic <net-id=net-uuid,v4-fixed-ip=ip-addr,v6-fixed-ip=ip-addr,port-id=port-uuid>
                        Create a NIC on the server. Specify option multiple
                        times to create multiple NICs. Either net-id or port-
                        id must be provided, but not both. net-id: attach NIC
                        to network with this UUID, port-id: attach NIC to port
                        with this UUID, v4-fixed-ip: IPv4 fixed address for
                        NIC (optional), v6-fixed-ip: IPv6 fixed address for
                        NIC (optional).
  --hint <key=value>    Hints for the scheduler (optional extension)
  --config-drive <config-drive-volume>|True
                        Use specified volume as the config drive, or 'True' to
                        use an ephemeral drive
  --min <count>         Minimum number of servers to launch (default=1)
  --max <count>         Maximum number of servers to launch (default=1)
  --wait                Wait for build to complete

output formatters:
  output formatter options

  -f {json,shell,table,value,yaml}, --format {json,shell,table,value,yaml}
                        the output format, defaults to table
  -c COLUMN, --column COLUMN
                        specify the column(s) to include, can be repeated

json formatter:
  --noindent            whether to disable indenting the JSON

shell formatter:
  a format a UNIX shell can parse (variable="value")

  --prefix PREFIX       add a prefix to all variable names

table formatter:
  --max-width <integer>
                        Maximum display width, 0 to disable
~~~
{: .output}

We see that the `--volume` option allows us to specify a volume to create the VM from but we will also need to specify the flavor for the VM with the `--flavor` option. Previously we used the `p1-1.5gb` flavor so lets just use that again and finally we need to specify a name lets just use the same name as before `chris-geroux-persistent`.
~~~
$ openstack server create --volume 4adf2c1c-5415-4d97-987c-f71251b673f9 --flavor p1-1.5gb chris-geroux-persistent
~~~
{: .bash}
~~~
+--------------------------------------+------------------------------------------------------------------+
| Field                                | Value                                                            |
+--------------------------------------+------------------------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                                           |
| OS-EXT-AZ:availability_zone          | nova                                                             |
| OS-EXT-STS:power_state               | 0                                                                |
| OS-EXT-STS:task_state                | scheduling                                                       |
| OS-EXT-STS:vm_state                  | building                                                         |
| OS-SRV-USG:launched_at               | None                                                             |
| OS-SRV-USG:terminated_at             | None                                                             |
| accessIPv4                           |                                                                  |
| accessIPv6                           |                                                                  |
| addresses                            |                                                                  |
| config_drive                         |                                                                  |
| created                              | 2017-05-03T20:37:09Z                                             |
| flavor                               | p1-1.5gb (00e3a213-8be7-427b-b115-32927cfb58b3)                  |
| hostId                               |                                                                  |
| id                                   | e638cc49-5bde-4f52-957d-470577d32352                             |
| image                                |                                                                  |
| key_name                             | None                                                             |
| name                                 | chris-geroux-persistent                                          |
| os-extended-volumes:volumes_attached | [{'id': '4adf2c1c-5415-4d97-987c-f71251b673f9'}]                 |
| progress                             | 0                                                                |
| project_id                           | 13dd64422fd74ec5b4065f885e3b297d                                 |
| properties                           |                                                                  |
| security_groups                      | [{'name': 'default'}]                                            |
| status                               | BUILD                                                            |
| updated                              | 2017-05-03T20:37:09Z                                             |
| user_id                              | d592c3020aa22591c0e6c8567915d1e367491ad82e5f730492673b0a3f1eb955 |
+--------------------------------------+------------------------------------------------------------------+
~~~
{: .output}
Now we have create a new VM booting from our original volume. To connect to that VM we must add a floating IP. First lets see what IPs we have available.
~~~
$ openstack ip floating list
~~~
{: .bash}
~~~
+--------------------------------------+---------------------+------------------+--------------------------------------+
| ID                                   | Floating IP Address | Fixed IP Address | Port                                 |
+--------------------------------------+---------------------+------------------+--------------------------------------+
| 8f74bd50-04d7-4f78-bd5d-1f44fa75caae | 206.167.181.126     | None             | None                                 |
| a9645122-4000-464a-92e4-b6139f587574 | 206.167.181.127     | 192.168.173.26   | 2eecaf66-7f8d-4967-bf89-45c9590703fd |
+--------------------------------------+---------------------+------------------+--------------------------------------+
~~~
{: .output}
We can see that we have two floating IPs, one which is associated to the VM we are working now now `206.167.181.127` and one which was previously associated to the deleted VM which is now not associated to any VM `206.167.181.126`. Lets associate this with our newly created VM.
~~~
$ openstack help ip floating add
~~~
{: .bash}
~~~
usage: openstack ip floating add [-h] <ip-address> <server>

Add floating IP address to server

positional arguments:
  <ip-address>  IP address to add to server (name only)
  <server>      Server to receive the IP address (name or ID)

optional arguments:
  -h, --help    show this help message and exit
~~~
{: .output}
This command takes two arguments, the IP address to add and the server to add it to.
~~~
$ openstack ip floating add 206.167.181.126 chris-geroux-persistent
~~~
{: .bash}
At this point we should have our server back as it was before we started this episode, but in addition we have created an image of the servers root volume. This means we can save it away for safe keeping in case something bad happens to our server (we accidentally delete it etc.). We could also use this image as a starting point to create another server containing all the setup we have done previously. Lets download the VM image for safe keeping. We can do that with the `image save` command, lets take a look at the help for it.
~~~
$ openstack help image save
~~~
{: .bash}
~~~
Save an image locally

positional arguments:
  <image>            Image to save (name or ID)

optional arguments:
  -h, --help         show this help message and exit
  --file <filename>  Downloaded image save filename (default: stdout)
~~~
{: .output}
It takes an image name or ID as an argument. There is also a `--file` option which has the default of `stdout` this means it will print the contents of the image to your terminal screen, it would be much more useful to save it to a file so we will want to use this option to specify a filename. We should also add the image type to the filename. This is not strictly required, but it will help our future selfs and anyone else who might use the image to easily recognize the image format. Knowing the format of an image is important, for example when you want to upload an image to the cloud. If you do not specify the image type it will assume the `raw` format. In this case that would be incorrect and there will be problems when you try to use this image.
~~~
$ openstack image save --file chris-geroux-persistent-june-6-2017.qcow2 chris-geroux-persistent-root
~~~
{: .bash}
This command may take some time to complete depending on the size of the image. Finally lets verify that the image file is there and has the size we expect. We will use the `l` option to give us details about the file, such as its size and the `h` option which displays file sizes in a human readable format.
~~~
$ ls -lh
~~~
{: .bash}
~~~
-rw-rw-r-- 1 ubuntu ubuntu 1015M May  4 16:23 chris-geroux-persistent-june-6-2017.qcow2
-rw-rw-r-- 1 ubuntu ubuntu  1.6K May  2 17:40 openstackrc.sh
~~~
{: .output}
There is a new file there with a size that nearly matches the size listed in the openstack dashboard (1014.1 MB). This difference in size is likely due to different formating for displaying the sizes and it seems likely that the entire image was downloaded correctly. For a more rigorous way to verify this consider looking into  [checksums](https://en.wikipedia.org/wiki/Checksum) specifically [md5 checksums](https://help.ubuntu.com/community/HowToMD5SUM) which is what OpenStack shows. 

Lets now delete the image in OpenStack so that we can upload our "backup" image but first lets list all the images.
~~~
$ openstack image list
~~~
{: .bash}
~~~
+--------------------------------------+----------------------------------------------------------+--------+
| ID                                   | Name                                                     | Status |
+--------------------------------------+----------------------------------------------------------+--------+
| 29a170f3-cbee-4e03-9f6b-8e0c756cb85c | chris-geroux-persistent-root                             | active |
| 4ee8b481-248d-4f1c-8d55-35265f72414d | Ubuntu-16.04-Xenial-x64-2017-03                          | active |
| 48b33525-8238-4027-abca-a71b24f5684a | Ubuntu-14.04.5-Trusty-x64-2017-03                        | active |
| 1c90c7d4-bd99-4596-96fd-d89270849d95 | Fedora-25-1.3-x64-2017-03                                | active |

...

+--------------------------------------+----------------------------------------------------------+--------+
~~~
{: .output}
Then delete the `chris-geroux-persistent-root` image and list the images again to verify that it was deleted.
~~~
$ openstack image delete chris-geroux-persistent-root
$ openstack image list
~~~
{: .bash}
~~~
+--------------------------------------+----------------------------------------------------------+--------+
| ID                                   | Name                                                     | Status |
+--------------------------------------+----------------------------------------------------------+--------+
| 4ee8b481-248d-4f1c-8d55-35265f72414d | Ubuntu-16.04-Xenial-x64-2017-03                          | active |
| 48b33525-8238-4027-abca-a71b24f5684a | Ubuntu-14.04.5-Trusty-x64-2017-03                        | active |
| 1c90c7d4-bd99-4596-96fd-d89270849d95 | Fedora-25-1.3-x64-2017-03                                | active |

...

+--------------------------------------+----------------------------------------------------------+--------+
~~~
{: .output}

Now lets upload our "backup" image. Lets have a look at the help for `image create` to see how to use the command in this case. We used it previously to create an image from a volume, now we want to use it to create an image from a file.
~~~
$ openstack help image create
~~~
{: .bash}
~~~
usage: openstack image create [-h] [-f {json,shell,table,value,yaml}]
                              [-c COLUMN] [--noindent] [--max-width <integer>]
                              [--prefix PREFIX] [--id <id>]
                              [--container-format <container-format>]
                              [--disk-format <disk-format>]
                              [--min-disk <disk-gb>] [--min-ram <ram-mb>]
                              [--file <file>] [--volume <volume>] [--force]
                              [--protected | --unprotected]
                              [--public | --private] [--property <key=value>]
                              [--tag <tag>] [--project <project>]
                              [--project-domain <project-domain>]
                              <image-name>

Create/upload an image

positional arguments:
  <image-name>          New image name

optional arguments:
  -h, --help            show this help message and exit
  --id <id>             Image ID to reserve
  --container-format <container-format>
                        Image container format (default: bare)
  --disk-format <disk-format>
                        Image disk format (default: raw)
  --min-disk <disk-gb>  Minimum disk size needed to boot image, in gigabytes
  --min-ram <ram-mb>    Minimum RAM size needed to boot image, in megabytes
  --file <file>         Upload image from local file
  --volume <volume>     Create image from a volume
  --force               Force image creation if volume is in use (only
                        meaningful with --volume)
  --protected           Prevent image from being deleted
  --unprotected         Allow image to be deleted (default)
  --public              Image is accessible to the public
  --private             Image is inaccessible to the public (default)
  --property <key=value>
                        Set a property on this image (repeat option to set
                        multiple properties)
  --tag <tag>           Set a tag on this image (repeat option to set multiple
                        tags)
  --project <project>   Set an alternate project on this image (name or ID)
  --project-domain <project-domain>
                        Domain the project belongs to (name or ID). This can
                        be used in case collisions between project names
                        exist.

output formatters:
  output formatter options

  -f {json,shell,table,value,yaml}, --format {json,shell,table,value,yaml}
                        the output format, defaults to table
  -c COLUMN, --column COLUMN
                        specify the column(s) to include, can be repeated

json formatter:
  --noindent            whether to disable indenting the JSON

table formatter:
  --max-width <integer>
                        Maximum display width, 0 to disable

shell formatter:
  a format a UNIX shell can parse (variable="value")

  --prefix PREFIX       add a prefix to all variable names
~~~
{: .output}
To create it from a file we use the `--file` option. We also want to specify the `--disk-format`. If we do not it will assume it is in the `raw` format which is incorrect and we will run into problems when we try to use the image.
~~~
$ openstack image create --file chris-geroux-persistent-june-6-2017.qcow2 --disk-format qcow2 chris-geroux-persistent-root
~~~
{: .bash}
~~~
+------------------+----------------------------------------------------------------------------------------------------------+
| Field            | Value                                                                                                    |
+------------------+----------------------------------------------------------------------------------------------------------+
| checksum         | ae9c0d7bd0723c43e17e5f1cb0d25408                                                                         |
| container_format | bare                                                                                                     |
| created_at       | 2017-05-04T16:44:13Z                                                                                     |
| disk_format      | qcow2                                                                                                    |
| file             | /v2/images/7885bb89-5935-4b3c-8d5a-63a30f2c1247/file                                                     |
| id               | 7885bb89-5935-4b3c-8d5a-63a30f2c1247                                                                     |
| min_disk         | 0                                                                                                        |
| min_ram          | 0                                                                                                        |
| name             | chris-geroux-persistent-root                                                                             |
| owner            | 13dd64422fd74ec5b4065f885e3b297d                                                                         |
| properties       | direct_url='rbd://3f4b0442-d864-43a5-b2f7-3878dc48cd1f/images/7885bb89-5935-4b3c-8d5a-63a30f2c1247/snap' |
| protected        | False                                                                                                    |
| schema           | /v2/schemas/image                                                                                        |
| size             | 1063321600                                                                                               |
| status           | active                                                                                                   |
| tags             |                                                                                                          |
| updated_at       | 2017-05-04T16:44:33Z                                                                                     |
| virtual_size     | None                                                                                                     |
| visibility       | private                                                                                                  |
+------------------+----------------------------------------------------------------------------------------------------------+
~~~
{: .output}
> ## Verify your uploaded image
> Try creating a VM from your image and log into it. Have a look around the file system, specifically look in `/etc/www/html` to see if your website files are there.
> 
{: .challenge}