#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Virtual Environment creation 
#usage: ./Filename.sh or sh Filename.sh

Virtual_Env_Dir="venvdir"
requirements_file="C:/Users/Administrator/devops/Devops_Learning/python/myenv/requirement.txt"

echo "Creating Virtual Environment"
python -m venv $Virtual_Env_Dir

cd $Virtual_Env_Dir
echo "Activating Virtual Environment"
./Scripts/activate
echo "Installing dependencies"
pip install -r $requirements_file
#pip list
python C:/Users/Administrator/devops/Devops_Learning/python/036_webapp.py
