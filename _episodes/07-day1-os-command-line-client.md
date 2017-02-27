---
layout: episode
title: "OpenStack command line client"
teaching: 60
exercises: 0
questions:
- "Why use OpenStacks command line client?"
objectives:
- "View various OpenStack resources using CLI"
- "Create an image from a volume"
- "Download an image to a local machine"
- "Create a new virtual machine"
keypoints:
- "A Keypoint 0"
---

---
PREREQUISITES

---
OUTLINE

* Setup
  * Using a VM in the cloud
  * Install CL client
  * Put OS RC file on VM
* Introduce commands in the context of saving an image of their persistent VM
  * give a reference for all commands:
    * https://docs.computecanada.ca/wiki/OpenStack_Command_Line_Clients#Command_groups
    * Also an OS reference
  * `server`
    * `list`
    * `stop` or `delete`
  * `volume`
    * `list`
  * `image`
    * `list`
    * `create`
    * `save`
  * `server`
    * `start` or `create`
  * `ip` (should already have an IP address)
    * `floating list`
    * `floating create`
    * `floating add`

  