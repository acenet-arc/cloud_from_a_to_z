---
layout: episode
title: "Create a Self-Signed SSL Certificate"
teaching: 15
exercises: 0
questions:
- "What is a Self-Signed SSL Certificate?"
- "How can we create one?"
- "What is a Trusted Certificate Authority?"
- "How do we configure Apache to use our certificate?"
- "How do we test to ensure that encryption is working?"
objectives:
- "Create a self-signed SSL certificate."
- "Configure Apache to use this certificate."
- "Verify that encryption works."
- "Create a permanent redirect."
keypoints:
- ""
---
In this episode we'll create a self-signed SSL certificate to use with our Apache server in order to secure communication with our WordPress application. SSL stands for Secure Sockets Layer. It has recently been replaced by Transport Layer Security (TLS). However, during this course, we'll still refer to it as SSL, as this seems to be the acronym that is referenced most frequently in current documentation.

The purpose of using SSL certificates is as follows:
- the connection uses symmetric cryptography to encrypt all transmitted data  
- use of trusted cryptographic keys ensures that the identity of the web server can be authenticated
- since each message includes a message authentication code, the connection can ensure data integrity (ie. there has been no loss or alteration of data)

There are two methods of creating SSL certificates. You can pay to purchase one that will be signed by a trusted certificate authority, such as GoDaddy, Symantec, Verizon, DigiCert, etc. Or you can create your own self-signed SSL certificate. While both types of certificates will encrypt communication between our web browsers and the WordPress server, self-signed certificates cannot be used to validate the identity of our web servers. For this reason, in production environments, it is recommended that you purchase digital certificates from a trusted certification authority. Even so, for the purposes of this course, a self-signed certificate will suffice. Self-signed certificates are still very useful for working with applications in a development, test, or educational environment (like this course, for example) -- or for any situation in which it is too cost prohibitive to purchase trusted certificates. Self-signed SSL certificates will still encrypt network traffic when users or administrators log into WordPress using password authentication in order to create and maintain content, as well as modify configuration settings. Naturally, this is communication that we *REALLY* don't want to be transmitting across the wide-open Internet in plain text.


## Creating the SSL certificate


## Configure Apache to use the certificate


## Verifying that encryption works


## Creating a permanent redirect
