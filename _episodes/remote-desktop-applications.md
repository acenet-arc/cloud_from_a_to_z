---
layout: episode
title: "Remote Desktop Applications"
teaching: 20
exercises: 15
questions:
- "What are some programs we can run on our remote desktop?"
objectives:
- "We'll run some programs on our remote desktop"
keypoints:
- "There are many programs we can run on our remote desktop"

---

First, a disclaimer: IceWM is a bare bones window manager. The functionality is very
basic. If you want something that is a bit more modern, perhaps check out
`ubuntu-mate-desktop`, or some of the other choices in the Remote Desktop Foundation
section.

## Terminal

The first thing we can do with our remote desktop is open up a terminal -- or many terminals.

In IceWM:

* Right click the desktop and select 'Terminal'

or

* Click on the IceWM menu bar and select `Terminal`

The default terminal that is launched is `xterm`. It is fairly low on features, but will do the trick. (An example of a terminal with a more full feature set is `gnome-terminal`. It depends on a lot of packages though, since it is part of the Gnome desktop environment).

Try right-clicking on a terminal window to get a window to increase the size of the font.

You can use a terminal to start another terminal with a very specific font:

~~~
xterm -fa 'Monospace' -fs 14 &
~~~
{: .bash}

Note that the `&` at the end of that line says
"put the program in the background" -- it allows our original terminal to still
accept commands. A lot of programs can be started from the terminal this way.
It's okay to start a graphical program without the `&`, you just won't have access
to the terminal you started it with (you use Ctrl-Z and `bg` in the terminal to
get your command prompt back, if you need it).

## Editor

There are many choices for editors for Linux systems. Many popular ones don't require
desktops (e.g. `vim`, `nano`, and `emacs`). Others are suitable for use in a
desktop environment.

Many such editors depend on having an entire desktop editor installed (for example `gedit` which comes with Gnome). One that has a very small list of dependencies is `nedit`:

~~~
sudo apt install nedit
~~~
{: .bash}

When installed, we can start nedit from a terminal with:

~~~
nedit &
~~~
{: .bash}

Or if we have a specific file that we want to edit or create, open it with:

~~~
nedit my_file.txt &
~~~
{: .bash}

## Browser

We'll install the firefox browser. You could also install the Google Chrome
browser by going to the Chrome website and downloading the Debian/Ubuntu package
for it.

~~~
sudo apt install firefox
~~~
{: .bash}

Again at the terminal:

~~~
firefox &
~~~
{: .bash}

## R Studio

R is a programming language for doing data science/statistics.

We can install the R language with:

~~~
sudo apt install r-base
~~~
{: .bash}

The R language does not rely on having a desktop environment and runs in
a terminal, simply by typing:

~~~
R
~~~
{: .bash}

We can assign a variable `x` the numbers from 1 through 5 and compute the mean:

~~~
x <- 1:5
mean(x)
~~~
{: .language-r}

(Ctrl-D to quit, don't save the workspace image.)

Many R programmers prefer to work with RStudio, an integrated graphical program
for programming, inspecting and visualizing data.

This program isn't in the main Ubuntu repositories, so we need to download it
directly:

~~~
wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.4.1717-amd64.deb
~~~
{: .bash}

Now that we have the package, we can install it (and it's dependencies) with:

~~~
sudo apt install ./rstudio-1.4.1717-amd64.deb
~~~
{: .bash}

Now at the terminal, start it up:

~~~
rstudio &
~~~
{: .bash}

Try the same short program above in RStudio...

(Note that RStudio appears to work with TigerVNC, but not with some of the
other VNC providers.)

## Ummm, Blender?

Some 3D graphics programs using OpenGL will work through VNC (although this
isn't an ideal way to run them; they work best with specialized graphics
cards on non-virtual desktops).

The follow appears to work with TigerVNC, but not with some of the
other VNC providers.

~~~
sudo apt install blender
~~~
{: .bash}

Start it with:

~~~
blender &
~~~
{: .bash}

