---
layout: episode
title: "YAML"
teaching: 30
exercises: 0
questions:
- "What does CloudInit do?"
objectives:
- "Learn how to provide a cloud config file to cloud-init."
keypoints:
- "A Keypoint 0"
start: false
---


---
PREREQUISITES
* Will need to describe YAML syntax and give some examples
   * YAML lint for checking syntax
   * very fussy about spaces/tabs etc.
   * YAML lint might not catch errors in write_files contents.
* file permissions (why?) Need set permissions if creating a file.
* know about installation of packages in Linux
* know about upgrading packages in Linux
* have done some OpenStack CLI (e.g. `openstack server create`)

---
OUTLINE

The [Ubuntu CloudInit](https://help.ubuntu.com/community/CloudInit) page has a description of the various ways user-data can be used to configure a VM. Here we will focus on two: user-data scripts and cloud config data.

User-data script
* runs a script, could be bash, sh, python, perl etc. provided the right requirements are met to run it on the VM
* shebang at beginning of scripts indicates how the script should be run (e.g. "#!/bin/bash")

Cloud Config Data
* begins with "#cloud-config"

Things which could be done using CloudInit
* Add more than one user
* Change the default user from (e.g. ubuntu, centos etc.)
* Install software
* Upgrade
* Show them cloud init log `tail -f /var/log/cloud-init*.log`
* Show them the log on horizon (how I usually look at it). Double check that this method and the method above contains the same information.
* Create files
* run commands (e.g. git clone etc.)
* see file in dhsi-2016-master/cloud-init/step2_this_version_works.yaml (some tabs were replaced, and some echos were added)
In the end want them to have a cloudInit yaml file which they can use to configure their wordpress site automatically using cloud init.