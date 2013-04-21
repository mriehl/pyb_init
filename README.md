pyb_init
========

[![Build Status](https://travis-ci.org/mriehl/pyb_init.png?branch=master)](https://travis-ci.org/mriehl/pyb_init)

Short script to ease working with the awesome pybuilder.

# What it does
When using the [pybuilder](http://pybuilder.github.com), every project needs to be initialized.
After checking out the project, you need to
 - Create a virtual environment.
 - Activate the virtual environment.
 - Install the pybuilder in the virtual environment.
 - Install the project dependencies in the virtual environment.
 - Run pyb to build and test your project.

This program is an attempt at making these routine operations dead simple and time-efficient.

# Installation
```bash
sudo pip install pyb-init
```
# Usage

## Check out a project from GitHub and initialize it
Simply run 
```bash
pyb-init github user : project
```
For instance : 
```bash
pyb-init github aelgru : committer
```

## Check out a git project and initialize it
Run 
```bash
pyb-init git GIT_URL
```
For instance : 
```bash
pyb-init git https://github.com/aelgru/committer
```

## Initialize an existing project
When in the project root, run 
```bash
pyb-init local
```
