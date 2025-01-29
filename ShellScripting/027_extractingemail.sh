#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning regular Expression
#Usage: sh Filename.sh or ./filename.sh
#Program: script to extract email addresses from a text file

echo "Enter file name"
read -r filename
if [ -f $filename ]; then
    echo "File exists"
    echo "Email Addresses fetched are"
    grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}' $filename
else
    echo "File does not exist"
fi