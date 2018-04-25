---
layout: page
title: "Instructor Notes"
permalink: /guide/
---

Cloud Resources required per participant:

* 1 x c1-7.5gb-30(west) or c1-3.75gb-36(east)
* 1 Floating IP
* 1 Security group

This is the first VM they create and will later be used in CLI and cloud-init episodes.

* 1 x p1-1.5gb(west) or p1-0.75gb(east)
* 1 Floating IP
* 1 Security group
* 10 GB storage

First basic webserver will be installed on it. Then manually install WP on it and later these resources will be recycled to use cloud-init and then HOT. This VM is needed during the CLI episode (to create images of volumes and show recreating a VM).

**Total per participant**:

* 2 VCPUs
* 9 GB RAM
* 2 Floating IPs
* 2 Security group
* 10 GB storage
* 1 Volume

When creating a first VM, if participants are using guest accounts in a shared project and we discovered earlier that they have different IP address, have them enter a security rule to allow their specific IP address for SSH to the default security group.