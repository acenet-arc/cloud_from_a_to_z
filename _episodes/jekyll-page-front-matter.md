---
layout: episode
title: "Page front matter"
teaching: 15
exercises: 15
questions:
- How does Jekyll know a file should be processed?
- How does Jekyll know how it should process a file?
- Can files in the source directory be omitted from the generated site?
objectives:
keypoints:
start: false
---

When we ran the `jekyll build -d /var/www/html/<your-username>` command it looks at the files in the current working directory and uses them to generate your site. Different files are handled in different ways. For example some files are converted into HTML files while other files are copied as they are. Have a look at our website root directory, where Jekyll generated our site for us, and compare that to our current working directory that Jekyll used as the source to create the site from.

#### Destination directory contents
The `ls` command is used to list the contents of a directory given as an argument to the command. The `ls` command can be used with the `-l` option to get a long listing which including additional information about the files and directories instead of only providing their names. If no argument is given `ls` will list the files and directories inside the current directory.

~~~
$ ls -l /var/www/html/<your-username>
~~~
{: .bash}
~~~
total 84
drwxrwxr-x 3 user01 user01  4096 Sep 20 20:07 2016
-rw-rw-r-- 1 user01 user01  5248 Sep 21 16:51 404.html
-rw-rw-r-- 1 user01 user01 15914 Sep 21 16:51 all_posts.html
drwxrwxr-x 6 user01 user01  4096 Sep 20 20:07 assets
-rw-rw-r-- 1 user01 user01 20675 Sep 21 16:51 elements.html
-rw-rw-r-- 1 user01 user01  6862 Sep 21 16:51 generic.html
-rw-rw-r-- 1 user01 user01  7412 Sep 21 16:51 index.html
-rw-rw-r-- 1 user01 user01  8939 Sep 21 16:51 landing.html
~~~
{: .output}

#### Source directory contents
~~~
$ pwd
~~~
{: .bash}
~~~
/home/<your-username>/forty-jekyll-theme-master
~~~
{: .output}
~~~
$ ls -l
~~~
{: .bash}
~~~
total 100
-rw-rw-r-- 1 user01 user01    68 Sep  2 03:50 404.md
-rw-rw-r-- 1 user01 user01   693 Sep  2 03:50 CONTRIBUTING.md
-rw-rw-r-- 1 user01 user01   120 Sep  2 03:50 Gemfile
-rw-rw-r-- 1 user01 user01  1656 Sep 20 20:07 Gemfile.lock
-rw-rw-r-- 1 user01 user01 17065 Sep  2 03:50 LICENSE.md
-rw-rw-r-- 1 user01 user01  2939 Sep  2 03:50 README.md
-rw-rw-r-- 1 user01 user01  1144 Sep 20 20:08 _config.yml
drwxrwxr-x 2 user01 user01  4096 Sep  2 03:50 _includes
drwxrwxr-x 2 user01 user01  4096 Sep  2 03:50 _layouts
drwxrwxr-x 2 user01 user01  4096 Sep  2 03:50 _posts
drwxrwxr-x 6 user01 user01  4096 Sep  2 03:50 _sass
-rw-rw-r-- 1 user01 user01   164 Sep  2 03:50 all_posts.md
drwxrwxr-x 6 user01 user01  4096 Sep  2 03:50 assets
-rw-rw-r-- 1 user01 user01 15750 Sep  2 03:50 elements.md
-rw-rw-r-- 1 user01 user01   650 Sep  2 03:50 forty_jekyll_theme.gemspec
-rw-rw-r-- 1 user01 user01  1645 Sep  2 03:50 generic.md
-rw-rw-r-- 1 user01 user01   536 Sep  2 03:50 index.md
-rw-rw-r-- 1 user01 user01  3544 Sep  2 03:50 landing.md
~~~
{: .output}

