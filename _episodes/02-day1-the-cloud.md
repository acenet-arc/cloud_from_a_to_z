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
- "A Keypoint 0"
---

In the previous episode we looked at how the Internet works at a very basic level. To visit a website you enter an domain name into your browser which is converted to an IP address which directs you at a computer (or LAN which then routes you to a specific computer based on the type of traffic) which then provides you with a website. Anyone connected to the Internet can potentially put up a website for the world to see. This ability for anyone to do this is part of what makes the Internet so great, in that you don't need lots of money and infrastructure to do this, just a computer and an Internet connection and some time to burn setting it up. However, what happens as your website grows in popularity? You get many more computers requesting your content, at some point this becomes too much for a single computer to handle so, you have to go out and get more computers. This adds not only the cost of the computers but also the time to set them up. In addition, that high load you just got, well it was a passing phase, and no one wants to visit your site any more and you have 10 computers you paid for not being used anymore.

Cloud to the rescue.

* the cloud under the hood can be complicated luckily you don't need to look under the hood to use it. Many people just take their car to a mechanic when there is a problem under the hood similarly with the cloud, contact cloud@computecanada.ca

---
PREREQUISITES 

---
OUTLINE

* What is a cloud
  * Some one Else's computer
  * Virtual computers (simulated computers running on real computers)
  * Disk Images (simulated disks as files on real disks)
  
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
  
