---
layout: episode
title: "Why static websites?"
teaching: 15
exercises: 0
questions:
- What is a static website?
- What is a dynamic website?
- Why might I want my website to be static?
objectives:
- Understand the differences between static and dynamic sites.
- Know why static websites are more secure and easier to maintain.
- What projects are suitable for static websites.
keypoints:
- Easier to dive into the components making up a site.
- Static websites render faster as code doesn't need to be run first, databases don't need to be queered.
- Easier to backup as static websites are a set of static files that can just be copied.
- Popular static websites have far fewer or no security patches required as compared to dynamic sites.
---

# Why static websites?

First what is a static website? **A static website is a website in which the contents are the same for every visitor to the web-page.** Some examples of static websites created using two popular static website generators:

#### Jekyll
* [IBM Mobile](https://mobilefirstplatform.ibmcloud.com/)
* [US Freedom of Informaiton Act (FOIA)](https://www.foia.gov/)
* [Hildegard](https://hildegard-1877bibliography.ca/)

#### Hugo
* [letsencrypt](https://letsencrypt.org/)
* [aether](https://getaether.net/)

Why would we want a static website rather than an alternative in which the contents can be customized for each visitor? To help understand why we might want a static website lets start with a little web history to put this question into context.

## A little web history
Static websites were the original website in the early days of the web (1990s) and were created from [HTML](https://en.wikipedia.org/wiki/HTML) (Hypertext Markup Language). In the late 1990s [CSS](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) were incorporated into HTML websites to allow web designers to separate the visual style of the website from the HTML tags and text defining the website content. To allow websites to have dynamic elements (e.g. change the appearance of the site based on button clicks etc.) a client side scripting language was developed that could run in web browsers called [JavaScript](https://en.wikipedia.org/wiki/JavaScript). Sites which use JavaScript are still static websites since all the content sent to the site visitor's web browsers is the same for every visitor. **A static website can have dynamic interactions with it's visitors.**

To increase the utility of the web, developers wanted to be able to collect information from site visitors. To be able to do this web servers needed to be able to write data to the server hosting the website. This lead to the development of server-side scripting languages. While a client side scripting language runs in the browser of the visitor to the website, a server-side scripting language runs on the web-server. One very popular server side scripting language is [PHP](https://en.wikipedia.org/wiki/PHP) (PHP: Hypertext Preprocessor). Server-side scripting allowed for the development of a more interactive web, were visitor's of sites participate in the creation of content on these sites, this new style of participatory web is often referred to as [Web 2.0](https://en.wikipedia.org/wiki/Web_2.0). **A dynamic website is one in which the visitors of that site can participate in generating the content of that website.** These systems are often referred to as Content Management Systems **CMS**.

In addition to server-side scripting languages it was found helpful to store user and page data in a database for fast retrieval. One commonly used database software is [MySQL](https://en.wikipedia.org/wiki/MySQL). At this point things have gotten fairly complicated, so lets summarize the components of a modern dynamic website:

* [HTML](https://en.wikipedia.org/wiki/HTML): describes content (text, links, images, etc.) and how it should be displayed.
* [CSS](https://en.wikipedia.org/wiki/CSS): provides styling (color, border style, link styles, element placement, ...).
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript): scripts which run in visitor's web browsers to provide interactiveness.
* [PHP](https://en.wikipedia.org/wiki/PHP): generates HTML (which may contain Javascript and CSS) form scripts and data stored in databases to be viewed by visitors
* [MySQL](https://en.wikipedia.org/wiki/MySQL): database to store information about visitors, pages. Data retrieved by PHP which generates HTML.

## Static websites are simpler
*"Everything should be made as simple as possible, but no simpler"*<br/>
~ Albert Einstein

That is to say, if you can accomplish your goals with a static website rather than a dynamic website, you should definitely use a static website instead.

A static website only involves the first three of the above components (HTML, CSS, and JavaScript), there are no databases or server-side scripts involved in a static site. This may seem that we have only reduced the complexity by 2/5 if we assume that each of the components has the same complexity, but the last two components add disproportionately more complexity. This simplicity means that it is **easier to understand how static websites work**, how to modify and customize them. Possibly even more important is that because there is no server-side scripting or databases involved the amount of work your server needs to do to serve your site to your visitors is much lower. This results in **increased speed** (shorter wait times); visitors don't have to wait for your server to run server-side scripts (which can start to slow with many visitors and lots of complex scripts) or retrieve data from databases. This also means that your site is **more stable and reliable** as there aren't issues with unresponsive databases. It also means it is extremely **easy to backup and migrate your site** to other locations as they are simply a set of plain text files that can be copied around that don't have dependencies on specific versions of software. You can copy them to a folder on your laptop and open the <code>index.html</code> in your web browser and view your site. If on the other hand, you rely on PHP and MySQL, not commonly found on laptops, you would need to install and configure those, upload a dump of your database on your server to the database software on you laptop, configure your site to connect to your local database, and hope that all the software versions and data formats are compatible. That clearly isn't as simple.

## Static websites are safer

We mentioned above that dynamic websites are ones in which the site visitors can participate in creating the site contents. This means that they must necessarily be able to change the website. **Allowing visitors from the web to change your website and your server has inherent security risks**. This requires that very careful consideration be taken to ensure the security of your site.

If we look on [CVEdetails.com](https://www.cvedetails.com) (a site which lists Common Vulnerabilities and Exposures of various software) at some modern website systems we see:

Popular dynamic web site systems:
* [Wordpress](https://www.cvedetails.com/vendor/2337/Wordpress.html): 402 total, 8 in 2023, 9 in 2022, 9 in 2021, 21 in 2020, 23 in 2019, 18 in 2018
* [Drupal](https://www.cvedetails.com/vendor/1367/Drupal.html): 408 total, 9 in 2023, 20 in 2022, 14 in 2021, 11 in 2020, 26 in 2019, 14 in 2018
* [Mediawiki](https://www.cvedetails.com/vendor/2360/Mediawiki.html): 363 total, 38 in 2023, 37 in 2022, 46 in 2021, 39 in 2020, 22 in 2019, 16 in 2018
* [Joomla](https://www.cvedetails.com/vendor/3496/Joomla.html): 485 total, 5 in 2023, 13 in 2022, 28 in 2021, 39 in 2020, 27 in 2019, 24 in 2018

Popular static website systems:
* [Next.js](https://www.cvedetails.com/product/43198/Zeit-Next.js.html?vendor_id=17577): 4 total, 1 in 2020, 2 in 2018, 1 in 2017
* Eleventy: no match found on CVEdetails
* Hugo: no match found on CVEdetails
* [Jekyll](https://www.cvedetails.com/vulnerability-list/vendor_id-19524/product_id-51408/Jekyllrb-Jekyll.html): 1 total in 2018


You will notice that the **popular dynamic websites require fixes for security vulnerabilities anywhere from 3 to 39 times a year**, that means monthly updates are a minimum, and more frequent updates than that would be much better. It should be noted that these vulnerability numbers are only for the core systems and don't include plugins. If you are using plugins, are the teams that created them watching for vulnerabilities and updating them with this kind of frequency? If not you will want to be very careful about using those plugins. There is also often concern that when updating CMS which use plugins for additionally functionality that some incompatibilities will arise, or in order to update you will also need to update some underlying dependent component such as PHP, or MySQL. While updates often do go smoothly, especially on mature dynamic website platforms, it isn't always the case.
