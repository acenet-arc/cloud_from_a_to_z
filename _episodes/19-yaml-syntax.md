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
- "A YAML file can be validated using [yamllint](http://www.yamllint.com/)."
- "White space is important in YAML."
- "Indentation indicates scope."
- "Block notation (indicated with a `|`) is used to preserver newline characters."
start: false
---

Cloud config files are written using YAML which can stand for different things depending on who you ask. The official [YAML website](yaml.org), which is a YAML file its self defines YAML as "YAML Ain't Markup Language", but it has also been referred to as "Yet Another Markup Language" (See this [page](http://yaml.org/spec/history/2001-08-01.html) on the official YAML website). So weather YAML is a markup language or not is up for debate. At this point I am not sure we are much closer to actually understanding what YAML is or isn't, so lets try again. YAML is a method for organizing and storing data in a human readable format and is commonly used for configuration files.

YAML provides a way to map between keys and values. This is useful for example if you want to specify a parameter name and a value for it.
~~~
day: Wednesday
~~~
{: .YAML}
The `:` is used to map the key `day` onto the value `Wednesday`. Note that there is a space between the `:` and the value. YAML is very picky about white space (spaces, tabs, etc.). To verify that you have written correct YAML you can use the **[yamllint](http://www.yamllint.com/)** website by copying and pasting your YAML into the text box and clicking *Go*. It is always a good idea to verify that your cloud config file is valid YAML before launching a VM with it as it is much faster to validate a YAML file that it is to wait for a VM to provide error messages about poorly formated YAML files.

It is also possible to put comments in YAML files as with Bash files they use a `#` to indicate the start of a comment.
~~~
day: Wednesday # which day to teach basics of YAML
~~~
{: .YAML}

You can also specify sequences with `-` again there must be a space between the `-` and the item in the sequence.
~~~
- Bob
- John
- Mark
~~~
{: .YAML}

You can also map a key to a sequence.
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

Note that the sequence is indented under the key to indicate that all the elements in the sequence are mapped to that key, or in other words, are within the scope of that key.

YAML also supports **block notation** where newlines are preserved and the content is considered as one solid block.
~~~
abstract: |
  This is my abstract which has
  many lines which I would like
  to keep as they are.
~~~
{: .YAML}

There is quite a bit more to YAML which you can learn about on the official YAML [specification page](http://www.yaml.org/spec/1.2/spec.html) however, at this point we now know enough YAML to understand at least the formating and syntax of the cloud config file. The specific keys, values and sequences in a cloud config file have special meaning to cloud-init so while YAML only specifies the format of the data cloud-init indicates what the data needs to be to tell cloud-init what you want to it to do.