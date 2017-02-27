---
layout: episode
title: "Create a persistent virtual machine"
teaching: 10
exercises: 0
questions:
- "What makes a virtual machine persistent?"
objectives:
- "Understand difference between ephemeral and persistent storage"
- "To be able to create a persistent virtual machine"
keypoints:
- "A Keypoint 0"
---

---
PREREQUISITES
* create a first VM

---
OUTLINE

* Volumes
* Discuss flavors again esp. 'p' versus 'c'
* Images (backup volumes)
  * but need CL client to download
    * import into Virtual Box
    * move between clouds (east/west)
  * creating an image of a volume a VM is currently writing too can be problematic. Better to shutdown a VM first.
* keep persistent VM for next episode
