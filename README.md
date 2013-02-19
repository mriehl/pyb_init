pyb_init
========

Short script to ease working with the awesome pythonbuilder.

# What it does
When using the [pythonbuilder](http://pybuilder.github.com), every project needs to be initialized.
After checking out the project, you need to 
 - Create a virtual environment
 - Activate the virtual environment
 - Install the pythonbuilder in the virtual environment
 - Install the project dependencies in the virtual environment
Only then you'll be able to build and test your project.

This script is an attempt at making these routine operations dead simple and time-efficient.

# Installation
Copy/paste the following into a shell (read it first) :

```bash
git clone https://github.com/mriehl/pyb_init ~/pyb_init && echo "source ~/pyb_init/pyb_init.sh" >> ~/.bashrc
```

# Usage

## Check out a project from GitHub and initialize it
Simply run ```pyb_init GIT_URL```

## Initialize an existing project
When in the project root, run ```pyb_init```. That's it!

# Updating
Just run a ```git pull``` in ~/pyb_init and re-source the script (or restart a shell..)
