pyb_init
========

[![Build Status](https://travis-ci.org/mriehl/pyb_init.png?branch=master)](https://travis-ci.org/mriehl/pyb_init)

Short script to ease working with the awesome pythonbuilder.

# What it does
When using the [pythonbuilder](http://pybuilder.github.com), every project needs to be initialized.
After checking out the project, you need to
 - Create a virtual environment.
 - Activate the virtual environment.
 - Install the pythonbuilder in the virtual environment.
 - Install the project dependencies in the virtual environment.
 - Run pyb to build and test your project.

This script is an attempt at making these routine operations dead simple and time-efficient.

# Installation
```bash
sudo pip install pyb-init
```
# Usage

## Check out a project from GitHub and initialize it
Simply run ```pyb-init github user : project```
For instance : ```pyb-init github aelgru : committer```


## Initialize an existing project
When in the project root, run ```pyb-init local```. That's it!
