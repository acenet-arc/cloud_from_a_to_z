---
layout: episode
title: "Install MySQL"
teaching: 40
exercises: 0
questions:
- "What is MySQL?"
- "How do we install it securely?"
- "How do we set the MySQL root user's password?"
objectives:
- "Install the MySQL relational database management system."
- "Configure MySQL to use password authentication for its root account."
- "'Harden' the MySQL installation by executing a command-line script."
keypoints:
- "Ubuntu has a 'root' account that is used to manage the operating system."
- "MySQL also has a different 'root' account that is used to manage only MySQL."
start: true
start_time: 540
---

In this episode we will install and configure the **MySQL Relational Database System**. MySQL is a free, open source database management system that runs as a service on your virtual machine. It allows multiple clients to create and manage numerous databases.  

WordPress requires a relational database system in order to organize and provide access to a database (which we will create later) that will store our WordPress site's information. This information includes posts pages, comments, categories, tags, custom fields, user data, URLs, and numerous site options.


## Installing the MySQL server package

Let's install the MySQL server package on our VM. Once again, we will use the `apt` command and we will elevate our account to use administrative privileges via the `sudo` command.

~~~
$ sudo apt install mysql-server -y
~~~
{: .bash}   

In my case, `apt` installed an additional 20 software packages and libraries in order to fulfil various required MySQL application dependencies.  

During the installation, you will be prompted -- repeatedly -- to set a password for the MySQL administrative 'root' user. (This is not to be confused with Ubuntu's 'root' user account.) You should leave this blank and select `<Ok>` because, later on, we will execute a script which allows us to better secure our MySQL environment and the root password will be set then. 


## Fixing the MySQL 'root' account authentication scheme

Before we do anything, we need to fix the default method that Ubuntu uses to authenticate the MySQL 'root' user. By default, Ubuntu does not configure the MySQL 'root' account to use MySQL native password authentication. This means that you can log into Ubuntu using Ubuntu's 'root' administrator account (or use `sudo`) and then, when you subsequently log into MySQL, you would never be prompted for a password. We want to disable this behavior.  

To achive this, we will configure MySQL to use native password authentication for its 'root' account simply by running a couple of database administrator commands.

First log into MySQL as 'root'.

~~~
$ sudo mysql -u root
~~~
{: .bash}

~~~
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 22
Server version: 5.7.18-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
~~~
{: .output}

Then select the `mysql` database.

~~~
mysql> USE mysql;
~~~
{: .bash}

~~~
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
~~~
{: .output}
This indicates to MySQL that all the commands to come will work with this database. Next, execute a SQL `update` command to change the authentication scheme for the MySQL 'root' user.

~~~
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
~~~
{: .bash}

~~~
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
~~~
{: .output}

To make the changes take effect immediately, flush database privileges.

~~~
mysql> FLUSH PRIVILEGES;
~~~
{: .bash}

Finally, exit MySQL and then restart the database service.

~~~
mysql> EXIT;
Bye

$ sudo systemctl restart mysql
~~~
{: .bash}

Ensure that the `mysql` service is running as follows:

~~~
$ sudo systemctl status mysql
~~~
{: .bash}

Look for the line that reads:

~~~
   Active: active (running) since...
~~~
{: .output}

Now that we've made this configuration change, we are ready to move on to the next section and 'harden' our MySQL installation by running a security script that will ensure that questionable (and dangerous) default settings have been removed.

## Executing the `mysql_secure_installation` script

Initiate the script by executing the following:

~~~
$ mysql_secure_installation
~~~
{: .bash}  

The first task is to select a level of password validation. We will select `y` to enable the setup VALIDATE PASSWORD plugin. You will then be prompted to select 1 of 3 password level policies. When configuring MySQL to run in a production environment, it is highly recommended that you select `2 = strong`. For the purposes of this course, will select `0 = Low`. This means that our passwords only have to be 8 characters long.

~~~
Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No: y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
~~~
{: .bash}

Next you will be prompted to set the MySQL 'root' password. Again, in a production setting, it is highly recommended that you choose a long, strong, unique password consisting of numeric, mixed case, and special characters. However, for the purposes of this course, in order to keep things as simple as possible, we will choose `rootMySQLPassword`.

~~~
Please set the password for root here.

New password: rootMySQLPassword

Re-enter new password: rootMySQLPassword
~~~
{: .bash}

The script will naturally complain that this is a pretty weak password. So you will be prompted if you wish to continue with this password or choose another. Press `y` to continue.

~~~
Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
~~~
{: .bash}

You will next be prompted to remove anonymous users. This is a good idea. Press `y` to continue.

~~~
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
~~~
{: .bash}

Then you will be prompted disable remote MySQL 'root' account logins. This is also a good idea. It is always a good practice to disable the ability for administrator accounts to log in from remote locations. Press `y` to continue.

~~~
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
~~~
{: .bash}

Next you will be asked to remove a default database named 'test'. This is a very good idea because we do not require this database for our WordPress installation. Not to mention, often times hackers use default accounts and test databases as an attack vector in order to compromise your system or application. Press `y` to continue.

~~~
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
~~~
{: .bash}

Finally, you will be asked to reload the privilege table in order to ensure that all of the changes we just made will take immediate effect. We definitely want that to happen. So press `y` one final time to exit the script.

~~~
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y

Success.

All done!
~~~
{: .bash}


## Verifying our MySQL installation

To verify that everything works, log back into MySQL as follows:

~~~
$ mysql -u root -p
~~~
{: .bash}

You should be prompted for the root password. Enter `rootMySQLPassword`.

Next let's run a query which lists all databases.

~~~
mysql> SHOW DATABASES;
~~~
{: .bash}

~~~
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
~~~
{: .bash}

If you were able to log in, execute the query, and you see the above output, then you are ready to move onto the next section.
