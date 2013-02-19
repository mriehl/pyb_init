#!/bin/bash

function pyb_init(){
    CURRENT_DIRECTORY=`pwd`
    PATH_TO_EXPECTED_BUILD_PY_FILE="$CURRENT_DIRECTORY/build.py"
    
    [[ -f $PATH_TO_EXPECTED_BUILD_PY_FILE ]] || {
        echo "ERROR: Did not find a build descriptor (looked for $PATH_TO_EXPECTED_BUILD_PY_FILE)."
        return 1
    }
    
    virtualenv venv || {
        echo "ERROR: Error while creating virtualenv, maybe python-virtualenv is not installed?"
        return 1
    }

    source venv/bin/activate

    pip install pybuilder || {
        echo "ERROR: Could not install pybuilder from PyPi.. maybe the cheeseshop is down?"
        return 1
    }

    pyb install_dependencies
}
