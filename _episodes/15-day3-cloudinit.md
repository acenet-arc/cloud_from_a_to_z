---
layout: episode
title: "CloudInit"
teaching: 180
exercises: 0
questions:
- "What does CloudInit do?"
objectives:
- "List of objectives"
keypoints:
- "A Keypoint 0"
start: true
start_time: 540
---

---
PREREQUISITES
* Will need to describe YAML syntax and give some examples
   * YAML lint for checking syntax
* file permissions
* know about installation of packages in Linux
* know about upgrading packages in Linux

---
OUTLINE

Things which could be done using CloudInit
* Add more than one user
* Change the default user from (e.g. ubuntu, centos etc.)
* Install software
* Upgrade
* Show them cloud init log `tail -f /var/log/cloud-init*.log`
* Show them the log on horizon (how I usually look at it). Double check that this method and the method above contains the same information.
* Create files
* run commands (e.g. git clone etc.)

In the end want them to have a cloudInit yaml file which they can use to configure their wordpress site automatically using cloud init.

  
