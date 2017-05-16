---
layout: episode
title: "Bash Scripting"
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

What is Bash scripting and what does it have to do with cloud-init? When we did the manual install of WordPress we ran commands in a terminal. As it turns out, there are multiple types of shells with slightly different ways of doing things. In our case we were using Bash (Born Again Shell). In addition to being able to issuse these commands interactively on the command line we can also put them into a file and tell Bash to execute these commands from the file.

Now that we have a rough, high-level concept of what Bash scripting is, how is it connected to cloud-init? In the cloud config file we used in the previous episode a large section of that was a Bash script which issues commands that we want to be performed to setup and install WordPress. Lets take a quick look at the contents of that file:
~~~
#cloud-config
package_update: true
package_upgrade: true
packages:
  - apache2
  - mysql-server
  - php
  - libapache2-mod-php
  - php-mcrypt
  - php-mysql
  - php-curl
  - php-gd
  - php-mbstring
  - php-xml
  - php-xmlrpc
write_files:
  - content: |
      #!/bin/bash
      
      echo "making DB_PASSWORD ..."
      DB_PASSWORD=$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16) # Generate a random password
      DB_NAME="wordpress"
      DB_USER="wordpress"
      DB_HOST=localhost
      
      echo "getting latest wordpress ..."
      wget http://wordpress.org/latest.tar.gz -O /tmp/latest.tar.gz
      echo "untarring wordpress ..."
      tar xzf /tmp/latest.tar.gz -C /var/www/
      
      # create the database, and configure the wordpress user.
      echo "configuring database ..."
      mysql <<EOF
      CREATE DATABASE $DB_NAME;
      GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER
      ON $DB_NAME.*
      TO $DB_USER@$DB_HOST
      IDENTIFIED BY '$DB_PASSWORD';
      FLUSH PRIVILEGES;
      EOF
      
      # copy the config file and then configure database name, username, and password
      echo "editing the wordpress configuration ..."
      cp /var/www/wordpress/wp-config-sample.php /var/www/wordpress/wp-config.php
      sed -i "s/database_name_here/$DB_NAME/g" /var/www/wordpress/wp-config.php
      sed -i "s/password_here/$DB_PASSWORD/g" /var/www/wordpress/wp-config.php
      sed -i "s/username_here/$DB_USER/g" /var/www/wordpress/wp-config.php
      
      # configure security keys : https://codex.wordpress.org/Editing_wp-config.php#Security_Keys
      echo "configuring wordpress security keys ..."
      for i in $(seq 1 8)
      do
        key=$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c64)
        sed -i "0,/put your unique phrase here/s/put your unique phrase here/$key/" /var/www/wordpress/wp-config.php
      done
      
      echo "moving install from /var/www/wordpress to /var/www/html ..."
      mv /var/www/wordpress /var/www/html/
      
      service apache2 restart
    path: /tmp/bootstrap-wp.sh
    permissions: "0755"
runcmd:
  - bash /tmp/bootstrap-wp.sh
~~~
{: .output}
All the text below the line `- content: |` down to and including the line `service apache2 restart` is a Bash script which is embedded into the cloud config file that we passed to cloud-init. We will digest the other bits of this file later, for now we will only focus on the Bash Script part. If you scan quickly through that bit of text you might even see a few commands you recognize from our manual install such as `wget http://wordpress.org/latest.tar.gz -O /tmp/latest.tar.gz` and the `tar` command which is only slightly different than the version we used previously with an extra `-C` option specifying the directory where the untarred contents of the archive should go. You will also notice lines which contain words which look like parts of the MySQL commands we ran as part of the manual setup also with some extra bits around them which might not look familiar to you. At this point you might be starting to see how this bit of text which I mentioned was a Bash script is related to the installation of the WordPress site by comparing it to the manual steps you took earlier. However, there are also likely parts which look significantly different like the lines beginning with `sed` or the `for i in `... line. In this episode we will explore various parts of Bash syntax to help us understand what the rest of this Bash script is doing to automate the manual steps from yesterday.

## A first Bash script
To understand how this Bash script works and how we might create our own for different installation processes lets start writing our own Bash script to explore how Bash scripting works. Lets start by creating a file called `bash_test.sh`.

