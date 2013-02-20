#!/bin/bash

function pyb_init(){

    __show_pyb_init_usage
    __try_to_clone_git_repository_if_argument_present_and_go_inside $@ || return 1
    __fail_if_current_directory_is_not_a_pybuilder_project || return 1
    __initialize_virtualenv || return 1
    __install_pybuilder || return 1
    pyb install_dependencies
}


function __show_pyb_init_usage(){

    echo "Usage : pyb_init [GIT_URL]"
    echo "Either initialize the current working directory or clone a git project and initialize it instead."
    return 0
}

function __try_to_clone_git_repository_if_argument_present_and_go_inside(){

    FIRST_ARGUMENT=$1
 
    [[ ! -z "$FIRST_ARGUMENT" ]] && {
        GIT_URL=$FIRST_ARGUMENT

        git clone $GIT_URL || {
            echo "ERROR: Could not clone git project at $GIT_URL ..maybe git is not installed, or the url is wrong?"
            return 1
        }
        cd `basename $GIT_URL`
    }
    return 0
}

function __fail_if_current_directory_is_not_a_pybuilder_project(){

    CURRENT_DIRECTORY=`pwd`
    PATH_TO_EXPECTED_BUILD_PY_FILE="$CURRENT_DIRECTORY/build.py"
   
    [[ -f $PATH_TO_EXPECTED_BUILD_PY_FILE ]] || {
        echo "ERROR: Did not find a build descriptor (looked for $PATH_TO_EXPECTED_BUILD_PY_FILE)."
        return 1
    }
    return 0
}

function __initialize_virtualenv(){
    
    virtualenv venv || {
        echo "ERROR: Error while creating virtualenv, maybe python-virtualenv is not installed?"
        return 1
    }

    source venv/bin/activate
    return 0
}

function __install_pybuilder(){
    
    pip install pybuilder || {
        echo "ERROR: Could not install pybuilder from PyPi.. maybe the cheeseshop is down?"
        return 1
    }
    return 0
}
