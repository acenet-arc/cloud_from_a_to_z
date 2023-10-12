---
layout: episode
title: "Hosting a site on github"
teaching: 15
exercises: 0
questions:
-
objectives:
-
keypoints:
-
---

# Jekyll site hosting options

First off, what does it mean to host a site? So far we have created and viewed our Jekyll websites from a computer setup for you on the Alliance cloud and later on a VM we setup ourselves in this workshop. These computers provided the necessary software to generate your static Jekyll site from your markdown and HTML and CSS source content. It also has a webserver setup and configured to allow your site to be viewed from the internet. This service of providing a computer on which you site is served up to the public on the internet is known as site hosting.

However for static sites and in particular Jekyll sites, another popular and free hosting option is available. A service called github, which will take a look at now.

# What is github?

Github is a free, mostly, cloud service for open source software development. I say, mostly, because if you want to keep your data private they charge. However, if you are fine sharing it publicly it is free. Github's main service is to host git repositories. So what is a git repository?

# What is git?

Git is a program to help manage versions of files, primarily text files, like the files we have been editing to create our websites.

We are going to do a very quick introduction to git, for a more complete lesson on using git, please see the [software carpentry git lesson](https://swcarpentry.github.io/git-novice/).

We will start by creating a new git repository. A git repository is a number of files and directories which contains meta data for tracking changes of your files and directories. Before we create a repository lets make sure we are in the correct place. We want to create our new repository in the directory containing the files we want to track, which in our case is the source directory for our websites.
~~~
$ pwd
~~~
{: .bash}
~~~
/home/<your-username>/forty-jekyll-theme-master
~~~
{: .output}

## Create a git repository
Now to create a new git repository type
~~~
$ git init
~~~
{: .bash}
~~~
Initialized empty Git repository in /home/<your-username>/forty-jekyll-theme-master/.git/
~~~
{: .output}
This command creates a new `.git` directory inside the current working directory to hold the meta data required to track your changes to your files.

## See repository status
To get a status report on our repository we can type `git status`.
~~~
$ git status
~~~
{: .bash}
~~~
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .github/
        .gitignore
        .gitlab-ci.yml
        404.md
        CONTRIBUTING.md
        Gemfile
        LICENSE.md
        README.md
        _config.yml
        _includes/
        _layouts/
        _posts/
        _sass/
        all_posts.md
        assets/
        elements.md
        facts_about_dogs.md
        forty_jekyll_theme.gemspec
        generic.md
        index.md
        landing.md

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

This tells us that we are on the 'master' branch. With git you can have different sets of changes living on different "branches" in parallel to each other and you can switch between branches. We don't need any more than one branch so other than knowing that we are working in the 'master' branch there isn't much more about branches we need to know.

Then it tells us that there are "No commits yet" which mean we have not yet saved any state of our files to our repository.

## Add files to be tracked

Further git lists a number of "Untracked files", these are files which git is not currently tracking the changes of but reside in the same directory as the git repository. Git even gives us a hint that we should use `git add` to start tracking those files. This is exactly what we want to do next let git know all the files we want it to track lets do that now.

At the top of this list of files we see
~~~
.github/
.gitignore
/gitlab-ci.yml
~~~
{: .output}
these are hidden files and contain configuration information for git. It turns out that the theme we downloaded was tracked using git previously and included some extra configuration data for git github and another git repository hosting service gitlab. Of these the only file we will want to include in our repository is `.gitignore` which provides a list of files and file types that git should ignore such that git won't even print them as "Untracked files". Lets start by adding this file to our repository.

~~~~
$ git add .gitignore
~~~~
{: .bash}
~~~
$ git status
~~~
{: .bash}
~~~
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .github/
        .gitlab-ci.yml
        404.md
        CONTRIBUTING.md
        Gemfile
        LICENSE.md
        README.md
        _config.yml
        _includes/
        _layouts/
        _posts/
        _sass/
        all_posts.md
        assets/
        elements.md
        facts_about_dogs.md
        forty_jekyll_theme.gemspec
        generic.md
        index.md
        landing.md
~~~
{: .output}

It now shows us there there are "Changes to be committed" and that these new changes are one "new file", our `.gitignore` file.

Lets add the rest of the files in our site's source directory.
~~~
$ git add 404.md CONTRIBUTING.md Gemfile LICENSE.md README.md _config.yml  _includes/ _layouts/ _posts/ _sass/ all_posts.md assets/ elements.md facts_about_dogs.md forty_jekyll_theme.gemspec  generic.md index.md landing.md
$ git status
~~~
{: .bash}
~~~
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   404.md
        new file:   CONTRIBUTING.md
        new file:   Gemfile
        new file:   LICENSE.md
        new file:   README.md
        new file:   _config.yml
        new file:   _includes/footer.html
        new file:   _includes/head.html
        new file:   _includes/header.html
        new file:   _includes/tiles.html
        new file:   _layouts/allposts.html
        new file:   _layouts/home.html
        new file:   _layouts/landing.html
        new file:   _layouts/page.html
        new file:   _layouts/post.html
        new file:   _posts/2016-8-20-etiam.md
        new file:   _posts/2016-8-21-consequat.md
        new file:   _posts/2016-8-22-ipsum.md
        new file:   _posts/2016-8-23-magna.md
        new file:   _posts/2016-8-24-tempus.md
...
~~~
{: .output}
Note that git actually added all the files within the directories we included in the `git add` command. Git doesn't actually track directories, only files so instead of adding the directories it added all the files within the directory, which is what we want.

## Create a commit
Now that we have told git that all the files we want to track for our site lets create our first commit.

~~~
$ git commit
~~~
{: bash}
~~~
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'user01@workshop.(none)')
~~~
{: .output}

