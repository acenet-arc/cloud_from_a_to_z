---
layout: page
title: twitter scraper
permalink: /twitter-scraper/
---

~~~
$ sudo apt-get update
$ sudo apt-cache search pip
$ sudo apt-get install python-pip
$ sudo pip install twarc
~~~
{: .bash}

1. sign up for twitter if you don't have an account
I needed to include a phone number in my profile before 
I could register an app, this involved getting a verification
code via text and entering it on twitter.

2. Register the app with Twitter: [http://apps.twitter.com](http://apps.twitter.com)
When the app is registered go to the "Keys and Access Tokens"  tab and generate an access token. Once this is done note the following:
- Consumer Key (e.g. 6q3avm7iWk9YqGKzWAYWuDJIq)
- Consumer Secret (e.g. hHReWGbOfnYazHlOkJeInR13k1adqRumHaInnVth0on7qJ31LN)
- Access Token (e.g. 567223483-Ew5zX3w4N3t9Cv6YFx1rfgIk4Wkj1r9PzwYPeWKk)
- Access Secret (e.g. LtOtuTNsjQrIlwqLibBRaC0z6WSgkd0Kw0WKD3Mr4mCFH)
- Under the "Permissions" tab set the access to "Read only".

Return to your terminal and run `twarc.py`. On the first run the tool will ask for the keys and secrets generated. Copying and pasting these directly from the twitter page is the best way to pass these.
NOTE: This will produce an error. The tool is complaining because it doesn't have enough information to actually run. This is fine because all we care about is having the tool generate a .twarc file in the home directory and save the keys to that file in the correct format.

OK, look at the Docs for twarc here: [https://github.com/DocNow/twarc](https://github.com/DocNow/twarc)
~~~
$ twarc configure
~~~
{: .bash}

seems to work, get streams of information print to terminal until I hit ctrl+c

~~~
$ mkdir tweets
$ twarc search ponies >tweets/search-ponies.json
$ sudo apt-get install git
$ git clone https://github.com/recrm/ArchiveTools
$ ./ArchiveTools/json-extractor.py -path tweets/ created_at retweet_count favorite_count text
~~~
{: .bash}

this creates a csv file containing the data from the tweet search I did on ponies, pulling out the data the tweet was created and the tweet text.
