#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Assignment
#Usage: sh Filename.sh or ./filename.sh
#Program: script to count the number of words in a given string

echo "Enter the string"
read -r string
set $string
no_words=$#
echo "No of words in string is $no_words"
no_characters=${#string}
echo "No of characters in string is $no_characters"
