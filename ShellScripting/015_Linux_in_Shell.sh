#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning Basic Commands of linux shell scripting
#Usage: sh Filename.sh or ./filename.sh

echo "I am $USERNAME. $USERNAME is the tiger of the jungle"
echo "my current working directory is `pwd`"
echo "`whoami`"
echo "`date`"
ls
command="ls -ltr /etc"
echo "$command"
eval $command
