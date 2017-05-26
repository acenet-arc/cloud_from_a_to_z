---
layout: episode
title: "Installing MySQL"
teaching: 40
exercises: 0
questions:
- "What is MySQL?"
- "How can MySQL databases and tables be viewed?"
- "How can MySQL tables be modified?"
- "How do we install it securely?"
- "How do we set the MySQL root user's password?"
objectives:
- "Install the MySQL relational database management system."
- "Configure MySQL to use password authentication for its root account."
- "'Harden' the MySQL installation by executing a command-line script."
keypoints:
- "MySQL also has a 'root' account that is used to manage the MySQL server, this is **different** from the operating system 'root' account used to manage the operating system."
- "The `mysql` command allows you to view and modify MySQL databases."
- "The `SHOW DATABASES` command shows the available databases in your MySQL server."
- "The `USE` command switches which database you actively working with."
- "The `SHOW TABLES` command shows the tables in the active database."
- "The `DESCRIBE <table>` command displays data columns present in the given table."
- "The `SELECT` command displays rows from a table."
- "The `UPDATE` command is used to modify rows in a table."
- "The `EXIT` command exits the mysql program."
start: true
start_time: 540
---

In this episode we will install and configure **MySQL** which is a **relational database management system** or **RDBMS**. Lets unpack what an RDBMS is. First what is a database? A MySQL database contains a set of tables (think excel or Google spread sheets where you have rows and columns of data) containing related data. So what is a *relational* database? A relational database has its data organization based on the relational [model of data](https://en.wikipedia.org/wiki/Relational_model), which basically means that data is stored in such a way to make **queries** (requests for specific pieces of the data) on the database efficient.

MySQL is a free, open source RDBMS that runs as a service on your virtual machine. It allows multiple clients to create and manage numerous databases. A client is a program or user who access or modifies data in databases which the MySQL service manages.

WordPress requires an RDBMS to store our site's information, including posts, pages, comments, categories, tags, custom fields, user data, URLs, and numerous site options.

## Installing the MySQL server package
Let's install the MySQL server package on our VM which on Ubuntu is named `mysql-server`.
~~~
$ sudo apt install mysql-server -y
~~~
{: .bash}
In this case, `apt` installed an additional 20 software packages and libraries in order to fulfil various required MySQL application dependencies.

During the installation, you will be prompted -- repeatedly -- to set a password for the MySQL administrative 'root' user (this is not to be confused with Ubuntu's 'root' user account). You should leave this blank and select `<Ok>`, as later on we will execute a script which allows us to better secure our MySQL environment and the root password will be set then.

## Basic MySQL Operations
Lets try out our newly installed MySQL server. Lets start by connecting to our MySQL server using the MySQL monitor program which comes with our installation. A MySQL server can be a local server, in that it is running on the same computer you are working on, or it could be running on some other computer, in our case it is running locally.
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
If we were connecting to a remote server we would have to specify an IP or URL to connect to this server, when connecting locally you do not.

We have just started up the `mysql` monitor command line tool and connected to our MySQL server as the MySQL `root` user. We have done this with super user privileges. We have mentioned that the MySQL root user is different from the Ubuntu root user, in fact you can have a number of users who can connect to your MySQL server and they do not have to have accounts on your VM. MySQL manages these user accounts in databases just as it does for everything else. Lets take a look around to see what we start with in our MySQL server. At this point we are presented with a new prompt `mysql>` which allows us to issue commands to send to the MySQL server.

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
{: .output}
This command tells the MySQL to show us the databases it manages. The `;` at the end of the command lets MySQL know that we have finished writing our command. This makes it easy to spread commands across lines if needed. Commands are case insensitive, meaning we can use either lower or upper case characters and it will behave the same in both cases. However, it is convention to use upper case letters for MySQL commands to distinguish them from things like database and table names. 

As you can see there are already 4 databases in your fresh new installation. The `information_schema` database contains information about all the other databases managed by the MySQL server. The `performance_schema` and `sys` databases contain data about the performance of various server events such as queries on tables and how that performance data can be interpreted. Finally the `mysql` database contains information used in managing the MySQL server, such as user information. It would be nice to see a list of users on our MySQL server. Does our MySQL server only have a root user? Lets have a deeper look at this database to see if we can figure it out. To start working with a database you need to tell MySQL you want to `use` it.
~~~
mysql> USE mysql;
~~~
{: .bash}
~~~
Database changed
~~~
{: .output}

As was mentioned, databases contain tables, so lets have a look at what tables the `mysql` database contains.
~~~
mysql> SHOW TABLES;
~~~
{: .bash}
~~~
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| engine_cost               |
| event                     |
| func                      |
| general_log               |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| ndb_binlog_index          |
| plugin                    |
| proc                      |
| procs_priv                |
| proxies_priv              |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
31 rows in set (0.00 sec)
~~~
{: .output}
Notice the table at the bottom called `user` this is where information about MySQL users is stored. Lets see what this table looks like.
~~~
mysql> DESCRIBE user;
~~~
{: .bash}
~~~
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Field                  | Type                              | Null | Key | Default               | Extra |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Host                   | char(60)                          | NO   | PRI |                       |       |
| User                   | char(32)                          | NO   | PRI |                       |       |
| Select_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Insert_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Update_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Delete_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Create_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Reload_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Shutdown_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Process_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| File_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Grant_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| References_priv        | enum('N','Y')                     | NO   |     | N                     |       |
| Index_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Show_db_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Super_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tmp_table_priv  | enum('N','Y')                     | NO   |     | N                     |       |
| Lock_tables_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Execute_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_slave_priv        | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_client_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Create_view_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Show_view_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Create_routine_priv    | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_routine_priv     | enum('N','Y')                     | NO   |     | N                     |       |
| Create_user_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Event_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Trigger_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tablespace_priv | enum('N','Y')                     | NO   |     | N                     |       |
| ssl_type               | enum('','ANY','X509','SPECIFIED') | NO   |     |                       |       |
| ssl_cipher             | blob                              | NO   |     | NULL                  |       |
| x509_issuer            | blob                              | NO   |     | NULL                  |       |
| x509_subject           | blob                              | NO   |     | NULL                  |       |
| max_questions          | int(11) unsigned                  | NO   |     | 0                     |       |
| max_updates            | int(11) unsigned                  | NO   |     | 0                     |       |
| max_connections        | int(11) unsigned                  | NO   |     | 0                     |       |
| max_user_connections   | int(11) unsigned                  | NO   |     | 0                     |       |
| plugin                 | char(64)                          | NO   |     | mysql_native_password |       |
| authentication_string  | text                              | YES  |     | NULL                  |       |
| password_expired       | enum('N','Y')                     | NO   |     | N                     |       |
| password_last_changed  | timestamp                         | YES  |     | NULL                  |       |
| password_lifetime      | smallint(5) unsigned              | YES  |     | NULL                  |       |
| account_locked         | enum('N','Y')                     | NO   |     | N                     |       |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
45 rows in set (0.01 sec)
~~~
{: .output}
This command tells us about all the columns in the `user` table. Some interesting columns from a security perspective are `User` which is the actual user name, `Host` which tells you which host (or computer) the user is allowed to connect from. Host is set to `localhost` if the user is only allowed to connect from the computer were the MySQL server is running. Also of interest is the `authentication_string` and `plugin` column which tells us about their password and how to authenticate a MySQL user. Passwords are often encrypted depending on the `plugin` or authentication scheme used so that looking at the `authentication_string` column for a user does not tell you their password but rather what the password will be once it has been encrypted. It is not possible to retrieve a password from an encrypted `authentication_string` except for brute force trail and error comparison, which would take a very long time. Lets construct a query which will display the `User`, `Host`, `authentication_string` and `plugin` columns for all the users on our MySQL server.
~~~
mysql> SELECT User,Host,authentication_string,plugin FROM user;
~~~
{: .bash}
~~~
+------------------+-----------+-------------------------------------------+-----------------------+
| User             | Host      | authentication_string                     | plugin                |
+------------------+-----------+-------------------------------------------+-----------------------+
| root             | localhost |                                           | auth_socket           |
| mysql.sys        | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password |
| debian-sys-maint | localhost | *C1287267F257C9B8BFEC8D42A62C8E11ED394A46 | mysql_native_password |
+------------------+-----------+-------------------------------------------+-----------------------+
3 rows in set (0.00 sec)
~~~
{: .output}
The `SELECT` command retrieves rows selected from one or more tables. In our case we told the `SELECT` command that we wanted to retrieve the `User`, `Host`, `authentication_string`, and `plugin` columns `FROM` the `user` table. We didn't specify any specific rows so the command returned all the rows.

There are actually 3 users on our MySQL server including the `root` user. The `mysql.sys` user is not a usable MySQL account as the password it not valid (as noted in the authentication string). This user is used by the MySQL server to manage the `sys` database. The user `debian-sys-maint` is a used by system scripts when starting and stopping the MySQL server and performing other maintenance tasks.

Notice that the `root` user doesn't have an authentication string and uses the `auth_socket` plugin for authentication. What this means is that when a user tries to connect to MySQL it compares the MySQL username with the current operating system username and if they match it allows that user to connect. When we ran the `mysql` command with the `sudo` command it made us the user `root` when executing the `mysql` command. So in this case our system username was `root` and matched the MySQL user `root` so it let us in. The second plugin type we see is the `mysql_native_password` plugin which applies an encryption on the password and then saves that encrypted password in the authentication_string column. This is a more secure way to authenticate users as it adds an extra layer of authentication between users on the system and the MySQL server.

## Fixing the MySQL 'root' account authentication scheme

We will configure MySQL to use native password authentication for its 'root' user by changing the value of the plugin column to `mysql_native_password` for the 'root' user. The `UPDATE` command is used to change modify a row in a table.

~~~
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
~~~
{: .bash}
~~~
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
~~~
{: .output}
So in the above command we told the `UPDATE` command that we wanted to update the table `user` by `SET`ting the column `plugin` to `mysql_native_password` for rows `WHERE` the column `User='root'`. Lets have a look at the result
~~~
mysql> SELECT User,Host,authentication_string,plugin FROM user;
~~~
{: .bash}
~~~
+------------------+-----------+-------------------------------------------+-----------------------+
| User             | Host      | authentication_string                     | plugin                |
+------------------+-----------+-------------------------------------------+-----------------------+
| root             | localhost |                                           | mysql_native_password |
| mysql.sys        | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password |
| debian-sys-maint | localhost | *C1287267F257C9B8BFEC8D42A62C8E11ED394A46 | mysql_native_password |
+------------------+-----------+-------------------------------------------+-----------------------+
~~~
{: .output}

Now the user 'root' is using the `mysql_native_password` plugin to authenticate, but the root user still has no password. So that, until we set the password for the root MySQL user, we have actually made the security worse. Because now any user who can connect to our VM can also connect to the MySQL server as the MySQL root user without specifying a password. We will fix this in the next section.

Even though we have made the changes to the way the 'root' user authenticates they have not yet taken effect, the old settings are still being used. To cause these changes to take effect we have to use the `FLUSH` command to reload the settings from the databases.
~~~
mysql> FLUSH PRIVILEGES;
~~~
{: .bash}
In this case we want to reload user privileges for users which includes how they connect to the MySQL server.

At this point we are done poking around in the MySQL databases so lets, exit MySQL and then restart the database service.
~~~
mysql> EXIT;
~~~
{: .bash}
~~~
Bye
~~~
{: .output}
~~~
$ sudo systemctl restart mysql
~~~
{: .bash}
Then ensure that the `mysql` service is running again.
~~~
$ sudo systemctl status mysql
~~~
{: .bash}
Look for the line that reads:
~~~
   Active: active (running) since ...
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
{: .output}

Next you will be prompted to set the MySQL 'root' password. Again, in a production setting, it is highly recommended that you choose a long, strong, unique password consisting of numeric, mixed case, and special characters. However, for the purposes of this course, in order to keep things as simple as possible, we will choose `rootMySQLPassword`.

~~~
Please set the password for root here.

New password: rootMySQLPassword

Re-enter new password: rootMySQLPassword
~~~
{: .output}

The script will naturally complain that this is a pretty weak password. So you will be prompted if you wish to continue with this password or choose another. Press `y` to continue.

~~~
Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
~~~
{: .output}

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
{: .output}

Then you will be prompted disable remote MySQL 'root' account logins. This is also a good idea. It is always a good practice to disable the ability for administrator accounts to log in from remote locations. Press `y` to continue.

~~~
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
~~~
{: .output}

Next you will be asked to remove a default database named 'test'. This is a very good idea because we do not require this database for our WordPress installation. Not to mention, often times hackers use default accounts and test databases as an attack vector in order to compromise your system or application. Press `y` to continue.

~~~
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
~~~
{: .output}

Finally, you will be asked to reload the privilege table in order to ensure that all of the changes we just made will take immediate effect. We definitely want that to happen. So press `y` one final time to exit the script.

~~~
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y

Success.

All done!
~~~
{: .output}


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
{: .output}

If you were able to log in, execute the query, and you see the above output, then you are ready to move onto the next section.
