---
layout: episode
title: "YAML"
teaching: 15
exercises: 0
questions:
- "What is YAML?"
- "How do you create a YAML file?"
- "How can a YAML file be validated?"
objectives:
- "Gain exposure to some of the syntax of YAML."
- "Write some (hopefully) valid YAML and validate it."
keypoints:
- "YAML is a format to store data in a way that is human readable."
- "A YAML file can be validated using **[yamllint](http://www.yamllint.com/)**."
- "White space is important in YAML."
- "Indentation indicates **scope**."
- "**Block notation** (indicated with a `|`) is used to preserver newline characters."
start: false
---

Cloud-config files are written using YAML which can stand for different things depending on who you ask. The official [YAML website](yaml.org), which is a YAML file its self defines YAML as "YAML Ain't Markup Language", but it has also been referred to as "Yet Another Markup Language" (See this [page](http://yaml.org/spec/history/2001-08-01.html) on the official YAML website). So weather YAML is a markup language or not is up for debate. A markup language is set of annotations added to a text which provides extra information about the text (e.g. formating).

At this point I am not sure we are much closer to actually understanding what YAML is or isn't, so lets try again. YAML is a method for organizing and storing data in a human readable format and is commonly used for configuration files. There are a number of different constructs which are possible ways to organize data in a YAML file here we will touch on just a few which are relevant for understanding cloud-config files. If you are familiar with a programing language these constructs often appear to correspond to common programing data structures which gives us some insight into how YAML is used. It is used as a way to store data which could then be read in and stored in these common programming data structures.

YAML provides a way to map between **keys** and **values**. This is useful for example if you want to specify a parameter name and a value for it.
~~~
day0: Wednesday
day1: Thursday
~~~
{: .YAML}
The `:` is used to map the key `day0` onto the value `Wednesday` and similarly for `day1`. Note that there is a space between the `:` and the value. YAML is very picky about white space (spaces, tabs, etc.). To verify that you have written correct YAML you can use the **[yamllint](http://www.yamllint.com/)** website by copying and pasting your YAML into the text box and clicking *Go*. It is always a good idea to verify that your cloud-config file is valid YAML before launching a VM with it as it is much faster to validate a YAML file than it is to wait for a VM to provide error messages about poorly formated YAML files.

It is also possible to put **comments** in YAML files as with Bash files they use a `#` to indicate the start of a comment.
~~~
day0: Wednesday # which day to teach basics of YAML
day1: Thursday
~~~
{: .YAML}
If you are familiar with programming this data structure would correspond to a dictionary in python, or map in C++. The ordering of the key/value pairs is not significant.

You can also specify **sequences** with `-` again there must be a space between the `-` and the item in the sequence.
~~~
- Bob
- John
- Mark
~~~
{: .YAML}
The ordering of items within a sequence is important in so far as the program reading the YAML may behave differently based on what order you specify items in a sequence though doesn't strictly have to. This is different from a set of mappings (or key/value pairs) where the order is not important and the programing reading the YAML should not behave differently based on the order of the mappings. In Python this would correspond to the list data structure, or an array or vector in C++.

You can also map a key to a sequence to help identify that particular sequence.
~~~
names:
  - Bob
  - John
  - Mark
provinces:
  - British Columbia
  - Nova Scotia
  - Ontario
~~~
{: .YAML}

Note that the sequence is indented under the key to indicate that all the elements in the sequence are mapped to that key, or in other words, are within the **scope** of that key.

YAML also supports **block notation** where newlines are preserved and the content is considered as one solid block.
~~~
abstract: |
  This is my abstract which has
  many lines which I would like
  to keep as they are.
~~~
{: .YAML}
In the example above we have a key `abstract` which is mapped on to a value consisting of multiple lines of text with newlines preserved.

You can also have a **sequence of mappings** where each set of mappings corresponds to an item in the sequence
~~~
people:
  - name: Bob
    age: 65
    location: London
  - name: Jeff
    age: 22
    location: Berlin
~~~
In this case each item in the sequence is a "person" with mappings of `name`, `age`, `location`. While the order of items in the sequence of `people` is meaningful, the order of the individual mappings for each person are not.

There is quite a bit more to YAML which you can learn about on the official YAML [specification page](http://www.yaml.org/spec/1.2/spec.html) however, at this point we now know enough YAML to understand at least the formating and syntax of the cloud-config file. The specific keys, values, and sequences in a cloud-config file have special meaning to cloud-init. While YAML specifies the format of the data, cloud-init requires specific data to tell it what you want to it to do. We will look at the specific data which cloud-init understands in the next episode.