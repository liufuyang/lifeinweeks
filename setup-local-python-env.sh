#!/usr/bin/env bash

PYTHON_3_DIR=/Library/Frameworks/Python.framework/Versions/3.5/bin/
PYTHON_ENV_NAME=python3.5-env

echo "Please install python3.5.1 if you haven't done that."
echo "On Mac OS X the default community version python 3 will be install at $PYTHON_3_DIR"

if [ ! -d "$PYTHON_3_DIR" ]; then
  # if PYTHON_3_DIR doesn't exist.
  echo "Could not find python version 3.5 on path $PYTHON_3_DIR. Please install it or specify a different path in the script"
  exit 1
fi

pip install virtualenv

virtualenv -p $PYTHON_3_DIR/python3 $PYTHON_ENV_NAME

echo "source $(pwd)/python3.5-env/bin/activate" > .env

source $(pwd)/$PYTHON_ENV_NAME/bin/activate # activate the local python environment

pip install -r ./backend/requirements.txt


echo "Please run \"$ source $PYTHON_ENV_NAME/bin/activate\" to switch to the python environment."
echo "Use \"$ deactivate\" anytime to deactivate the local python environment if you want to switch back to your default python."
echo "Or install autoenv as described on project readme file to make your life much easier."
