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

For WordPress to function properly, we need to make a few minor modifications to our Apache web server configuration.  

First, we need to enable the use of `.htaccess` files. The reason for this is that WordPress and, more specifically, many of the WordPress plugins use this file to perform "in-directory" adjustments which will affect the behavior of Apache.

To do this, we need to modify the main Apache configuration file, located here: `/etc/apache2/apache2.conf`.

~~~
$ sudo nano /etc/apache2/apache2.conf
~~~
{: .bash}

Look for the section that starts with this heading:  

~~~
# Sets the default security model of the Apache2 HTTPD server. It does
# not allow access to the root filesystem outside of /usr/share and /var/www.
# The former is used by web applications packaged in Debian,
# the latter may be used for local directories served by the web server. If
# your system is serving content from a sub-directory in /srv you must allow
# access here, or in any related virtual host.
~~~
{: .output}

In order to allow `.htaccess` files, we need to set an `AllowOverride` directive within a `Directory` block that points to our web root directory. For this reason, append this block to the bottom of this section:  

~~~
<Directory /var/www/html/>
    AllowOverride All
</Directory>
~~~
{: .bash}

Then save and exit the file.

Second, in order to user WordPress's permalink feature, we need to enable the `mod_rewrite` Apache module. To accomplish this, we can invoke the `a2enmod` command as follows:

~~~
$ sudo a2enmod rewrite
~~~
{: .bash}

~~~
Enabling module rewrite.
To activate the new configuration, you need to run:
  service apache2 restart
~~~
{: .output}

Before restarting the Apache service, we should test to make certain that our configuration changes are correct.

~~~
$ sudo apache2ctl configtest
~~~
{: .bash}

If you see the following result:

~~~
Syntax OK
~~~
{: .output}

Then it is safe to restart Apache so that our changes take immediate effect.

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


## Download the WordPress Software

At this point, all of the prerequisite software for our virtual machine has been installed and configured. We are now ready to download the latest version of WordPress which is housed at `wordpress.org`. We'll use the `wget` command to grab the installation package and store it in the `/tmp` directory until it's ready to moved to `/var/www/html`.

~~~
$  wget http://wordpress.org/latest.tar.gz -O /tmp/latest.tar.gz
$ cd /tmp
~~~
{: .bash}

~~~
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 7851k  100 7851k    0     0  4176k      0  0:00:01  0:00:01 --:--:-- 4176k
~~~
{: .output}

Like most open source software available via the Internet, the file name (`latest.tar.gz`) ends with a `.tar.gz` extension. This means that this is a **TAR** (short for Tape Archiving) package that has been compressed using the **GNU zip** utility. To decompress and extract the file contents, we will use the following command:  

~~~
$ tar xzvf latest.tar.gz
~~~
{: .bash}

The required command-line arguments listed above are as follows:

- `x`: extract the package contents  
- `z`: decompress the file using **GNU zip**
- `v`: be verbose - show me all of the file paths
- `f`: extract from a specified file (`latest.tar.gz`)

If you engage is any subsequent Linux systems administration during the remainder of your lifetime, you will uses the `tar` command a lot.

The output should look something like this:

~~~
wordpress/
wordpress/wp-settings.php
wordpress/wp-cron.php
wordpress/wp-comments-post.php
...
... lots and lots more files...
...
wordpress/wp-includes/update.php
wordpress/wp-includes/comment.php
wordpress/wp-includes/class-wp-text-diff-renderer-table.php
wordpress/wp-config-sample.php
~~~
{: .output}

The next step is to create a blank `.htaccess` file that WordPress will use later. Then use the `chmod` command to set appropriate file permissions.

~~~
$ touch /tmp/wordpress/.htaccess
$ chmod 660 /tmp/wordpress/.htaccess
~~~
{: .bash}

Basically, the `660` argument gives read/write access to both the file's specified owner and group.

At this point, it's also a good idea to copy the sample WordPress configuration file.

~~~
$ cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
~~~
{: .bash}

While we're at it, we should also create an `upgrade` directory so that WordPress can use this to perform any subsequent software upgrades without running into any permission conflicts.

~~~
$ mkdir /tmp/wordpress/wp-content/upgrade
~~~
{: .bash}

Now we can copy the entire contents to the web document root.

~~~
$ sudo cp -av /tmp/wordpress/. /var/www/html
~~~
{: .bash}


## Configure the WordPress Web Root Directory

## Complete the Installation using the WordPress GUI