There are a few differences between the source directory ( and the destination directories. First you might notice that all the directories and files beginning with a `_` have been omitted. This is a feature of Jekyll which allows you to have extra files, like our `_config.yml` which aren't directly part of the generated site but often used in some way to help generate the final site. It also looks like our `Gemfile` and `Gemfile.lock` have been omitted, indicating the Jekyll is aware of these types of files and their purpose. There is also a new `2016` directory in the destination directory, that has to do with how Jekyll handles the `_posts` directory, we will get to that later.

> ## Additional omitted files and directories
> In addition to files and directories beginning with `_`, files and directories beginning with `.`,`#`, and `~` in the source directory are also omitted from the destination.
{: .callout}

Finally many of the `.md` files have been converted to `.html` files, but not all. For example our `index.md` file has been converted into an `index.html` file. However, the `README.md` file has not, why? To find out lets have a look at these two markdown files and compare them.

~~~
$ cat README.md
~~~
{: .bash}
~~~
# Forty - Jekyll Theme

A Jekyll version of the "Forty" theme by [HTML5 UP](https://html5up.net/).

![Forty Theme](assets/images/forty.jpg "Forty Theme")

# How to Use
.
.
.
~~~
{: .output}
~~~
$ cat index.md
~~~
{: .bash}
~~~
---
layout: home
title: Home
landing-title: 'Hi, my name is Forty'
description: null
image: null
author: null
show_tile: false
---

Nullam et orci eu lorem consequat tincidunt vivamus et sagittis libero. Mauris aliquet magna magna sed nunc rhoncus pharetra. Pellentesque condimentum sem. In efficitur ligula tate urna. Maecenas laoreet massa vel lacinia pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis libero. Mauris aliquet magna magna sed nunc rhoncus amet pharetra et feugiat tempus.

~~~
{: .output}

You will notice that the file that was converted to an HTML file contains a special section at the top of it between two sets of triple dashes, `---`. This is called **front matter** and is actually written in the same YAML syntax we saw in the `_config.yml` file. Front matter tells Jekyll how we want it to process the file. Files which don't contain this front matter receive no special processing from Jekyll. Files that don't contain this front matter are copied as they are to your destination directory and are referred to as **static files** because they aren't modified by Jekyll when generating your site. Front matter must be at the very beginning of the file and have these two sets of triple dashes for Jekyll to recognize that the file needs special processing. The key-values pairs are optional.

The key values pairs in the front matter tell Jekyll how to create the HTML page. In this case the `layout` key tells Jekyll to use an HTML template in the `_layouts` directory, called `home.html` as the basis for creating this HTML page. The other keys and values are used within this template to customize how it is displayed.

Below the front matter is the main content of the page, written in markdown syntax. Template files often contain a section for this main content which is converted by Jekyll from markdown to HTML and placed at the location in the page specified by the HTML template.

Lets try changing the `landing-title` and the main content of this file and rebuild our site and look at the result.
~~~
$ nano index.md
~~~
{: .bash}
~~~
---
layout: home
title: Home
landing-title: 'My new site'
description: null
image: null
author: null
show_tile: false
---

Some information I would like people to see.
~~~
{: .output}
Save and exit nano; then run the command to rebuild your site.
~~~
$ jekyll build -d /var/www/html/<your-username>
~~~
{: .bash}
Go back to your browser to view the changes. You will likely need to refresh the page to see them take affect. In many browsers the `F5` keyboard key will do this for you.

![First Jekyll site modified](../fig/first_jekyll_site_modified.png)

You can easily see the result of having changed the `landing-title` key value. However, where is our new content? To see that scroll down the page.

> ## Modifying page front matter
> Open up your site’s `index.md` in nano. Edit the value `show_title` key from `false` to `true`. Then rebuild your site and look at the result in your browser. Remember to refresh your browser either by pressing the F5 key, or reload without using the cache (on Windows: `control`+`shift`+`R` or on Mac: `command`+`shift`+`R`). What did it change?
> 1. Nothing
> 2. Added a new tile
> 3. Generated an error message like:
> > `YAML Exception reading /home/user48/forty-jekyll-theme-master/index.md: (<unknown>): could not find expected ':' while scanning a simple key at line 8 column 1`
> 
> > ## Solution
> > 1. No: it should have added a new tile. Did you get an error message?
> > 2. Yes: it should have added a new tile called "home"
> > 3. No: YAML syntax is a bit picking, you need to have a space between the `:` and the value.
> {: .solution}
{: .challenge}
