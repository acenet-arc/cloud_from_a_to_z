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

When we ran the `jekyll build -d /var/www/html` command it looks at the files in the current working directory and uses them to generate your site. Different files are handled in different ways. For example some files are converted into HTML files while other files are copied as they are. Have a look at our website root directory, where Jekyll generated our site for us, and compare that to our current working directory that Jekyll used as the source to create the site from.

~~~
$ ls -l /var/www/html
~~~
{: .bash}
~~~
total 112
drwxrwxr-x 3 ubuntu ubuntu  4096 Sep 11 19:32 2016
-rw-rw-r-- 1 ubuntu ubuntu  4864 Sep 22 20:21 404.html
-rw-rw-r-- 1 ubuntu ubuntu   693 Jun 27 16:29 CONTRIBUTING.md
-rw-rw-r-- 1 ubuntu ubuntu 17065 Jun 27 16:29 LICENSE.md
-rw-rw-r-- 1 ubuntu ubuntu  2886 Jun 27 16:29 README.md
-rw-rw-r-- 1 ubuntu ubuntu 15488 Sep 22 20:21 all_posts.html
drwxrwxr-x 6 ubuntu ubuntu  4096 Sep 11 19:32 assets
-rw-rw-r-- 1 ubuntu ubuntu 20207 Sep 22 20:21 elements.html
-rw-rw-r-- 1 ubuntu ubuntu   650 Jun 27 16:29 forty_jekyll_theme.gemspec
-rw-rw-r-- 1 ubuntu ubuntu  6471 Sep 22 20:21 generic.html
-rw-rw-r-- 1 ubuntu ubuntu  6901 Sep 22 20:21 index.html
-rw-rw-r-- 1 ubuntu ubuntu  8527 Sep 22 20:21 landing.html

~~~
{: .output}

~~~
$ pwd
~~~
{: .bash}
~~~
/home/ubuntu/forty-jekyll-theme-master
~~~
{: .output}
~~~
$ ls -l
~~~
{: .bash}
~~~
-rw-rw-r-- 1 ubuntu ubuntu    68 Jun 27 16:29 404.md
-rw-rw-r-- 1 ubuntu ubuntu   693 Jun 27 16:29 CONTRIBUTING.md
-rw-rw-r-- 1 ubuntu ubuntu    38 Jun 27 16:29 Gemfile
-rw-rw-r-- 1 ubuntu ubuntu  1646 Sep 11 19:00 Gemfile.lock
-rw-rw-r-- 1 ubuntu ubuntu 17065 Jun 27 16:29 LICENSE.md
-rw-rw-r-- 1 ubuntu ubuntu  2886 Jun 27 16:29 README.md
-rw-rw-r-- 1 ubuntu ubuntu   922 Sep 11 18:58 _config.yml
drwxrwxr-x 2 ubuntu ubuntu  4096 Jun 27 16:29 _includes
drwxrwxr-x 2 ubuntu ubuntu  4096 Jun 27 16:29 _layouts
drwxrwxr-x 2 ubuntu ubuntu  4096 Jun 27 16:29 _posts
drwxrwxr-x 6 ubuntu ubuntu  4096 Jun 27 16:29 _sass
-rw-rw-r-- 1 ubuntu ubuntu   164 Jun 27 16:29 all_posts.md
drwxrwxr-x 6 ubuntu ubuntu  4096 Jun 27 16:29 assets
-rw-rw-r-- 1 ubuntu ubuntu 15719 Jun 27 16:29 elements.md
-rw-rw-r-- 1 ubuntu ubuntu   650 Jun 27 16:29 forty_jekyll_theme.gemspec
-rw-rw-r-- 1 ubuntu ubuntu  1645 Jun 27 16:29 generic.md
-rw-rw-r-- 1 ubuntu ubuntu   536 Jun 27 16:29 index.md
-rw-rw-r-- 1 ubuntu ubuntu  3544 Jun 27 16:29 landing.md
~~~
{: .output}

There are a few differences between the source directory and the destination directories. First you might notice that all the directories and files beginning with a `_` have been omitted. This is a feature of Jekyll which allows you to have extra files, like our `_config.yml` which aren't directly part of the generated site but often used in some way to help generate the final site. It also looks like our `Gemfile` and `Gemfile.lock` have been omitted, indicating the Jekyll is aware of these types of files and their purpose. There is also a new `2016` directory in the destination directory, that has to do with how Jekyll handles the `_posts` directory, we will get to that later.

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

You will notice that the file that was converted to an HTML file contains a special section at the top of it between two sets of triple dashes, `---`. This is called **front matter** and is actually written in the same YAML syntax we saw in the `_config.yml` file. Front matter tells Jekyll how we want it to process the file. Files which don't contain this front matter receive no special processing from Jekyll. Files that don't contain this front matter that are copied as is to your destination site are refered to as **static files** because the aren't modified or changed by Jekyll when generating your site. Front matter must be at the very beginning of the file and have these two sets of triple dashes in order for Jekyll to recognize this file and needing special processing. The key-values pairs are optional.

The key values pairs tell Jekyll how to create the HTML page. In this case the `layout` key tells Jekyll to use an HTML template in the `_layouts` directory, called `home.html` as the basis for creating this HTML page. The other keys and values are used within this template to customize how it is displayed. Below the front matter is the main content of the page, written in markdown syntax. Template files often contain a section for this main content which is converted by Jekyll from markdown to HTML and placed at the location specified in the HTML template.

Lets try changing the title and the main content of this file and rebuild our site and look at the result.
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
$ jekyll build -d /var/www/html
~~~
{: .bash}
Go back to your browser to view the changes. You will likely need to refresh the page to see them take affect. In many browsers the `F5` keyboard key will do this for you.

![First Jekyll site modified](../fig/first_jekyll_site_modified.png)

You can easily see the result of having changed the `landing-title` key value. However, where is our new content? To see that scroll down the page.
