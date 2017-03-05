#!/usr/bin/env bash

set -e

if [ -z "$(which python3)" ]; then
  echo "Please install Python 3 if you haven't done that."
  exit 1
fi

PYTHON_ENV_NAME=python3-env

pip3 install virtualenv

virtualenv -p python3 $PYTHON_ENV_NAME

echo "source $(pwd)/$PYTHON_ENV_NAME/bin/activate" > .env
source $(pwd)/$PYTHON_ENV_NAME/bin/activate # activate the local python environment
pip3 install -r ./backend/requirements.txt

echo -e "\n"
echo "Please run \"$ source $PYTHON_ENV_NAME/bin/activate\" to switch to the python environment."
echo "Use \"$ deactivate\" anytime to deactivate the local python environment if you want to switch back to your default python."
echo "Or install autoenv as described on project readme file to make your life much easier."

mkdir -p backend/log/