~~~
$ nano bash_test.sh
~~~
{: .bash}
and enter the text
~~~
#!/bin/bash
echo "hello world!"
~~~
{: .output}
The first line is the same as the line in the Bash script in the cloud config file. This line tells the operating system how to **interpret** the commands in the file. The `#!` is called a sha-bang or shebang which is used to tell the operating system which program to run the command with. In this case it is saying to use the command `/bin/bash` which is the same program that is used to perform the commands you type in the terminal. That means that all the command which come next are Bash commands. The second line tells Bash to `echo` or print the string `"hello world!" to the terminal. Now lets save and exit nano. Finally if we want to be able to execute the script like we do other commands, we have to give it execute permissions.
~~~
$ chmod +x bash_test.sh
~~~
{: .bash}
and check that it did what we expected with
~~~
$ ls -l
~~~
{: .bash}
~~~
total 1
-rwxrwxr-x 1 ubuntu ubuntu   32 May 12 15:23 bash_test.sh
~~~
{: .output}
notice that it has an `x` now in the permissions column for the `bash_test.sh` file indicating that it can be executed. We can now run the bash script with
~~~
$ ./bash_test.sh
~~~
{: .bash}
~~~
hello world!
~~~
{: .output}
You can verify that the script did the same thing as if you had run the `echo` command directly in the terminal.
~~~
$ echo "hello world!"
~~~
{: .bash}
~~~
hello world!
~~~
{: .output}
> ## Text vs. Whatever
>
> We usually call programs like Microsoft Word or LibreOffice Writer "text editors", but we need to be a bit more careful when it comes to writing scripts. By default, Microsoft Word uses `.docx` files to store not only text, but also formatting information about fonts, headings, and so on. This extra information isn't stored as characters, and doesn't mean anything to tools like `bash`: they expect input files to contain nothing but the letters, digits, and punctuation on a standard computer keyboard. When editing scripts, therefore, you must either use a plain text editor, or be careful to save files as plain text.
{: .callout}

Exploring how bash works can sometimes be easier and faster directly on the command line rather than in a script and as we just saw commands run in the terminal work similarly to those in a Bash script. For the next few sections of this episode we will simply run commands in the terminal in the interest of speed. However, when using scripts the commands will be saved and can be easily reused multiple times without having to retype all the commands, we will return to writing commands into our script later.

## Decoding the WordPress Bash script
After the `echo` command the next line of the bash script in the cloud config file is `DB_PASSWORD=$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16) # Generate a random password` which has a lot happening here; lets come back to that later. Instead lets have a look at the next line, `DB_NAME="wordpress"`. This line is setting the **variable** `DB_NAME` to the string "wordpress". Lets try this out by typing the following commands in our Bash terminals:
~~~
$ message="hello world!"
$ echo $message
~~~
{: .bash}
~~~
hello world!
~~~
{: .output}
We stored a string `"hello world!"` inside the variable `message` to later reference that variable using `$message` in order to print out the string. The `$` is used when you are referencing a variable but not when you are assigning a value to it. Also notice that there are no spaces on either side of the `=`. You might be wondering why variables are useful. In this case it looks like we added to the complexity without gaining anything. Generally adding complexity for no reason is a bad idea as simpler scripts are easier to understand and thus less likely to contain mistakes. However, in the long run using variables can simplify the code. For example if we had a longer script which performed more tasks than this simple case we might want to print out the same message in multiple places. If we were not using variables and then later wanted to change the message we would have to edit the code in multiple places to change the message. However, using a variable for the message we can change it in one place and that change will be referenced everywhere we use the variable.

You can also assign one variable to another.
~~~
$ greeting=$message
$ echo $greeting
~~~
{: .bash}
~~~
hello world!
~~~
{: .output}

You can also combine variables with other strings or variables
~~~
$ message=$greetings" from Chris"
$ echo $message
~~~
{: .bash}
~~~
hello world! from Chris
~~~
{: .output}

> ## Comments in Bash scripts
> You can add `#` to indicate that what ever comes after it should not be interpreted as a command but rather as a comment for humans to read. It is a good idea to describe what your bash script is doing so that your future self and others can more easily understand what your script is doing.
{: .callout}

Next lets look at the lines `for i in $(seq 1 8)` down to the line `done`. This is what is known as a **for loop** which lets you repeat commands many times without having to type them out many times. Usually you do not want to do exactly the same command each time and instead want to change an argument to the command. The syntax for a for loop looks like this:
~~~
for <variable-name> in <list-of-values>
do
<commands to do each iteration of the loop>
done
~~~
{: .output}

Here is an example of a for loop which `echo`s out names in a list.
~~~
$ for name in Bob John Pete
> do
> echo $name
> done
~~~
{: .bash}
~~~
Bob
John
Pete
~~~
{: .output}

Loops often span multiple input lines. The `>` indicates, that the shell is waiting for us to type the next line of the multi-line command. When putting a for loop into a script, each part of this command goes on separate lines as it does when typing it into the terminal. The loop then iterates through the names in the list `Bob John Pete` and each time the variable `name` takes on one of the names in the list.

Next lets take a look at the command `seq`. If we look at the manual page for the command we see that it prints out a sequence of numbers from the first value to the last value.
~~~
$ seq 1 8
~~~
{: .bash}
~~~
1
2
3
4
5
6
7
8
~~~
{: .output}

The final piece we need to understand that for loop is the what the syntax `$( )` is doing in `$(seq 1 8)`. This syntax is what is known as **command substitution** in Bash. What this means is that the resulting output of the contained command is substituted into the rest of the surround command. Lets try this with a for loop.
~~~
$ for i in $(seq 1 8)
> do
> echo "I am number "$i
> done
~~~
{: .bash}
~~~
I am number 1
I am number 2
I am number 3
I am number 4
I am number 5
I am number 6
I am number 7
I am number 8
~~~
{: .output}

Lets turn our attention to the line we skipped earlier `DB_PASSWORD=$(</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16) # Generate a random password` and start to unpack it bit by bit. The portion after the `#` we know is a comment, so we can stop worrying about what that does. Also we know that the `DB_PASSWORD=` is a variable assignment. We also know that the `$( )` syntax says set the variable to the result of the command contained inside. So now we have to decode the `</dev/urandom tr -dc _A-Z-a-z-0-9 | head -c16`. Notice the `|` character, this is known as a **pipe**.

Pipes allow you to direct the output of one command into another allowing you to chain a number of commands together with pipes into a pipeline. You will also notice the `head` command which displays some beginning portion a file or stream.

~~~
~~~

## Redirects
When we run a command the output from that command is generally printed to the terminal (also known as standard output or stdout for short). This output can be redirected to a file using the `>` redirect.

~~~
$ ls
~~~
{: .bash}
~~~
bash_test.sh
~~~
{: .output}
~~~
$ ls > dir_list.txt
$ cat dir_list.txt
~~~
{: .bash}
~~~
dir_list.txt
test_bash.sh
~~~
{: .output}

## Sed (Stream Editor)
~~~
# sed -i
~~~
{: .bash}

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