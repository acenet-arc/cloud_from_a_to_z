---
layout: episode
title: "VNC viewer"
teaching: 20
exercises: 15
questions:
- "What software do you need on your machine to connect to VNC?"
objectives:
- "Install the TigerVNC client (viewer) packages"
keypoints:
- "TigerVNC viewers are available for many popular platforms"
---

We have installed a window manager and VNC software on the remote VM.
Now we need to install software on our local machine (laptop/desktop) to connect
to the VNC server running on the VM.

We'll be installing TigerVNC, which has packages for Windows, Mac OSX, and Linux.

## Windows

The first thing we need to do is checkout the releases on the tigervnc
GitHub page and find the highest version that is not 'Beta':

<https://github.com/TigerVNC/tigervnc/releases>

You will find a link to SourceForge for downloading that version for various
platforms (e.g., for Windows, the version should look similar to
`vncviewer64-1.11.0.exe`).

Install from the downloaded file.

## Mac OSX

Similar to Windows above, we need to do is checkout the releases on the tigervnc
GitHub page and find the highest version that is not 'Beta':

<https://github.com/TigerVNC/tigervnc/releases>

You will find a link to SourceForge for downloading that version for various
platforms (e.g., for Mac, the version should look similar to
`TigerVNC-1.11.0.dmg`).

Install from the downloaded file.

## Linux

The package manager that comes with your flavour of Linux should be able to
install a package for you, e.g.,

|Linux Version           | Install Command                      |
|------------------------|--------------------------------------|
|Debian, Ubuntu          | sudo apt-get install tigervnc-viewer |
|Fedora, CentOS, or RHEL | sudo yum install tigervnc            |
|Gentoo                  | emerge -av net-misc/tigervnc         |
