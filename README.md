pyb_init
========

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

On a sidenote, ```pyb_init``` will always create the virtualenv with the ```--clear``` flag. Thus it is suitable
to always run ```pyb_init``` instead of ```pyb```. This will ensure you have a clean virtual environment
with no unnecessary dependencies.

# Installation
Copy/paste the following into a shell (read it first) :

```bash
git clone https://github.com/mriehl/pyb_init ./pyb_init && echo "source `pwd`/pyb_init/pyb_init.sh" >> ~/.bashrc
```

# Usage

## Check out a project from GitHub and initialize it
Simply run ```pyb_init GIT_URL```

### Example
```bash
pyb_init https://github.com/aelgru/committer
```

## Initialize an existing project
When in the project root, run ```pyb_init```. That's it!

### Example
```bash
cd project
pyb_init
```

# Updating
Just run a ```git pull``` in ~/pyb_init and re-source the script (or restart a shell..)
