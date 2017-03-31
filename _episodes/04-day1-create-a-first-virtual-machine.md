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
