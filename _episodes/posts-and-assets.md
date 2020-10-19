---
layout: episode
title: "Posts and assets"
teaching: 15
exercises: 15
questions:
- What is a post and how is it different from a page?
- Can I store images on my VM to use with my site?
- What is the assets directory?
- Where to go to learn more about creating static websites?
objectives:
keypoints:
start: false
---

## A few finishing touches

We learned a lot about markdown, but now that we have an understanding of markdown, lets turn back to our website as a whole and see how our new pages integrates with the site.

If we click on our site title in the top left "Awesome Site" it will take us back to the home page. If we look at the tiles of the other pages we notice that some of the pre-made pages have images as backgrounds, and they also have a sub title or descriptive text displayed. How do they get those? Also if click into one of those pages, the "Generic" page for example, the layout of content looks a bit different. It has more of a left margin than our page does and the header has an underline. Lets exit our nano text editor `^X`, and open it up with the `generic.md` page to see the differences.

~~~
$ nano generic.md
~~~
{: .bash}
~~~
---
layout: post
title: Generic
description: Lorem ipsum dolor est
image: assets/images/pic11.jpg
nav-menu: true
---

Donec eget ex magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque venenatis dolor imperdiet dolor mattis sagittis. Praese ...
~~~
{: .output}

There are a few differences we can notice right away:
1. the layout is `post` rather than `page`
2. there is a `description` key
3. there is an `image` key

Let first try adding a description to our "facts about dogs" page and see what happens. Exit nano and open it again with our page.
~~~
$ nano facts_about_dogs.md
~~~
{: .bash}
Then edit the front matter to include a description.
~~~
--
layout: page
title: Facts about dogs
description: Some Interesting facts, images and videos about dogs
nav-menu: true
---
.
.
.
~~~
{: .output}
Lets save that and refresh our browser on the main page or our site to see the results. We now see our newly added description of our page showing up. What about the image? Lets reuse the image of the dog we added to the page and add an `image` key to the front matter with the URL to the image we selected.
~~~
--
layout: page
title: Facts about dogs
description: Some Interesting facts, images and videos about dogs
image: https://live.staticflickr.com/8624/16540146562_975cfdb11f_b.jpg
nav-menu: true
---
.
.
.
~~~
{: .output}
Again, write out the results with nano and refresh your browser on the front page of your site.
![](../fig/facts_about_dogs_page_tile_image.png)

We now have the descriptive text and the image on the home page tile for our new page, but what about the left margin and the page title underline? If we have a look at our page it is actually still the same. Lets try changing the layout from `page` to `post` and see what happens.
~~~
--
layout: post
title: Facts about dogs
description: Some Interesting facts, images and videos about dogs
image: https://live.staticflickr.com/8624/16540146562_975cfdb11f_b.jpg
nav-menu: true
---
.
.
.
~~~
{: .output}
Now write out the changes and refresh our browser again to see the changes. Great, we now see the left margin space, which I think looks a little nicer, however, we now have our page title "Facts about dogs" with an underline and our header `# Facts about dogs`. Lets remove our header as it is a bit redundant with the `posts` layout. OK, great our page looks pretty good now and is better represented on the home page.

## Posts

What's next? If you have been watching carefully you might be starting to wonder a bit about these "posts" and wondering what they are about. We have just seen that our theme gave us a special layout for posts, which is separate from pages, and also there is a entry for "All posts" in our main site menu at the top right. If we click on that it takes us to a list of pre-made "posts". However, if you scroll all the way through them, you will notice that our "Facts about dogs" page is no where to be found. So it seems that even though our page uses the `post` layout, it still isn't considered a post. So what is considered a post?

Lets exit nano and have a look around our site's source directory to see if we can figure out where these posts are coming form.