It turns out that when you create commits, git associates some information about us with the commit. Lets set that information now. Fortunately git has told us exactly the commands we need to use to set this information.

~~~
$ git config --global user.email "chris.geroux@ace-net.ca"
$ git config --global user.name "Chris Geroux"
~~~
{: .bash}

Now, back to our commit. This command opens up the nano text editor we have been using all along to write a message to identify our commit.
~~~
$ git commit
~~~
{: .bash}
I enter a note about our commit "Initial commit of our site"
~~~
Initial commit of our site

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
#
# Initial commit
#
# Changes to be committed:
#       new file:   .gitignore
#       new file:   404.md
#       new file:   CONTRIBUTING.md
...
~~~
{: .output}
And then press `ctrl`+`x` to exit, followed by pressing "Y" to confirm that I wish to save the modified buffer, then "enter" to confirm the file name to write to.

We have now made our first git commit. Now if we take a look at the status report for our repository we see
~~~
$ git status
~~~
{: .bash}
~~~
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .github/
        .gitlab-ci.yml

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}
We only see the could untracked files we didn't add to our repository to be tracked by git.

To continue working on our site we could then go and edit files or create new files and repeat the process of `git add -u` to add any updated files and or `git add <new-file-name>` to add new files. Then follow this with a `git commit` to save our new changes as a new commit to the repository.

We now have a local git repository which is tracking changes to our site. The next step is to create a new remote github repository and configure our local repository to push up to it.

By pushing our local repository up to our remote github repository we can configure our remote github repository to generate our Jekyll site and make the generated site publicly accessible.

# How to host your site on github?

## Create a new remote git repository on github.
1. Go to [github.com](http://github.com) and log in.
2. Click *New* next to "Repositories" on the left
3. Give your repository a name 'first-jekyll-site'
4. Make sure "Public" is check and click "Create repository"

Github will then present you with your new repository and some "Quick setup" information. We will want to copy the text that looks something like `git@github.com:<your-github-username>/first-jekyll-site.git` as we will need this shortly.

## Add a remote to local git repository
Now back to our terminal where we were working with our local git repository we want to tell it how to connect to our remote github repository so we can push our local repository up to github. We can do this with the `git remote add` command.
~~~
$ git add remote origin git@github.com:<your-github-username>/first-jekyll-site.git
~~~
{: .bash}

This command adds a new reference to a new remote repository called `origin`. We can now `push` our repository to this new remote repository, except that we need to add a method of authenticating with github.


## Create a keypair
Github no longer supports passwords and so the simplest alternative is to use keypairs. Lets create a new keypair.

~~~
$ ssh-keygen -t rsa -b 2048
~~~
{: .bash}
~~~
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user01/.ssh/id_rsa):
~~~
{: .output}
Press enter to accept the default keyfile name
~~~
Enter passphrase (empty for no passphrase):
~~~
{: .output}

