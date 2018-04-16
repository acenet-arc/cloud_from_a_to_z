---
layout: episode
title: "Bash Scripting"
teaching: 45
exercises: 0
questions:
- "What is Bash scripting?"
- "Why use Bash?"
- "How does Bash scripting relate to cloud-init?"
- "How can passwords be automatically generated?"
objectives:
- "Make a Bash script"
- "Understand how the Bash script configures and installs WordPress."
- "Learn enough Bash scripting basics to be able to generalize to other similar installation processes."
keypoints:
- "A for loop executes commands multiple times while changing the loop variable each iteration."
- "A stream is a sequence of data elements which are made available over time."
- "The `echo` command sends a string to a stream."
- "The `head` command displays the begging of a file or stream."
- "Pipes `|` are used to pipe the output of one command to the input of the next."
- "`tr` translates characters in one set to corresponding characters in another set."
- "Redirects `<`,`>` are used to redirect output and input to files or streams."
- "`sed` is a stream editor which can be used to replace one string with another in a stream."
start: false
---

What is Bash scripting and what does it have to do with cloud-init? When we did the manual install of WordPress we ran commands in a terminal. As it turns out, there are multiple types of shells with slightly different ways of doing things. In our case we were using Bash (Born Again Shell). In addition to being able to issue these commands interactively on the command line we can also put them into a file and tell Bash to execute these commands from the file. Creating such a file is known as **Bash scripting**.

Now that we have a rough, high-level concept of what Bash scripting is, how is it connected to cloud-init? In the cloud-config file we used in the previous episode a large section of that was a Bash script which issues commands that we want to be performed to setup and install WordPress. Lets take a quick look at the contents of that file:
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
      DB_PASSWORD=$(tr -dc _A-Za-z0-9 < /dev/urandom | head -c16) # Generate a random password
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
        key=$(tr -dc _A-Za-z0-9 < /dev/urandom | head -c64)
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
All the text below the line `- content: |` down to and including the line `service apache2 restart` is a Bash script which is embedded into the cloud-config file that we passed to cloud-init. We will digest the other bits of this file later, for now we will only focus on the Bash script part. If you scan quickly through that bit of text you might even see a few commands you recognize from our manual install such as `wget http://wordpress.org/latest.tar.gz -O /tmp/latest.tar.gz` and the `tar` command which is only slightly different than the version we used previously with an extra `-C` option specifying the directory where the untarred contents of the archive should go. You will also notice lines which contain words which look like parts of the MySQL commands we ran as part of the manual setup also with some extra bits around them which might not look familiar to you. At this point you might be starting to see how this bit of text which I mentioned was a Bash script is related to the installation of the WordPress site by comparing it to the manual steps you took earlier. However, there are also likely parts which look significantly different like the lines beginning with `sed` or the `for i in `... line. In this episode we will explore various parts of Bash syntax as well as the extra Bash commands to help us understand what the rest of this Bash script is doing to automate the manual steps from yesterday.

## Why Bash?
Bash has been around since 1989 and while it is powerful it is not the most elegant way of automating setup. Bash is a bit like English, in that it has many special rules and exceptions. There are many alternatives to Bash which could be used equally well, for example Python could be used in place of Bash in the cloud-config files. However, to get almost anything done on a Linux computer, you have to start with Bash, even if it is to just run a Python script. In addition the commands to manage a Linux computer are all available through the Bash shell. That isn't to say you can get them in other ways with another languages, but it very might well involve invoking the Bash command from within that language. In addition we have been using and learning bash commands throughout this course and continuing with Bash limits the number of new things to be learnt. However, if you are so inclined, Python is a very nice language to learn and interfaces well with OpenStack so I would recommend it if you find your self wanting more while trying to get things done with Bash.