~~~
$ ls -l 
~~~
{: .bash}
~~~
-rw-rw-r-- 1 ubuntu ubuntu    68 Jun 27 16:29 404.md
-rw-rw-r-- 1 ubuntu ubuntu   693 Jun 27 16:29 CONTRIBUTING.md
-rw-rw-r-- 1 ubuntu ubuntu    38 Jun 27 16:29 Gemfile
-rw-rw-r-- 1 ubuntu ubuntu  1646 Sep 24 19:11 Gemfile.lock
-rw-rw-r-- 1 ubuntu ubuntu 17065 Jun 27 16:29 LICENSE.md
-rw-rw-r-- 1 ubuntu ubuntu  2886 Jun 27 16:29 README.md
-rw-rw-r-- 1 ubuntu ubuntu   867 Sep 24 20:08 _config.yml
-rw-rw-r-- 1 ubuntu ubuntu   379 Oct  1 17:53 _facts_about_dogs.md
drwxrwxr-x 2 ubuntu ubuntu  4096 Jun 27 16:29 _includes
drwxrwxr-x 3 ubuntu ubuntu  4096 Sep 24 19:16 _layouts
drwxrwxr-x 2 ubuntu ubuntu  4096 Jun 27 16:29 _posts
drwxrwxr-x 6 ubuntu ubuntu  4096 Jun 27 16:29 _sass
drwxrwxr-x 2 ubuntu ubuntu  4096 Sep 28 16:53 _test
-rw-rw-r-- 1 ubuntu ubuntu   164 Jun 27 16:29 all_posts.md
drwxrwxr-x 6 ubuntu ubuntu  4096 Jun 27 16:29 assets
-rw-rw-r-- 1 ubuntu ubuntu 15730 Oct  1 18:06 elements.md
-rw-rw-r-- 1 ubuntu ubuntu  1809 Oct  7 19:39 facts_about_dogs.md
-rw-rw-r-- 1 ubuntu ubuntu   650 Jun 27 16:29 forty_jekyll_theme.gemspec
-rw-rw-r-- 1 ubuntu ubuntu  1645 Jun 27 16:29 generic.md
-rw-rw-r-- 1 ubuntu ubuntu   169 Sep 24 19:20 index.md
-rw-rw-r-- 1 ubuntu ubuntu  3544 Jun 27 16:29 landing.md
~~~
{: .output}
So where might there be something to do with "posts"? Oh look, there is a `_posts` directory, that looks promising; lets have a look in there.
~~~
$ cd _posts
$ ls -l
~~~
{: .bash}
~~~
-rw-rw-r-- 1 ubuntu ubuntu 1636 Jun 27 16:29 2016-8-20-etiam.md
-rw-rw-r-- 1 ubuntu ubuntu 1641 Jun 27 16:29 2016-8-21-consequat.md
-rw-rw-r-- 1 ubuntu ubuntu 1633 Jun 27 16:29 2016-8-22-ipsum.md
-rw-rw-r-- 1 ubuntu ubuntu 1695 Jun 27 16:29 2016-8-23-magna.md
-rw-rw-r-- 1 ubuntu ubuntu 1637 Jun 27 16:29 2016-8-24-tempus.md
-rw-rw-r-- 1 ubuntu ubuntu 1638 Jun 27 16:29 2016-8-25-aliquam.md
~~~
{: .output}
Interesting, we have a list of markdown files with file names containing dates and a name. Interestingly those names look a little bit like the titles for the list of posts we saw in the "All posts" page.

Jekyll has some special support for posts as it is frequently used for blogging. The presence of this special `_posts` folder is part of this extra support and isn't something that our theme supplied, though it did supply the example posts in this folder.

To create a new post you create a new file in the `_posts` folder, however, Jekyll does some special processing of the files in this folder and the filenames of these posts must follow a special format.

~~~
YEAR-MONTH-DAY-title.MARKUP
~~~
{: .code}

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. All posts must begin with front matter. If we wanted our facts about dogs page to show up as a post we would need to put it in the `_posts` folder, so lets do that.

~~~
$ cp ../facts_about_dogs.md ./2020-10-01-facts-about-dogs.md
~~~

So now we have both a page "facts_about_dogs.md" and a post "2020-10-01-facts-about-dogs.md". Typically you wouldn't want to have duplicate content like this but our "Facts about dogs" page will give us something interesting for our post without having to create it from scratch. Lets refresh our browser and have a look at our new post in the "All posts" page from the sites main menu. If you scroll down you will notice that other posts on this page have their image directly under their title. However, our new post doesn't; why? It turns out if you go digging through the theme's `_laouts/allposts.html` file, that it expects images to be part of your site, rather than located on a different site.

# Assets
Lets download the image we use on our "Facts about dogs" page and store it on our site, but first where should we store the image?

Lets have a look at the `generic.md` file again and see where it references the image it uses.
~~~
$ cd ..
$ nano generic.md
~~~
{: .bash}
~~~
---
layout: post
title: Generic
description: Lorem ipsum dolor est
image: assets/images/pic11.jpg
nav-menu: true
---
.
.
.
~~~
{: .output}

So that page is getting the image it is using from the `assets/images` directory. Lets refresh memory of what happens when our site is generated.

* Directories and files beginning with an `_` are ignored by the normal Jekyll processing and are not copied to the site destination directory.
* Files containing front matter are transformed into new files in the destination directory
* Files without front matter that don't begin with an `_` are copied as they are into the same directory structure in destination directory as the source directory.

The assets folder is not prefixed with an `_`, nor is the `images` or the file `pic11.jpg`. However, the image file does not have any front matter, it is a regular image file. So this **static** file is copied over to our destination directory, and placed in the same directory as in the source directory.

