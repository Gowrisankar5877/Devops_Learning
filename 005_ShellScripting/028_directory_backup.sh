#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning regular Expression
#Usage: sh Filename.sh or ./filename.sh
#Program: script to create a backup of a given directory

echo "Enter the directory name to backup"
read -r directory
if [ -d $directory ]; then
    echo "Directory exists"
    echo "Enter the backup directory name"
    read -r backup
    mkdir $backup
    cp -r $directory/* $backup
    echo "Backup created successfully"
else
    echo "Directory does not exist"
fi