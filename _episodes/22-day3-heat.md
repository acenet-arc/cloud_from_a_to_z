---
layout: episode
title: "Heat Orchestration Templates (HOT)"
teaching: 150
exercises: 0
questions:
- "What do HOT templates do?"
- "Can I use HOT templates with cloudInit scripts?"
objectives:
- "Create a HOT template"
keypoints:
- "A Keypoint 0"
---

In this episode we will learn how to perform automated cloud environment orchestration. Basically, by the time we're done this episode, we'll see that all the work that we performed during the first two days of the course can actually be accomplished in under 5 minutes by simply executing an **OpenStack Heat template**.

**Heat** is an OpenStack orchestration engine that is used to build entire cloud applications by parsing a declarative template in the form of a text file which is treated as code. These text files are referred to as **HOT** (Heat Orchestration Templates) and they are most commonly saved as human-readable YAML files. In short, they provide us with a method of automating the creation of all cloud components, including key pairs, security groups, security rules, volumes, networks, and virtual machine instances. One key advantage of using Heat is reproducibility. That is to say, in a disaster recovery situation where we would be required to recreate a previous cloud environment, we'd simply execute our template (which is basically an exact recording of the original environment) instead of manually clicking through various web GUI interfaces and potentially guessing at all the settings for our original configuration.

It should be noted that Heat is considered to be a fairly advanced topic and might easily have its own dedicated course in order to cover all of its elements in depth. However, for the sake of this course, in order to get you started, we will introduce some basic information, illustrate some useful examples which you can execute yourself, and provide additional references that you can explore on your own, should you decide to increase your orchestration knowledge and skills.

## Terminology

There are 5 basic components that make up OpenStack Heat. They are as follows:  

- **Resources**: these are cloud objects that will be created or modified during the execution of your template. As previously mentioned, resources include key pairs, security groups, security rules, volumes, networks, and virtual machine instances.  

- **Stack**: Heat refers to stacks as collections of cloud resources.

- **Parameters**: Heat uses parameters as a means for allowing users to provide various configuration input during the deployment state of template execution. Parameters allow you to reuse your templates in order to construct similar resources with different configuration information. For example, if you wanted to deploy 3 instances, you could use the same template but provide different input parameters for instance name, instance type, etc.  

- **Templates**: templates are used to describe the stack and define the parameters. Another way to refer to a template is *Infrastructure as Code* (*IaC*).  

- **Output**: Heat allows users to define input, as well as output parameters. Use output parameters if you require information about your stack such as private and floating IP addresses, or any additional information about your stack that you would have to look up yourself.   


## Template Components


## Creating Your First HOT


## Executing Your First HOT


## Illustrating and Executing and Example WordPress HOT


## Where to Find Additional Heat Information