So to include our dog image in our live site we must place it somewhere in our source directory and the `assets/images` directory is a good place as it groups it together with the other images already there that we got with our theme. We could of course place it anywhere within our source directory or sub directories within it, but the assets directory is a good convention to stick with for storing 'assets' used by our site. So lets download our image there.

First lets go find the URL of our image. It is stored in our "Facts about dogs" page.
~~~
$ nano facts_about_dogs.md
~~~
{: .bash}
~~~
.
.
.
![Pet Dog](https://live.staticflickr.com/8624/16540146562_975cfdb11f_b.jpg)
"Pet Dog" by sonstroem is licensed with CC BY 2.0. To view a copy of this license, visit https://creativecommons.org/licenses/by/2.0/
.
.
.
~~~
{: .output}
Lets copy the URL and exit nano. Now lets download it. We can use the `wget` command to do this.
~~~
$ wget https://live.staticflickr.com/8624/16540146562_975cfdb11f_b.jpg -O assets/images/dog.jpg
~~~
{: .bash}
The `-O` option (capital oh) tells `wget` where we want the downloaded file to be saved. Lets double check that the file is where we expect it.
~~~
$ ls -l assets/images
~~~
{: .bash}
~~~
-rw-rw-r-- 1 ubuntu ubuntu 589247 Jun 27 16:29 banner.jpg
-rw-rw-r-- 1 ubuntu ubuntu 137084 Feb 24  2019 dog.jpg
-rw-rw-r-- 1 ubuntu ubuntu  62690 Jun 27 16:29 forty.jpg
-rw-rw-r-- 1 ubuntu ubuntu  54651 Jun 27 16:29 pic01.jpg
-rw-rw-r-- 1 ubuntu ubuntu 155987 Jun 27 16:29 pic02.jpg
.
.
.
~~~
{: .output}
There we see our new dog image. Now we can reference it in our post's `image` keys so that it will be properly included in the "All posts" page.
~~~
$ nano _posts/2020-10-07-facts-about-dogs.md
~~~
{: .bash}
~~~
---
layout: post
title: Facts about dogs
description: Some Interesting facts, images and videos about dogs
image: https://live.staticflickr.com/8624/16540146562_975cfdb11f_b.jpg
nav-menu: true
---
.
.
.
~~~
{: .output}
and change it to
~~~
---
layout: post
title: Facts about dogs
description: Some Interesting facts, images and videos about dogs
image: assets/images/dog.jpg
nav-menu: true
---
.
.
.
~~~
{: .output}
Lets write those changes out to the file (`^O`) and exit nano(`^X`) and have a look at the changes to our site.

> ## Uploading files via SFTP
> If you took a picture with your camera and uploaded it to your laptop, or if you created a figure in a graphics tool like [GIMP](https://www.gimp.org/) or [InkScape](https://inkscape.org/), you can upload it to your VM using SFTP. MobaXterm has built in SFTP support, and Mac and Linux operating systems have a built in `sftp` command. If you would like to use a GUI SFTP client, [filezilla](https://filezilla-project.org/) is a good cross platform GUI SFTP client.
{: .callout}

# What next?
We have covered most of the basics of Jekyll which will allow you to create pages, posts, and upload and include your own pictures and videos on your pages. However, there are more advanced topics to learn about which will help you when developing your Jekyll sites. We won't cover them here but I wanted to make you aware of them so you would have some idea of where to look if you wanted to do more.

* **HTML** is used to create the layouts of your theme, to customize your theme you will need to know some HTML at a minimum. A good place to learn about HTML is [w3schools](https://www.w3schools.com/html/).
* **CSS** (Cascading Style Sheets) often the styling in themes is described using CSS. Again [w3schools](https://www.w3schools.com/css/default.asp) has a good tutorial about CSS.
* **JavaScript** is a programming language used to create dynamic elements, such as menus, on your site. [w3schools](https://www.w3schools.com/js/default.asp) has java script covered.

There is also more to learn about Jekyll its self.
* Jekyll uses a templating language called [**Liquid**](https://jekyllrb.com/docs/liquid/), which allows you to reference values, from for example your pages front matter, in your HTML layouts.
* Jekyll also provides the concept of [**Collections**](https://jekyllrb.com/docs/collections/) which allows you to group related content and has some interesting uses when combined with HTML page layouts and the Liquid templating language.
* Finally Jekyll also has support for [**plugins**](https://jekyllrb.com/docs/plugins/), which allow you create or use different types of page generators for example.

#### GitHub can host your jekyll site
[github.com](https://github.com/) is a web platform to host [git](https://git-scm.com/) repositories. Git is a version control software which helps manage different versions of your documents. GitHub offers [GitHub pages](https://pages.github.com/) to host your [jekyll](https://jekyllrb.com/docs/github-pages/) based sites. See this [guide](https://guides.github.com/features/pages/) for more information about creating Jekyll pages on GitHub.
