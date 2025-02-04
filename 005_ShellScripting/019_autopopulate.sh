#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning autopopulate
#Usage: sh Filename.sh or ./filename.sh

echo "All arguments Concatenated together $*"
echo "No of arguments $#"
echo "prints first and second arguments $1 $2"
echo " Expands all cmd line arguments as separate words $@"
echo "PID of the current process $$"

sleep 400 & # specifying & after command specifes the command to run in background
echo " prints the PID of the last background process $!"  
echo "Filename of the current program $0"