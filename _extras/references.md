---
layout: reference
permalink: /reference/
---

## Glossary

{:auto_ids}
bash
: is a replacement for the earlier Bourne shell and is the default shell for most Linux distributions. See also [shell](#shell) for a more description of shells in general.

boot source
: what the [virtual machine](#virtual-machine) boots from. Examples of a boot sources are [volumes](#volume) and [images](#image)

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

flavor
: defines the virtual hardware specifications of a [virtual machine](#virtual-machine)

floating ip
: is an [IP address](#ip-address) which is publicly addressable from the Internet and which can be moved between [virtual machines](#virtual-machines). Also referred to as a [public IP](#public-ip).

FQDN
: is a [domain name](#domain-name) that is completely specified with all labels in the hierarchy of the domain name system.

hardware virtualization
: or sometimes referred to just as virtualization is the presentation of simulated hardware by software. For example this virtual hardware could be routers, computers, or disk drives.

hostname
: is a label that is assigned to a device connected to a computer network

hypervisor
: is computer software or hardware that creates and runs [virtual machines](#virtual-machine)

IaaS
: Infrastructer as a Service is a service which provides computing infrastructure often through use of [cloud computing](#cloud-computing)

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

OpenStack
: is open source software for creating clouds. See [cloud computing](#cloud-computing)

operating system
: software which runs on a computer to manage computer hardware, data and common services for computer programs.

PaaS
: Platform as a Service

port
: identifies a specific process or a type of network service.

port-forwarding
: also referred to as port mapping redirects communication requests from one address and port number to another while the data is traversing a network gateway or [router](#router)

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

terminal
: is a program for entering and displaying text, see also [shell](#shell).

Ubuntu
: is an [operating system](../reference#operating-system) in the [Linux](#linux) family. See the official [Ubuntu page](https://www.ubuntu.com/) for more details.

virtual device
: is an emulation of a real physical device usually through means of virtualization software.

virtual machine
: is a [virtual device](#virtual-device) emulating a computer system which provides the functionality of a physical computer. A virtual machine runs a real underlying computer.

VirtualBox
: a software tool for creating and running virtual machines. See [VirtualBox website](https://www.virtualbox.org/) for more details.

virtualization
: see [hardware virtualization](#hardware-virtualization)

volume
: a volume is a virtual disk drive that can be attached to a [virtual computer](#virtual-machine) as you would a real drive to a real computer.

WAN
: wide area network is a computer network that extends over a large geographical distance. The Internet may be considered a WAN.
