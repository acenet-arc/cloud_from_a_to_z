---
layout: episode
title: "Introduction to the cloud"
teaching: 30
exercises: 0
questions:
- "What is a cloud?"
- "What does \"virtual\" mean when applied to a computer?"
- "Why use Compute Canada's cloud?"
- "What is OpenStack?"
objectives:
- "To understand common cloud terminology"
- "Get exposure to the various parts of OpenStacks Dashboard"
keypoints:
- "A Keypoint 0"
start: true
start_time: 615
---

## The Internet
To put cloud computing into perspective, lets first take a look at how you use your computer and how it interacts with the Internet.

These days everyone uses a computer connected to the Internet. Being connected to the Internet allows your computer to access multitudes of information, from bus schedules, maps and travel planning, to wikipedia. It also provides entertainment through services like netflix, spotify, and online gaming with other people. But how does this actually work, what is the Internet, and where does this data come from?

![the internet](../fig/the-internet.svg)

The Internet is the world wide interconnection of networks of computers. So what is a network of computers? Many of us have a local network at home and at work. We have a router (often wi-fi) which our computer or computers connect to which routes information from one computer to another. We can communicate between software programs and transfer files between computers on such a network even if they were not connected to the Internet. This is what many of the first networks of computers were like, though using wires instead of wifi, and only allowing sharing of information between local computers, often called a Local Area Network (LAN).

![local network](../fig/local-networks.svg)

How do these computers know where to send data to or where to request it from? They use what is known as Internet Protocol address (IP address). Each device on a network is assigned an IP address. This address is used to route data to the correct device. Within a LAN IP addresses often have the form `192.168.###.###` by convention.

Many of these local area networks exist around the world and the Internet connects these smaller networks together which is where the name Internet comes from, interconnected network (Internet).

![interconnected networks](../fig/interconnected-networks.svg)

To connect your LAN to the rest of the Internet your router is connected to an Internet Service Provider (ISP). Now how does a computer on your network know how to exchange information with a computer on your Neighbour's LAN? Again IP addresses are used. Each LAN connected to the Internet gets a unique IP address. 


> ## How many unique IPs are there?
> IP address are compose of numbers separated by `.` Each number is chosen from the range from 0 to 255, or one of 256 possible numbers. An IP is made up of 4 such numbers  separated by `.`s so all possible combinations of these numbers gives 256<sup>4</sup>=4.294e9 (about 4 billion) possible IP addresses. There are now ~7 billion people in the world and in 2011 we ran out of IPv4 address (e.g. IP address of the form ###.###.###.###). This is why IPv6 address were introduced which provide approximately 3.403e38 unique addresses. However IPv4 addresses are still widely used and very common.
{: .callout}

If your neighbour wanted to share some information with you on a website located on his device with local address `192.168.1.103` how could your computer know to connect to that device to get that information? If you know your neighbour's IP address given to them by their ISP that uniquely identifies their LAN (`206.113.222.122`). But how to route the request for the information on your neighbours website to the local device? Your neighbour must configure their router to forward traffic to the device with local address `192.168.103`, but which traffic? What if your neighbour wanted some information to be routed to one device and other information to be routed to another? The solution to this issue are ports. Different types of information requests are associated with different ports and the local network can be configured to forward requests associated with certain ports to specific devices (known as port forwarding). In the case of a website the convention is to use port 80. You can combine IP address and ports with a `:` for example `206.113.222.122:80` could be entered into your web-browser to access a website on your neighbours device with local IP `192.168.1.103` once your neighbour configured their router to forward requests on port 80 to that device.

That is the way all the services you access over the Internet work. Another computer connected to the Internet provides your computer with data (text, audio, video) stored on another computer.

## Cloud Computing

## "Real" and "Virtual" in Computing

## Examples


