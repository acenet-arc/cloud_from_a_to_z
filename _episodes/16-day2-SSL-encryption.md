---
layout: episode
title: "Create a Self-Signed SSL Certificate"
teaching: 20
exercises: 0
questions:
- "What is a Self-Signed SSL Certificate?"
- "How can we create one?"
- "What is a Trusted Certificate Authority?"
- "What is a Diffie-Hellman group?"
- "How do we configure Apache to use our certificate?"
- "How do we test to ensure that encryption is working?"
objectives:
- "Create a self-signed SSL certificate."
- "Create a Diffie-Hellman group"
- "Configure Apache to use this certificate."
- "Verify that encryption works."
- "Create a permanent redirect."
keypoints:
- ""
---
In this episode we'll create a self-signed SSL certificate to use with our Apache server in order to secure communication with our WordPress application. SSL stands for Secure Sockets Layer. It has recently been replaced by Transport Layer Security (TLS). However, during this course, we'll still refer to it as SSL, as this seems to be the acronym that is referenced most frequently in most documentation.

The purpose of using SSL certificates is as follows:
- the connection uses symmetric cryptography to encrypt all transmitted data  
- use of trusted cryptographic keys ensures that the identity of the web server can be authenticated
- since each message includes a message authentication code, the connection can ensure data integrity (ie. there has been no loss or alteration of data)

There are two methods of creating SSL certificates. You can pay to purchase one that will be signed by a trusted certificate authority, such as GoDaddy, Symantec, Verizon, DigiCert, etc. Or you can create your own self-signed SSL certificate. While both types of certificates will encrypt communication between our web browsers and the WordPress server, self-signed certificates cannot be used to validate the identity of our web servers. For this reason, in production environments, it is recommended that you purchase digital certificates from a trusted certification authority. Even so, for the purposes of this course, a self-signed certificate will suffice. Self-signed certificates are still very useful for working with applications in a development, test, or educational environment (like this course, for example) -- or for any situation in which it is too cost prohibitive to purchase trusted certificates. Self-signed SSL certificates will still encrypt network traffic when users or administrators log into WordPress using password authentication in order to create and maintain content, as well as modify configuration settings. Naturally, this is communication that we *REALLY* don't want to be transmitting across the wide-open Internet in plain text.


## Creating the SSL certificate
Before we can create our certificate, we need to make certain that the OpenSSL package is installed. It should already be there but, in case that it is missing, please perform the following:  

~~~
$ apt update
$ apt install openssl
~~~
{: .bash}

TLS/SSL works by using both a public certificate (which we share) and a private key (which is kept secret at all times and remains on the server). Basically, the certificate is shared with any user who requests content from our web site and it is used to decrypt each transmission which had already been encrypted by the private key.

The process is as follows:  
- we will issue a command to create the certificate/private key
- then we will be asked a series of questions which help to identify our web site

The command looks like this:  
~~~
$ sudo openssl req -x509 -nodes \
  -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/apache-selfsigned.key \
  -out /etc/ssl/certs/apache-selfsigned.crt
~~~
{: .bash}

Before considering any output, let's go over what that command really does. First, you are executing both `sudo` and `openssl` to invoke administrator access and create the SSL certificate and private key. However, the command itself requires a lot more information, such as:  

- `req`: We would like to use the X.509 certificate standard.
- `x509`: We want to make a self-signed certificate, so please don't bother generating certificate signing request.
- `-nodes`: Please skip the option to secure this certificate with a passphrase.
- `-days 365`: Please keep this certificate valid for 1 year.
- `-newkey rsa:2048`: Please create a secret key at the same time. Please make it an RSA key that is 2048 bits strong.
- `-keyout`: This is the file path in which to store our new secret private key.
- `-out`: This is the file path in which to store our new SSL certificate.  

Now to deal with the series of questions that help to identify our web site.  

You will first be prompted to identify your location information, such as Country, State or Province, and City.

~~~
Generating a 2048 bit RSA private key
................................................................+++
..........+++
writing new private key to '/etc/ssl/private/apache-selfsigned.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CA
State or Province Name (full name) [Some-State]:British Columbia
Locality Name (eg, city) []:Vancouver
~~~
{: .bash}

Next, you will be asked to provide some information about your organization or place of employment.  

~~~
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Province University
Organizational Unit Name (eg, section) []:Research Computing
~~~
{: .bash}

Finally, you will be asked to provide information about your server. NOTE: for `Common Name`, you can just provide the external IP address of your virtual machine.

~~~
Common Name (e.g. server FQDN or YOUR name) []:206.167.181.126
Email Address []:admin@fake.org
~~~
{: .bash}

And that's it. You can verify the creation of your private key as follows:

~~~
$ $ sudo ls -l /etc/ssl/private/
~~~
{: .bash}  

~~~
-rw-r--r-- 1 root root     1708 May  4 19:45 apache-selfsigned.key
~~~
{: .output}

You can also verify the creation of your public SSL certificate:  

~~~
$ ls -ltr /etc/ssl/certs/
~~~
{: .bash}  

~~~
...
whole bunch of other certificate files ...
...
-rw-r--r-- 1 root root   1501 May  4 19:45 apache-selfsigned.crt
~~~
{: .output}


## Creating a Diffie-Hellman group

At the same time, we should also create what's called a Diffie-Hellman group. What is that? Good question.  

Diffie-Hellman groups determine the strength of the key that is used during an encryption key exchange process. There is a trade off. Higher group numbers are more secure but they require longer duration to compute the key. As a consequence, we'll create one that will match the strength of the RSA private key that we created in the previous section. Please note, this will take more than a few moments.

~~~
$ sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
~~~
{: .bash}  

~~~
Generating DH parameters, 2048 bit long safe prime, generator 2
This is going to take a long time
................................................................
.......................+......................................+.
[and so on for more than a screen length...]
......................+......................................^C
~~~
{: .output}  

After the command has completed, your stong DH group file will be stored here:

`/etc/ssl/certs/dhparam.pem`

We will reference this file path in the very next section.


## Configure Apache to use the certificate


## Verifying that encryption works


## Creating a permanent redirect
