---
layout: episode
title: "Introduction to the cloud"
teaching: 30
exercises: 0
questions:
- "What is a cloud?"
- "What does \"virtual\" mean when applied to a computer?"
- "Why use Compute Canada's cloud?"
- "What is OpenStack?"
objectives:
- "To understand common cloud terminology"
- "Get exposure to the various parts of OpenStacks Dashboard"
keypoints:
- "Elasticity refers to the ability to scale devices up or down to meet demand."
- "A Virtual Machine or Device is simulated with software running on physical hardware."
- "A cloud allows one to borrow or rent virtual devices on-demand."
- "Infrastructure as a Service (IaaS): the service provider provides you with the ability to create and manage virtual devices. You have complete control over VM configuration."
- "Platform as a Service (PaaS): the service provider provides you with an environment to build and setup your software."
- "Software as a Service (SaaS): the service provider provides the software and all the infrastructure and operating system configuration and management required to run the software. (e.g. gmail)."

---

In the previous episode we looked at how the Internet works at a very basic level. To visit a website you enter an domain name into your browser which is converted to an IP address which directs your request to a computer (or LAN which then routes your request to a specific computer within that LAN based on the type of traffic) which then provides your computer with the data for the web page you requested. 

Anyone connected to the Internet can potentially put up a website for the world to see. This ability for anyone to create a website is part of what makes the Internet so great, in that you don't need lots of money and infrastructure to do this, just a computer and an Internet connection and some time to burn setting it up. However, what happens as your website grows in popularity? You get many more computers requesting your content, at some point this becomes too much for a single computer to handle so, you have to go out and get more computers. This adds not only the cost of the computers but also the time to set them up. In addition, that high load you just got, well it was a passing phase, and no one wants to visit your site any more and you have 10 computers you paid for not being used anymore. This is a problem of scalability and elasticity. The problem of a lack of **scalability** arises from not being able to easily increase your hardware resources to cope with an increased demand for your website. The problem of a lack of **elasticity** arises when you can not return the hardware when you no longer require it.

## What is cloud computing?

Cloud computing can solve the problem of scalability and elasticity described above, but what is the cloud and how does it solve this problem?

A first description of the cloud could be **it is someone else's computer that you rent or borrow**. But borrowing or renting a laptop from someone is not a cloud, so there is more to a cloud than being someone else's computer that you rent or borrow. Generally a cloud isn't something you physically possess as a user, you **access a cloud remotely** across the Internet. However, people have been remotely accessing computers for a long time before the term cloud was used so there are still more characteristics which make clouds unique.

What does a cloud computing environment have that these previously mentioned cases don't? One big characteristic is **on-demand service**. You are able to request resources (and get them) without additional human interaction. In other words, click some buttons on a website to get access to more devices, usually within seconds. More over, you can customize these devices using a web interface, for example request a computer with 2 CPUs, 7 GB of RAM, and 80 GB of disk space. Does this mean the providers of the cloud service had a computer sitting in their server room with exactly the hardware you requested waiting for you? No, they use a technology called **hardware virtualization** which is the simulation of hardware using software. What this means is that you can simulate the hardware you requested on different physical hardware. For example something with 16 CPUs, 64GB of RAM, and 2TB of disk space. In this way a single physical machine can provide multiple virtual machines (VM).

Multiple virtual machines can be simulated at once by running software within a host operating system, a virtual disk can be simulated by a file residing on the host operating system's file system. In addition it is possible to migrate virtual machines from one physical piece of hardware to another. This makes cloud infrastructure more **resilient** than traditional physical hardware in that a virtual machine can be migrated off a physical machine for upgrades and maintenance allowing the virtual machine to remain available while the original physical machine hosting the virtual machine is unavailable for maintenance.

![Virtualization](../fig/virtualization.svg)

There are many different providers of cloud services for example, [Amazon Web Service](https://en.wikipedia.org/wiki/Amazon_Web_Services), [Microsoft Azure](https://en.wikipedia.org/wiki/Microsoft_Azure), [DigitalOcean](https://en.wikipedia.org/wiki/DigitalOcean), and many more. In general you pay for cloud services on a per usage bases. To make this billing possible there is almost always some form of **resource usage monitoring and tracking** built into a cloud platform. 

## Cloud Service Models

So far we have been talking about clouds providing virtual devices as a service, also known as **Infrastructure as a Service (IaaS)**. This is one step above actually managing the hardware directly. Infrastructure as a service allows the greatest amount of flexibility and power to configure and setup your computing environment as you like it apart from actually managing the hardware yourself. With this great flexibility comes the responsibility to ensure that security patches and operating system updates are applied and that backups are made in case of disaster. This service model also requires that the user understand how to setup and configure their environments them selves. There are several other service models that are possible with clouds ranging form IaaS to **Software as a Service (SaaS)** at the other end of the spectrum where software services such as gmail or Facebook.  In the middle of these two extremes is **Platform as a Service (PaaS)** which provides an environment already configured with the tools required to develop software. An example of PaaS would be an high performance computing (HPC) environment where programing languages and libraries are installed and configured to allow the user to dive into writing code to solve their problem, or a Hadoop cluster where you can write Apache Spark code to process your data. Both of these use cases could be deployed within a cloud environment or directly on hardware.

![Service Models](../fig/service-models.svg)


## Why Compute Canada Cloud?

First and for most it is a free service offered to researchers and librarians across Canada. 

## OpenStack

<img src="../fig/os-screens/Overview.png" alt="OpenStack Dashboard Overview" style="width: 800px;"/>

<img src="../fig/os-screens/Instances.png" alt="OpenStack Dashboard Instances" style="width: 800px;"/>

* the cloud under the hood can be complicated luckily you don't need to look under the hood to use it. Many people just take their car to a mechanic when there is a problem under the hood similarly with the cloud, contact cloud@computecanada.ca

---
PREREQUISITES 

---
OUTLINE

* What is a cloud
  * Some one Else's computer **DONE**
  * Virtual computers (simulated computers running on real computers) **DONE**
  * Disk Images (simulated disks as files on real disks) **DONE**
  * the descriptions of the above could maybe use some more work/elaboration
* Go over components of Horizon (Dashboard)
  * Overview (quotas)
  * Instances (VMs)
  * Volumes (disks)
  * Images (archives of Volumes/Static disks)
  * Access & Security
    * Security Groups
    * Key pairs
    * Floating IPs

These items could be left till much later or not mentioned at all

* Access & Security
  * leave API Access till later 
* Networking 
* Orchestration 
* Identity
  
