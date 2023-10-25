---
layout: episode
title: "VNC through a tunnel"
teaching: 20
exercises: 15
questions:
- "What is an SSH tunnel?"
- "What problems are solved by using a tunnel?"
objectives:
- "We'll set up a good approach to VNC"
keypoints:
- "We can set up a secure VNC connection with an SSH tunnel"
- "All of our SSH traffic goes through port 22"
- "Traffic to our VNC server is encrypted"
- "Our VNC server only accepts connections from localhost"
---

## A tunnel?

The [Concordia University School of Engineering](https://www.concordia.ca/ginacody/aits/support/faq/ssh-tunnel.html) has a nice, concise description of
what an SSH tunnel is:

> SSH tunneling, or SSH port forwarding, is a method of transporting arbitrary data over an encrypted SSH connection. SSH tunnels allow connections made to a local port (that is, to a port on your own desktop) to be forwarded to a remote machine via a secure channel.

Our goal will be to trick our computer to take connections to port `5901` or our
own computer and send the to port `5901` of our cloud VM. Better yet: all of the traffic
goes through the standard SSH port (`22`), so we don't need to open any more
holes in our firewall.

How do we do this?

~~~
$ ssh -L 5901:localhost:5901 ubuntu@<IP for VM>
~~~
{: .bash}

> ## Try it!
>
> Our tunnel is open as long as we are connected to our machine through SSH
{: .callout}

The above is actually shorthand for: `ssh -L localhost:5901:localhost:5901 ubuntu@<IP for VM>`

Translation: 'When we send/receive data to/from port 5901 on our local machine, send it to our cloud VM through the SSH port (22), and send/receive the data to/from port 5901 there (to localhost on the cloud VM).'

There are many different ways we can set up tunnels for various applications.
From the man page for ssh:

~~~
     -L [bind_address:]port:host:hostport
     -L [bind_address:]port:remote_socket
     -L local_socket:host:hostport
     -L local_socket:remote_socket
             Specifies that connections to the given TCP port or Unix socket
             on the local (client) host are to be forwarded to the given host
             and port, or Unix socket, on the remote side.  This works by al‐
             locating a socket to listen to either a TCP port on the local
             side, optionally bound to the specified bind_address, or to a
             Unix socket.  Whenever a connection is made to the local port or
             socket, the connection is forwarded over the secure channel, and
             a connection is made to either host port hostport, or the Unix
             socket remote_socket, from the remote machine.

~~~
{: .output}

Lets also restart our vncserver 

~~~
$ vncserver :1
~~~
{: .bash}

In a separate local terminal we can tell our VNC client/viewer to connect to display `:1` of
our local machine, e.g., on Linux:

~~~
$ vncviewer :1
~~~
{: .bash}

(On other systems, you will want to tell the VNC client to connect to display `:1`,
but possible leave the host blank, or set it to `localhost` or `127.0.0.1`.)

## What have we done?

We now have a connection to our VNC server on our remote VM with the following
properties:

* We did not need to open additional holes in our firewall
* We did not need to run our VNC server so that it accepts connections
  from arbitrary internet addresses.

This is exactly where we want to be; we have the secure remote desktop we want.

In the next section we'll discuss some things we can do with our
remote desktop.

> ## A trick! (Optional!)
>
> The ports on the localhost and the remote VM do not have to be the same!
> For example:
>
> ~~~
> ssh -L 5908:localhost:5901 ubuntu@<IP for VM>
> ~~~
> {: .bash}
>
> Translation: 'When we send/receive data to/from port 5908 on our local machine, send it to our cloud VM through the SSH port (22), and send/receive the data to/from port 5901 there (to localhost on the cloud VM).'
>
> We can now connect to the VNC server, pretending it's on display `:8` of our local
machine:
>
> ~~~
> vncviewer :8
> ~~~
> {: .bash}
{: .callout}
