---
layout: episode
title: "Create a WordPress site"
teaching: 55
exercises: 0
questions:
- "How do we download the WordPress software?"
- "How do we install the WordPress software?"
- "How do we finalie the WordPress installation?"
objectives:
- "Create a WordPress database and user."
- "Modify the Apache configuration."
- "Download the WordPress source code."
- "Configure the WordPress web root directory."
- "Finalize the installation using the WordPress GUI."
keypoints:
- ""
---

During the previous three episodes, we finished installing our LAMP software stack on our virtual machine. Consequently, in this episode we are now ready to move on to the activity of installing and configuring our WordPress application. The entire procedure will require us to accomplish the following systems administration tasks:  

- we will create a WordPress database and user  
- we will modify our Apache web server configuration
- we will download the WordPress software
- we will configure the WordPress web root directory  
- we will complete the installation using the WordPress web interface

## Create the WordPress MySQL Database and User

The very first thing we need to do is log into our database command prompt using the MySQL root administrative account. To do so, issue the following command:  

~~~
$ mysql -u root -p
~~~
{: .bash}

You will be prompted to enter your password. (Remember from a previous episode, that we had set this password to `rootMySQLPassword`.) We now want to create a separate database that only the WordPress application can access. To keep things simple, let's name the database `wordpress`.

~~~
mysql> CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
~~~
{: .bash}

If successful, the output should look like the following:  

~~~
Query OK, 1 row affected (0.00 sec)
~~~
{: .output}

Next, it is a good idea to also create a separate MySQL (who does *NOT* have administrative access) that WordPress will use exclusively to administrate the `wordpress` database. In order to tighten security, only WordPress is required to have access to this user's authentication credentials and the only database this user has access to is the `wordpress` database. Again, to keep things simple, let's call this user `wordpressuser`. In production, you would want to create a strong and unique password for this user. However, for this course, we will use `userMySQLPassword` as the password.

~~~
mysql> GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost' IDENTIFIED BY 'userMySQLPassword';
~~~
{: .bash}

If successful, the output should look like this:

~~~
Query OK, 0 rows affected, 1 warning (0.00 sec)
~~~
{: .output}

Finally, in order to ensure that our modifications take immediate effect, we need to flush the privileges.

~~~
mysql> FLUSH PRIVILEGES;
~~~
{: .bash}

The output should look like this:

~~~
Query OK, 0 rows affected (0.00 sec)
~~~
{: .output}

You may now exit the MySQL database system management application.

~~~
mysql> QUIT;
~~~
{: .bash}


## Modify the Apache Web Server Configuration

## Download the WordPress Software

## Configure the WordPress Web Root Directory

## Complete the Installation using the WordPress GUI
