---
layout: episode
title: "Remote desktop foundation"
teaching: 20
exercises: 15
questions:
- "What is a window manager?"
- "What packages are needed to run a remote desktop?"
- "What VNC packages are there?"
objectives:
- "Explain what a window manager is"
- "Install a window manager"
- "Install VNC packages"
keypoints:
- "There are a lot of choices for window manager to use"
- "There are a lot of choices for VNC server to use"
---

In this section set up the foundations for running a remote desktop.

## Let's install some software!

The first thing we'll want to do is set up a window manager.

With operating systems like Windows and Mac, you essentially have one choice for the graphical user interface (GUI) you use to interact with programs on your computer. These user interfaces are professional, good looking, and have an excellent set of features.

In Linux/Unix, you have more options for the graphical user interfaces, and each has it's advantages and it's own set of quirks. Some are very professional looking and full featured, whereas others are very minimal.

Window managers handle many properties of the look and feel that you will have for your user interface -- quite literally, they are responsible for managing the windows you see in the user interface. There is another term "desktop environment" that is a similar concept, but builds on top of a window manager to support a more integrated approach to a user interface (this includes things like login screens, a taskbar, handling sound and printing, control panels, etc.). The dividing line between what is a window manager and what is a desktop environment can be a bit blurry.

There are many choices for window manager/desktop environments for ubuntu/linux. You can check some out in [this article](https://linuxconfig.org/8-best-ubuntu-desktop-environments-18-04-bionic-beaver-linux).

Some choices for Ubuntu packages are here:

* `ubuntu-unity-desktop`
* `ubuntu-mate-desktop`
* `lubuntu-desktop`
* `xubuntu-desktop`
* `xfce4`
* `ubuntu-desktop`
* `kde-plasma-desktop`
* `ubuntu-desktop-minimal`
* `cinnamon`
* `icewm`

Some of these extend or modify the other ones. For example, `xubuntu-desktop` is an extention of `xfce4`.

When installing some of these packages, sometimes over 1500 additional packages may need to get installed, taking up several gigabytes of disk. The download and install process can take up as much as 30 minutes. This won't work out in a workshop setting!

We will look at a very minimal desktop today (`icewm`), which installs in only a minute or two, but you are encouraged to try out some of the other choices on your own time -- the nice thing about the cloud is that you can can spin up a VM, install a desktop environment, try it out, through the VM away, and repeat!

Here we go, we'll time how long it takes to install `icewm` as we install it:

```time sudo apt install -y icewm```

How long did it take to install on your VM?

### Okay, so what?

Well, now we have a desktop environment/window manager. How do we connect to it? We'll install a VNC (Virtual Network Computing) remote desktop to connect to this desktop.

Linux is about choice. As we saw there were many choices for window manager. It turns out that there are many different choices for VNC servers as well. Here's a command that is useful for finding all packages related to `vnc`:

```apt-cache search vnc```

Wow, what a list!

If we are only interested in servers, can you think of a way to filter this list?

```apt-cache search vnc | grep server```

The server package that we will install is `tigervnc-standalone-server`. We will also grab the `tigervnc-common` package.

```sudo apt install -y tigervnc-common tigervnc-standalone-server```

The TigerVNC server appears to handle many software packages (even ones that do 3D rendering).

We can checkout some defaults that are configured for our system:

```update-alternatives --get-selections`

We hopefully see the lines:

```vncserver                      auto     /usr/bin/tigervncserver```

and

```x-session-manager              auto     /usr/bin/icewm-session```