## A first Bash script
To understand how this Bash script works and how we might create our own for a different installation processes (such as for [mediawiki](https://www.mediawiki.org/wiki/MediaWiki), [omeka](https://omeka.org/), [drupal](https://www.drupal.org/), or other software stack) lets start writing our own Bash script to explore how Bash scripting works. Lets start by creating a file called `bash_test.sh`.

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
The first line is the same as the line in the Bash script in the cloud-config file. This line tells the operating system how to **interpret** the commands in the file. The `#!` is called a sha-bang or shebang which is used to tell the operating system which program to run the command with. In this case it is saying to use the command `/bin/bash` which is the same program that is used to perform the commands you type in the terminal. That means that all the command which come next are Bash commands. The second line tells Bash to `echo` or print the string `"hello world!" to the terminal. Now lets save and exit nano. Finally if we want to be able to execute the script like we do other commands, we have to give it execute permissions.
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
-rwxrwxr-x 1 ubuntu ubuntu         32 May 6 15:23 bash_test.sh
-rw-rw-r-- 1 ubuntu ubuntu 1064304640 May 4 16:23 chris-geroux-persistent-june-6-2017.qcow2
-rw-rw-r-- 1 ubuntu ubuntu       1597 May 2 17:40 openstackrc.sh
-rw-rw-r-- 1 ubuntu ubuntu       2116 May 5 13:08 wordpress.yaml
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
After the `echo` command the next line of the bash script in the cloud-config file is `DB_PASSWORD=$(tr -dc _A-Za-z0-9 < /dev/urandom | head -c16) # Generate a random password` which has a lot happening here; lets come back to that later. Instead lets have a look at the next line, `DB_NAME="wordpress"`. This line is setting the **variable** `DB_NAME` to the string "wordpress". Lets try this out by typing the following commands in our Bash terminals:
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

Lets turn our attention to the line we skipped earlier `DB_PASSWORD=$(tr -dc _A-Za-z0-9 < /dev/urandom | head -c16) # Generate a random password` and start to unpack it bit by bit. The portion after the `#` we know is a comment and while the Bash shell ignores the text following the `#` it lets us know what this line is supposed to do, generate a random password. Also we know that the `DB_PASSWORD=` is a variable assignment so variable `DB_PASSWORD` will contain the final password value. We also know that the `$( )` syntax is replaced by the result of the command contained inside. So somehow the code inside the `$( )` generates the characters for the random password. So now we have to decode what `tr -dc _A-Za-z0-9 < /dev/urandom | head -c16` outputs. Lets examine this bit of Bash script one piece at a time, starting with `head -c16`. `head` is a command which displays the beginning portion of a file. 
~~~
$ head wordpress.yaml
~~~
{: .bash}
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
~~~
{: .output}
As you can see the `head` command displayed the first 10 lines of the file. The number of lines it displays can be adjusted with the `-n` option followed by the number of lines to display
~~~
$ head -n 2 wordpress.yaml
~~~
{: .bash}
~~~
#cloud-config
package_update: true
~~~
{: .output}
In the cloud-config Bash script, a `-c` option is used instead. This option indicates the number of bytes (and since a character is represented by a single byte in standard text files this translates into the number of characters to display. 

~~~
$ head -c 5 wordpress.yaml
~~~
{: .bash}
~~~
#clou
~~~
{: .output}

So we have some idea of what the `head -c16` is doing (note that options do not require a space between the option flag and the value), but where is it getting text from? Notice the `|` character just be for the `head` command, this is known as a **pipe**. Pipes allow you to direct the output of one command into another allowing you to chain a number of commands together with pipes into a pipeline.
~~~
$ cat wordpress.yaml | head -c5
~~~
{: .bash}
~~~
#clou
~~~
{: .output}
In the above pipeline we are using the `cat` command operating on the `wordpress.yaml` file which would normally display the entire file to the terminal, however, the pipe redirects that output to the head command which then only displays the first 5 bytes or characters.

Next lets look at the `tr` command which translates one set of characters to another set of characters. This command behaves a little different from some commands we have already been using like `cat` and `cd` in that it has been designed to work interactively. 
~~~
$ tr a-z A-Z
~~~
{: .bash}
~~~

~~~
{: .output}
After you press return, the command sits there waiting for input and does not return you to the command prompt. So lets give it some input.
~~~
hello
HELLO
what's up
WHAT'S UP
~~~
{: .output}
It is echoing back the string we type after we press enter but all in upper case. This is because when we started the `tr` command we told it to convert from the set of lower case characters `a-z` to the set of upper case characters `A-Z` and it leaves all other characters as they are. How do we stop this "parroting"? We signal to the command that we are at the end of a file by pressing `ctrl`+`D`. This command is getting its input from the characters we type into the terminal, this source of characters is referred to as standard input, stdin for short. Standard input does not have to come only from characters we type into the terminal but can also come from a file using what is known as a **redirect**. A redirect can direct the contents of a file to be directed to stdin. Redirects also work in the opposite direction, in that output going to the terminal, known as stdard output or stdout for short, can be redirected to a file. Redirects are indicated by either a `>` after a command followed by a file name to place the output to a file such as
~~~
$ echo "0 hello world!" > temp_out.txt
$ cat temp_out.txt
~~~
{: .bash}
~~~
0 hello world!
~~~
{: .output}
or by a `<` which directs the input for stdin should come from a file such as
~~~
$ tr a-z A-Z < temp_out.txt
~~~
{: .bash}
~~~
0 HELLO WORLD!
~~~
{: .output}

Now lets look at the options given to the `tr` command in the cloud-config file Bash script starting with `-d`. This option changes the behaviour of `tr` fairly substantially, instead of translating from one set to another, it deletes any characters in that set and prints all other characters to the terminal. Lets try it on our `temp_out.txt` file
~~~
$ tr -d a-z < temp_out.txt
~~~
{: .bash}
~~~
0  !
~~~
{: .output}
It left the `0` two spaces `  ` and the `!` at the end, all the lower case letters have been deleted. The `-c` option specifies that the character set used should be the compliment of the set given, in other words all the characters except the ones specified.
~~~
$ tr -d -c a-z < temp_out.txt
~~~
{: .bash}
~~~
helloworld
~~~
{: .output}
The output is the contents of the `temp_out.txt` file with all non-lower case letters removed.

> ## combining options
> You might be wondering what the option `-cd` is. Actually it is two options the `-d` and the `-c` option. Options can often be combined together using only one `-`, though the ability to combine options can vary somewhat from command to command.
>
{: .callout}

We are almost at the point where we can understand the line `DB_PASSWORD=$(tr -dc _A-Za-z0-9 < /dev/urandom | head -c16)`. However there is one piece left, the `/dev/urandom` this looks like a file and it does behave much like a file, however it has some special properties. For one thing every time you read from it you get different characters. In addition the "file" never ends, you can keep reading characters from it for ever, or until your computer dies. Also the characters read from this "file" are not always the usual characters we think of (e.g. lower and upper case letters, numbers, and punctuation) these characters are only a subset of all possible characters to be represented by one byte. A byte is composed of 8 bits. Each bit has 2 possible states, 0 or 1. If you have 8 bits together you have 2<sup>8</sup>=256 different possible values, so a character which is 1 byte, or 8 bits, has 256 different possible values. The list of possible values for characters represented by one byte on a computer are given by the [ASCII](http://www.asciitable.com/) table.

![ASCII full table](../fig/asciifull.gif)
![ASCII extended table](../fig/asciiextend.gif)

The characters read from `/dev/urandom` can be any of the characters listed in the ASCII table. Lets combine what we have learnt above to see what characters we get when we read from `/dev/urandom`
~~~
$ head -c 10 < /dev/urandom
~~~
{: .bash}
~~~
NgH▒▒2a▒
~~~
{: .output}

Lets now use `tr` command to remove odd characters from `/dev/urandom` and then use a pipe to send the result to `head` to limit the number of characters we get to 16.
~~~
$ tr -cd _a-zA-Z0-9 < /dev/urandom | head -c 16
~~~
{: .bash}
~~~
0OKlugIuS4_INaBb
~~~
{: .output}
This is exactly what is used to create passwords and keys of random characters of various lengths, in this case of 16 characters.

In the cloud-config file there are a number of lines using the `sed` command which is a stream editor. So what is a stream? We have actually already been working with streams we just have not been calling them streams. A stream is a sequence of data elements which are made available over time. In our case these data elements have represented characters and have come from various places such as files and keyboard input. **stdin** and **stdout** we have talked about are streams. So how do you edit a stream? Well you put something in the middle of the stream to read data from it, and output different data, that is what `sed` does. 
~~~
# sed "s/l/d/" bash_test.yaml
~~~
{: .bash}
~~~
#!/bin/bash
echo "hedlo world!"
~~~
{: .output}
In this example we have use the file `bash_test.sh` as the input stream to `sed`. Then we told `sed` to substitute the string `l` with `d`. The `s` in the command we gave to `sed` indicates that we should substitute one string for another, with `/` bracketing each side of the search and replacement strings. This does not change the contents of the file, but instead just changed what was printed to the terminal. If we instead wanted to replace all the occurrences of `l` in the line we could append a `g` to the end of our `sed` command.
~~~
$ sed "s/l/d/g" bash_test.yaml
~~~
{: .bash}
~~~
#!/bin/bash
echo "heddo wordd!"
~~~
{: .output}
Finally if you feel like `sed` is doing what you want the `-i` option can be used to change the file in-place so that contents of the file are changed instead of being printed to the terminal. Be careful with this option as it overwrites what was there previously. There is much more that can be done with `sed`; here is a good [tutorial for sed](http://www.grymoire.com/Unix/Sed.html) illustrating many more of the capabilities of `sed`.

The final bit of decoding of the cloud-config Bash script is the lines below `mysql << EOF` which look like MySQL commands, well that is because they are. We have seen the `mysql` command already but what is the `<<` part? That is known as a **here document**. The `EOF` following the `<<` is a string which was chosen to indicate the end of the **here document**. Any string could be used for this but as soon as it is encountered the **here document** will end. So these lines are using the `mysql` command to create the "wordpress" database and grant permissions to the "wordpress" database user on this database. If the user does not exist it is created.
