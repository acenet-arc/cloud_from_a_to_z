---
layout: reference
permalink: /reference/
---

## Glossary

{:auto_ids}
apt
: is a command which provides an interface to the Ubuntu package management system. Commonly used sub-commands are update for updating the package list and upgrade for upgrading already installed packages to the newest version. See [Ubuntu manual page for apt](http://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html) for more details.

bash
: is a replacement for the earlier Bourne shell and is the default shell for most Linux distributions. See also [shell](#shell) for a more description of shells in general.

boot
: or startup of a compute involves loading files and starting programs running which are contained on a [boot source](#boot-source).

boot source
: what the [virtual machine](#virtual-machine) [boots](#boot) from. Examples of a boot sources are [volumes](#volume) and [images](#image)

cat
: a [command](#command) to concatenate files and print on the standard output.

cd
: a [command](#command) to change directories.

chmod
: a [command](#command) to change file mode bits or permissions.

CIDR
: stands for Classless Inter-Domain Routing which can be used for specifying ranges of [IP addresses](#ip-address).

cloud computing
: A computing paradigm that enables access to shared pools of configurable computing resources.

command
: a series of characters entered in a [shell](#shell) indicating an action you would like the operating system to perform.

CPU
: or central processing unit, is the electronic circuitry within a computer that carries out the instructions of a computer program.

CPU oversubscription
: is when one physical [CPU](#cpu) runs two or more [VCPUs](#vcpu). In this case the one real physical CPU will switch back and forth between running tasks for the two or more VCPUs.

compute flavor
: is a [virtual machine](#virtual-machine) [flavor](#flavor) which is configured for short temporary usage. Because data safety is often less of a concern they are designed with a 20 GB root [ephemeral disk](#ephemeral-disk) and often have an extra ephemeral data disk attached. An example of a compute flavor name is `c1-7.5gb-30` which has 1 [**VCPU**](#vcpu), 7.5 GB of [**RAM**](#ram), and a 30 GB extra ephemeral data disk in addition to the 20 GB ephemeral root disk.

computer network
: is a digital telecommunications network which allows nodes in the network to share resources and exchange data.

decryption
: the process of transforming an [encrypted](#encryption) message into its original form before the encryption took place.

DNS
: or domain name server is a computer which matches [domain names](#domain-names) to [IP addresses](#ip-address).

domain name
: is an identification string that defines a realm of administrative autonomy, authority or control. In general, a domain name represents an [IP](#ip-address) resource.

encryption
: a process of transforming a message into one which is only readable by authorized parties.

elasticity
: The ability to quickly change the amount of resources being used based on demand.

ephemeral disk
: a [virtual disk](#virtual-disk) residing on the physical [node](#node) or [hypervisor](#hypervisor) which runs the [virtual machine](#virtual-machine). Ephemeral disks, as the name might suggest do not outlive their virtual machine, meaning that when their virtual machine is terminated or deleted the drive is also deleted.

flavor
: defines the virtual hardware specifications of a [virtual machine](#virtual-machine)

floating ip
: is an [IP address](#ip-address) which is publicly addressable from the Internet and which can be moved between [virtual machines](#virtual-machines). Also referred to as a [public IP](#public-ip).

FQDN
: is a [domain name](#domain-name) that is completely specified with all labels in the hierarchy of the domain name system.

git
: [git](https://git-scm.com) if a free open source, source code management tool. It keeps versioned snapshots of your code and easily displays the differences from one snapshot to the next.

github
: [github.com](https://github.com/) provides a web platform for hosting [git](#git) version control repositories.

hardware virtualization
: or sometimes referred to just as virtualization is the presentation of simulated hardware by software. For example this virtual hardware could be routers, computers, or disk drives.

hostname
: is a label that is assigned to a device connected to a computer network

hypervisor
: is computer software or hardware that creates and runs [virtual machines](#virtual-machine)

IaaS
: Infrastructure as a Service is a service which provides computing infrastructure often through use of [cloud computing](#cloud-computing)

image
: an image is a file which contains the contents of a virtual drive or [volume](#volume). Images are however more portable than volumes as they can be downloaded and uploaded to various clouds and used with software such as [VirtualBox](#virtualbox)

instance
: see [virtual machine](#virtual-machine)

IP address
: Internet Protocol address is a numerical label assigned to each device connected to a computer network.

key pair
: a pair of cryptographic keys used in asymmetric encryption. Asymmetric encryption uses a different key to [encrypt](#encryption) a message, in this case a [public key](#public-key), and another, in this case a [private key](#private-key), to [decrypt](#decryption) the message.

LAN
: local area network is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building.

Linux
: is a family of free and open-source software [operating systems](#operating-system).

ls
: a [command](#command) to list the file system structure in the [bash](#bash) [shell](#shell) and many other common shells.

node
: often refers to a computer within a [computer network](#computer-network).

OpenStack
: is open source software for creating clouds. See [cloud computing](#cloud-computing)

operating system
: software which runs on a computer to manage computer hardware, data and common services for computer programs.

PaaS
: Platform as a Service

persistent flavor
: is a [virtual machine](#virtual-machine) [flavor](#flavor) which is configured for long running or persisting virtual machines. These machines are typically for webservers and may spend substantial portions of their time not doing anything. As such they may have the [**VCPUs**](#vcpu) [oversubscribed](#oversubscribe) by up to a factor of 8. They are also meant to boot form a [volume](#volume) for added robustness. An example of a persistent flavor name is `p1-1.5gb` indicating a virtual machine with 1 VCPU and 1.5 GB of [**RAM**](#ram).

port
: identifies a specific process or a type of network service.

port-forwarding
: also referred to as port mapping redirects communication requests from one address and port number to another while the data is traversing a network gateway or [router](#router)

private IP
: an [IP address](#ip-address) assigned to devices on a [LAN](#lan) and is only accessible from within the LAN. Private IP address often have the form `192.168.XXX.YYY`.

private key
: is a key which is part of a [key pair](#key-pair) which is intended to be kept private and is used to [decrypted](#decryption) messages [encrypted](#encryption) by the [public key](#public-key).

prompt
: a set of characters presented in a [shell](#shell) to indicate it is waiting for a [command](#command).

public key
: is a key which is part of a [key pair](#key-pair) which is intended to be distributed publicly and is used to [encrypt](#encryption) messages to be [decrypted](#decryption) by the [private key](#private-key).

public IP
: see [floating IP](#floating-ip)

pwd
: a [command](#command) to print the current working directory in the [bash](#bash) [shell](#shell) and many other common shells.

RAM
: or random-access memory is a form of computer data storage that stores data for quick access by the [CPU](#cpu).

reboot
: is the act of shutting down and then [booting](#boot) an already running computer. It is also a Linux command which can be issued to cause a computer to reboot.

root
: can refer to the root of a file system, the root drive (which contains the root of the file system), or a root or administrative user.

router
: is a networking device that forwards data between computer networks for example a [WAN](#wan) and a [LAN](#lan)

SaaS
: Software as a Service

scalability
: The ability to increase resources as needed.

security group
: is a set of [rules](#security-rules) indicating how traffic can flow into and out of the [virtual machines](#virtual-machine) which are members of a security group.

security rule
: is a rule for a particular [port](#port) or range of ports dictating what [IP address](#ip-address), range of IP addresses, or which security group are allowed to send or receive data.

shell
: or more specifically a command-line interface is a user interface for interacting with an operating system by typing [commands](#command). A common shell is the [Bash](#bash) shell. Some times the word terminal and shell are used interchangeably but the shell defines which commands are used while a terminal is a means of interfacing with a shell and different shells can be used within a single terminal.

SSH
: is a cryptographic network protocol for operating network services securely over an unsecured network, commonly used for remote command execution in a [shell](#shell). It uses [key pairs](#key-pair) for authentication.

ssh-keygen
: a [command](#command) for creating [key pairs](#key-pair).

static website
: a static website is a web page that is delivered to the user exactly as stored, in contrast to [dynamic websites](../references#dynamic-websites).

sudo
: is a Linux command which runs the command following it, supplied as an argument, as the [**root**](#root) user or administrative user. See [Linux man page for sudo](https://linux.die.net/man/8/sudo) for more details.

terminal
: is a program for entering and displaying text, see also [shell](#shell).

Ubuntu
: is an [operating system](../reference#operating-system) in the [Linux](#linux) family. Ubuntu is one of the more popular Linux based operating systems and is widely used in [cloud](#cloud-computing) environments. See the official [Ubuntu page](https://www.ubuntu.com/) for more details.

VCPU
: is a [virtual](#hardware-virtualization) [CPU](#cpu).

virtual device
: is an emulation of a real physical device usually through means of virtualization software.

virtual machine
: is a [virtual device](#virtual-device) emulating a computer system which provides the functionality of a physical computer. A virtual machine runs on a real underlying computer.

VirtualBox
: a software tool for creating and running virtual machines. See [VirtualBox website](https://www.virtualbox.org/) for more details.

virtualization
: see [hardware virtualization](#hardware-virtualization)

volume
: a volume is a virtual disk drive that can be attached to a [virtual computer](#virtual-machine) as you would a real drive to a real computer.

WAN
: wide area network is a computer network that extends over a large geographical distance. The Internet may be considered a WAN.
