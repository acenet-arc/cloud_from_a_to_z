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
- "We can expose our VM to unnecessary risk"
- "VNC traffic is not secure by default"
- "Reducing the holes in your firewall enhances security"
- "Binding a server to only accept connections from localhost enhances security"
---

Now that we have a window manager and VNC software installed, we'll try to score an easy win by setting up a VNC server "the wrong way". We'll set it up so that it works, but our set up will have security problems.

In the following section, we'll correct those problems.

> ## Mistake number 1: opening one too many holes in our firewall
{: .error}

In OpenStack:

* go to Network->Security Groups
* Next to your default security group, select 'Manage Rules'
* Click Add Rule.
  * Under description, you can write `'VNC'`.
  * Under port, put `5901`.
  * Under CIDR, put `0.0.0.0/0`.

If a program (like VNC) is running on port `5901` and allows connections from arbitrary IP addresses, anybody on the internet can potentially connect to the VNC server!

> ## Open ports
>
> Each time you open a port in your firewall, you open another potential
> hole for intruders to come it to your system.
{: .callout}

> ## Mistake 2: starting a VNC server so that any host on the internet can connect to it
{: .error}

The command we need to start a VNC server is (surprise) `vncserver`. We can provide an optional argument to the VNC server to specify what display to use (default is `:1`, which listens for connections to port `5901`).

~~~
$ vncserver :1
~~~
{: .bash}

Since this is the first time you have run `vncserver`, the server asks you to put
in a password (twice). This password will allow users to access the VNC server
remotely. A hashed version of the password is stored in the file `~/.vnc/passwd`.

When asked about adding a "view-only password", press `n` (no).

Now, point your VNC Viewer program on your computer to your VNC server on display `:1`. You'll need your VM's floating IP address (e.g, `206.167.180.170`). E.g., tell your VNC viewer to attach to the server at `206.167.180.170:1`. For example, on Linux you can run:

~~~
$ vncviewer <ip-of-your-VM>:1
~~~
{: .bash}

Your VNC program may have separate options for host, display, or port.

> ## Question
>
> Did it work?
> > ## Answer
> >
> > No, it did not work.
> {: .solution}
{: .challenge}

How can we check that the server is even trying to accept connections?

There is a utility `lsof` (list open file handles) that can help:

~~~
$ lsof | grep 5901
~~~
{: .bash}

You will see that the VNC server is running (listening), but it only allows
connections from `localhost` (that is, it will accept network connections from itself,
but not from other addresses on the internet).

> This is actually the right way to run a VNC server, because it won't
> allow possible intruders to connect from the internet! Unfortunately,
> as a side effect, it won't let us connect either!
{: .callout}

Let's kill the VNC server:

~~~
$ vncserver -kill :1
~~~
{: .bash}

> ## Question
>
> Suppose we really did want to connect to our VM from the wider internet.
> Can you figure out a way to do this by looking at `vncserver -help`?
> Restart the server using what you have learned.
> > ## Solution
> >
> > There is an option `-localhost` that takes values `yes` or `no`.
> >
> > `yes` is the default option, which is why we couldn't connect
> > before to the VNC server.
> >
> > Let's restart the VNC server with:
> > ~~~
> > $ vncserver -localhost no :1
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

Check the solution above to start up the vncserver so that it allows
connections from arbitrary addresses on the internet.

> ## Question
> Now we can try `lsof | grep 5901` again ... what difference do you see?
>
> > ## Solution
> >
> > We now see a bunch of lines of the form `*.5901`. This means
> > That our VNC server is accepting connections from arbitrary
> > addresses from the internet
> {: .solution}
{: .challenge}

Try to connect your VNC viewer again to your IP address (display `:1` or port `5901`).

> ## Question
> Did it work?
{: .challenge}

## A working connection ... but at what price?

We now have a working VNC connection (hopefully).
This approach might be fine if we are on a secure private network, but the problem now is that anybody on the internet can also connect to this port on our VM. The intruder probably won't know your password, but there are other ways around ... check out this list of known vulnerabilities with various VNC software:

<https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=vnc>

This one hits pretty close to home:

<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15694>

> ## Question: Are we vulnerable?
>
> We can check out our VNC server version with
> ~~~
> $ dpkg -s tigervnc-standalone-server
> ~~~
> {: .bash}
>
> Does our version match the version in the above security alert?
{: .challenge}

> ## Unencrypted!
>
> Worse, VNC by default doesn't encrypt data that it sends or receives.
> This means that unscrupulous people may be able to listen to this data
> and pick up key strokes or pictures of your desktop.
{: .callout}

## Let's harden things up

First, let's undo the two mistakes listed above. First, let's kill the VNC server:

~~~
$ vncserver -kill :1
~~~
{: .bash}

Second, let's undo the hole in our firewall:

* Go to Network -> Security Groups
* Click on 'Manage Rules' for the default security group.
* Delete the rule that allows traffic to port 5901.

So now that we've been able to fix things, let's take an alternative strategy to connect to our remote desktop in a secure way.
