---
layout: episode
title: "Install PHP"
teaching: 15
exercises: 0
questions:
- "What is PHP?"
objectives:
- "Install the PHP general-purpose scripting language packages."
keypoints:
- ""
---

In this episode we will install a server-side scripting tool called **PHP** and configure it to run in conjunction with our **Apache Web Server**.  

WordPress uses PHP to store and retrieve data to and from the MySQL database. To retrieve data, WordPress (via PHP) runs SQL queries to dynamically generate webpage content.

## Installing the PHP scripting language packages

Let's install all of the PHP packages that are required by default in order to run our WordPress website.

~~~
$ sudo apt install php libapache2-mod-php php-mcrypt php-mysql php-curl php-gd php-mbstring php-mcrypt php-xml php-xmlrpc -y
~~~
{: .bash}

In my case, `apt` installed approximately 38 new packages and libraries in order to fulfill various required PHP dependencies.

Please note that each WordPress plugin might have its own set of requirements. This might require you to install additional PHP packages whenever you decide to install and enable a new plugin. Most plugin documentation will list its own PHP requirements. You can install additional PHP packages using the same method that is documented here.


## Modify Apache to look for PHP files First

By default, when a user requests a directory from Apache (without specifying a specific web page file), Apache first looks for a file called `index.html`. We want to change this behavior for WordPress so that Apache looks for `index.php` files first.  

To do this, we need to modify `/etc/apache2/mods-enabled/dir.conf` using a text editor with root privileges.  

~~~
$ sudo nano /etc/apache2/mods-enabled/dir.conf
~~~
{: .bash}

Originally, the output will look like this:

~~~
<IfModule mod_dir.c>
    DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
</IfModule>
~~~
{: .output}

All we need to do is to move `index.php` to the beginning of the list. So, the edited output should now look like this:

~~~
<IfModule mod_dir.c>
    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
</IfModule>
~~~
{: .output}

After this modification has been completed, restart the Apache web service in order for this change to take immediate effect.

~~~
$ sudo systemctl restart apache2
~~~
{: .bash}

Then check the status of the Apache service by running the following:

~~~
$ sudo systemctl status apache2
~~~
{: .bash}

Look for the line that reads:

~~~
   Active: active (running) since...
~~~
{: .output}


## Verifying our PHP installation

The easiest way to test if PHP is working is to create and execute a simply PHP script. We will first create the script and place it in the 'web root'. In our case, the 'web root' is located at `/var/www/html`.  

We will call the script `info.php` and the purpose of it will be to display a report of our PHP environment when we view it with our web browser application. If our browser displays the report, then we know that PHP is working. If it does not, then we know that we've made a mistake.

Create the script as follows:

~~~
$ sudo nano /var/www/html/info.php
~~~
{: .bash}

Add the following text (which is actually valid PHP code):

~~~
<?php
phpinfo();
?>
~~~
{: .output}

Then save and exit the file.  

To execute the script, we need to launch our web browser and navigate to the following URL:  

`http://your_server_IP_address/info.php`  

You should see something like the image below.

<img src="../fig/web-screens/php_info_output.png" alt="Ubuntu Default Web Page"/>

It is a very good idea to remove this file, once you are satisfied that this test is successful. The reason is that it could give a potential attacker too much information about your environment. To remove the file, execute the following command:

~~~
sudo rm /var/www/html/info.php
~~~
{: .bash}
