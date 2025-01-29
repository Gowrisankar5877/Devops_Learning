#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Assignment
#Usage: sh Filename.sh or ./filename.sh
#Program: script to convert a string to uppercase

echo "Enter a string"
read -r string
uppercase_string=$(echo $string | tr 'a-z' 'A-Z')
echo "The string in uppercase is: $uppercase_string"