Then enter the pass phrase for your key pair. **It will not show key presses as you type your passphrase.** It will then ask you to confirm your passphrase.

Next we need to add our public key to github. Back on the github web page go to your account **settings** from the drop drop down in the top right corner. The go to **SSH and GPG keys** under the left side menu. The click **New SSH key**. Enter a memorable title e.g. `user01-workshop`. Next we need to copy our public key into this text box so go back to your terminal where we created the keypair (e.g. the `ssh-keygen` command).

~~~
$ cat ~/.ssh/id_rsa.pub
~~~
{: .bash}
~~~
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDl1SraFqE343Qi0sP1h07DSVPd1gLC9yja6U6QvLyA/432Dk9bY9rcHA64Mn85z7JWbT5Dzmd66qF8QFc50fsTh3vN7vERLgufc6au1c+PQGBkAOZPBxHYm7gGF0VD/JVWjaJ1YfzBHLgptxRXmr95Sn7bqoCYcvcKJ8YgoitP8qNK0+FAEXzTdUv1vncSETzJI+toWw4vc6w/R388QgTRjz6L6LJX4h2wtTDIONUweLFpJf+sfAGlFQnrt9j7+eUtHkJugOyxuH/R/UnqMOs+UW9tQDHpAaQr2oyJlBg6zdiJXT51xUS79xzltIYfLZD+1Mvce+SN8leWQ/mbdZgT user01@workshop
~~~
{: .output}

Then copy this and paste it into the text box on the github webpage. Finally click **Add SSH key**.

~~~
$ git push origin master
~~~
{: .bash}
~~~
The authenticity of host 'github.com (140.82.113.3)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
~~~
{: .output}
Then enter `yes` and press enter.
~~~
Enter passphrase for key '/home/user01/.ssh/id_rsa':
~~~
{: .output}
Enter the passphrase for your private key (the one you typed in when you created the keypair).
~~~
Enumerating objects: 104, done.
Counting objects: 100% (104/104), done.
Compressing objects: 100% (103/103), done.
Writing objects: 100% (104/104), 2.54 MiB | 3.65 MiB/s, done.
Total 104 (delta 10), reused 0 (delta 0)
remote: Resolving deltas: 100% (10/10), done.
To github.com:cgeroux/first-jekyll-site.git
 * [new branch]      master -> master
~~~
{: output}

Now lets see the results on github.

Got back to the github website, click on the drop down menu on the top right corner and click "Your repositories". You should see your newly create repository listed there, click on it's name. You should now see a list of all the files we added to our git repository.

To setup our github repository to generate the Jekyll website go to the **Settings** for the repository and click on **Pages** from the left hand menu.

The under the **Source** drop down select, "master". This is the name of the branch that we want to use to generate the site from. Leave the folder as "/(root)" and click **Save**.

It then tells you "Your site is ready to be published at https://cgeroux.github.io/first-jekyll-site/". If you go to that link you will likely see a 404 if you go there right away as it can take a little time for github to generate the site. Try again in a few more seconds.

<!--Ok I can now see my site, but the styling is all messed up, more specifically there is no styling. This is because the configuration we setup for our site on the computer we were using on the Alliance cloud had the site under a sub directory `/<your-user-name>` this is not the case on github. On github it is in a sub directory with the name of the repository `first-jekyll-site` as we can see from the URL above. We can fix this by editing our _config.yml file and setting the `baseurl` to "first-jekyll-site".

After this change, add the modified files to the local git repository and commit the changes.

~~~
$ git add -u
$ git commit
~~~
{: .bash}

Add the commit message "Fixed baseurl for github", then press `ctrl`+`x`, followed by 'y' and enter to save the message. Then push this change up to github
~~~
$ git push origin master
~~~
{: .bash}
Check back on the github website to see if our commit shows up. Again it will take github a few seconds to render your new site so it might not show up right away. When github is done rendering your new site a green check mark will show up next to the most recent commit. At the point go checkout your updated site. -->
