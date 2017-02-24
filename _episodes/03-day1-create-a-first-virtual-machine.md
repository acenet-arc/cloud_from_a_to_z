---
layout: episode
title: "Create a first virtual machine"
teaching: 60
exercises: 0
questions:
- "What are keypairs used for?"
objectives:
- "Create a key pair"
- "Create a VM which you can log into"
keypoints:
- "A Keypoint 0"
---

---
PREREQUISITES
* need to know `ls`, `ls -l`
 * should maybe also know a bit more
    * `rm`
    * `mkdir`
    * `cat`
* file permissions
  * user, group, everyone
  * wrx
  * `chmod`
* need to know about `.ssh` folder

---
OUTLINE

* Key pairs
  * Describe key pairs and what they are for
    * need to mention about SSH
  * Creating one using the OS dashboard
  * Creating one on the client (Windows/Linux/Mac) and importing it into OS
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
