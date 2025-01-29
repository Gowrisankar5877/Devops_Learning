#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Assignment
#Usage: sh Filename.sh or ./filename.sh
#Program: script to check if a string is a palindrome or not
echo "Enter a string"
read -r string
length=${#string}
rev_string=""
for (( i=$length-1; i>=0; i--)); do
    rev_string="$rev_string${string:$i:1}"
done
if [[ "$string" = "$rev_string" ]]; then
    echo "The string is a palindrome"
else
    echo "The string is not a palindrome"
fi

