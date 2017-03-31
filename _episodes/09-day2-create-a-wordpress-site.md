---
layout: episode
title: "Create a wordpress site"
teaching: 180
exercises: 0
questions:
- "A question"
objectives:
- "List of objectives"
keypoints:
- "A Keypoint 0"
start: true
start_time: 540
---

---
PREREQUISITES
* services on Unubut e.g. `sudo service apache2 start` etc.
* adding users `sudo adduser --disabled-password wp-update`
* switching between users `sudo su - wp-update`
* commands:
  * `ssh-keygen`
  * `mkdir`
  * `chmod`
  * `cd`
  * `cp`
  * `exit`
  * `wget`
  * `tar`
  
---
OUTLINE
* Databases
  * Specifically MySQL
  * need to know how to go into msql prompt `mysql -u root -p`
  * need to know some basic mysql commands:
    * `create database`
    * `create user`
    * `grant`
    * `flush` (not actually sure myself what this command does)
* PHP 
  * what is it?
  * what it does that HTML doesn't
  * maybe just mention a tiny bit about how HTML and PHP interact, will come up when testing that PHP works e.g. 
  `<?php
  phpinfo();
  ?>`
  * how it interacts with MySQL
  * need to be able to set variables for mysql settings
* setup LAMP (Linux Apache MySQL PHP)
* create Wordpress user
* setup Wordpress user ssh keys (why do I need those?)
  * seems setting up allowing SSH from local host with this key and authorized_keys file
  * why are we doing that?
  * seems something about an FTP something or other
* install additional packages needed for Wordpress
  * some `sudo apt-get` commands
  * and a `sudo service apache2 restart`
* copy word press files to apache root (originally downloaded and edited as a user)
* go to web server