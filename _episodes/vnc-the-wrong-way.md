---
layout: episode
title: "VNC, the wrong way"
teaching: 20
exercises: 15
questions:
- "What is the wrong way?"
- "Why is this the wrong way?"
- "How do you open unnecessary ports on a VM?"
- "How do you expose your VNC server to every hacker on the internet?"
objectives:
- "We'll set up (and tear down) a bad approach to VNC"
- "We'll score an easy win, paying through reduced security"
keypoints:
- "We can score an easy win by doing VNC the wrong way (but we shouldn't)"
- "We can expose our VM to unneccessary risk"
- "VNC traffic is not secure by default"
- "Reducing the holes in your firewall enhances security"
- "Binding a server to only accept connections from localhost enhances security"
---

Now that we have a window manager and VNC software installed, we'll try to score an easy win by setting up a VNC server "the wrong way". We'll set it up so that it works, but our set up will have security problems.

In the following section, we'll correct those problems.

## Mistake number 1: opening one too many holes in our firewall

In OpenStack, go to Network->Security Groups

Next to your default security group, select 'Manage Rules'

Click Add Rule.

Under description, you can write 'VNC'. Under port, put '5901'. Under CIDR, put `0.0.0.0/0`.

If a program (like VNC) is running on port `5901` and allows connections from arbitrary IP addresses, anybody on the internet can potentially connect to the VNC server!

## Mistake 2: starting a VNC server so that any host on the internet can connect to it

The command we need to start a VNC server is (surprise) `vncserver`. We can provide an optional argument to the VNC server to specify what display to use (default is `:1`).

```vncserver :1```

(TODO: add information about password)


Now, point your VNC Viewer program on your computer to your VNC server on display `:1`. You'll need your floating IP address (e.g, `206.167.180.170`). E.g., tell your VNC viewer to attach to the server at `206.167.180.170:1`:

``` vncviewer 206.167.180.170:1```

Your VNC program may have options for host, display, or port.

Did it work?

How can we check that the server is even trying to accept connections? There is a utility `lsof` (list open file handles) that can help:

```lsof | grep 5901```

You will see that the VNC is running (listening), but it only allows connections from `localhost` (that is, it will accept connections from itself, but no other addresses on the internet).

This is actually the right way to run a VNC server, because it won't allow possible intruders to connect from the internet! Unfortunately, as a side effect, it won't let us connect either.

Let's kill the VNC server:

```vncserver -kill :1```

Suppose we really did want to connect to our VM from the wider internet. Can you figure out a way to do this by looking at `vnc -help`?

```vncserver -localhost no :1```

Now we can try `lsof | grep 5901` again ... what difference do you see?

Try to connect your VNC viewer again to your IP address (display `:1` or port `5901`). Did it work?

## A working connection ... but at what price?

We now have a working VNC connection (hopefully).
This approach might be fine if we are on a secure private network, but the problem now is that anybody on the internet can also connect to this port on our VM. The intruder probably won't know your password, but there are other ways around ... check out this list of known vulnerabilities with various VNC software:

https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=vnc

This one hits pretty close to home:

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15694

(We can check out our VNC server version with `dpkg -s tigervnc-standalone-server`.)

Worse, VNC doesn't encypt data that it sends or recieves. This means that unscrupulous people may be able to listen to this data and pick up key strokes or pictures of your desktop.

## Let's harden things up

First, let's undo the two mistakes listed above. First, let's kill the VNC server:

```vncserver -kill :1```

Second, let's undo the hole in our firewall.

Do to Network -> Security Groups

Click on 'Manage Rules' for the default security group.

Delete the rule that allows traffic to port 5901.

So now that we've been able to fix things, let's take an alternative strategy to connect to our remote desktop in a secure way.
