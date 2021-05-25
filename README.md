Here is a another lesson I found from the SWC site about using Jekyll:

https://carpentries-incubator.github.io/jekyll-pages-novice/

To deploy on webserver with apache2 installed:

first follow the setup here:
https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/

on the webserver then run:

```bash
sudo bundle exec jekyll build --destination /var/www/html
```

Content which could be added if time permits:
Data transfer tools:
* rsync
* scp
* sshfs
* Owncloud (client, cadaver,davfs2)
* Globus
* Load balancer only at east cloud as of May 4th 2017


