---
layout: episode
title: "Graphical User Interfaces for Linux/Unix"
teaching: 20
exercises: 15
questions:
- "What is a remote desktop?"
- "What is X11"
- "What is VNC?"
- "What is X2Go"
- "What is a window manager?"
- "What is a desktop environment?"
- "What kinds of software can we use on a remote desktop?"
objectives:
- "Install software for window and desktop management"
- "Install software to connect to a remote desktop"
- "Connect to a VM through remote desktop."
- "Run some applications on a remote desktop"
keypoints:
- "Ubuntu provides packages for a number of remote desktop setups for your VM"

---

## Graphical User Interfaces on Linux/Windows

With operating systems like Windows and Mac, you essentially have one choice for the graphical user interface (GUI) you use to interact with programs on your computer. These user interfaces are professional, good looking, and have an excellent set of features.

In Linux/Unix, you have more options for the graphical user interfaces. Each interface is organized in a few layers (some optional), and each has it's own set of quirks. Some are very professional looking and full featured, whereas others are very minimal.

We will be looking at remote desktops on our VMs (where we operate a graphical user interface on our VM through a window), but it's helpful to understand how these interfaces work.

Let's look at the layers involved in a typical GUI on a Linux/Unix system:

### Display server (e.g., an X server or wayland)
* software that provides a simple graphical user interface to the user
* handles mouse/keyboard and other devices
* handles rendering graphics on the display (this can be a virtual display or a hardware display like a monitor)
* uses a network protocol (X11 in the case of X server) that handles graphic primatives, images, mouse pointer motion, key presses. Note you can run a graphical program on one computer, and have the program show up on another computer.
* we will be looking at VNC (virtual network computer) and X2go as choices for remote desktop, and these act as display servers.

### Windows manager
* software that works with the display server to present applications in one of more windows
* handles things like moving, resizing, maximizing windows
* handles title bars on windows
* uses a "widget toolkit", software for drawing buttons, scrollbars (e.g., GTK)

### Desktop environment
* provides libaries and specifications that applications can use and follow to interact with each other, to give a consistent user interface
* Programs like a login screen and a task bar might be part of a desktop environment
* Copy/paste is often handled here
* Supporting sound and printing might be handled here (at least the GUI parts)
* Control panels for modifying components of the operating system/windowing system can be handed here

## Remote desktop

```
sudo apt-get update
sudo apt-get dist-upgrade

# desktop
sudo apt-get install ??????


sudo apt-get install tightvncserver
# or cinnamon wants...
# sudo apt install tigervnc-standalone-server tigervnc-common
```