#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Assignment
#Usage: sh Filename.sh or ./filename.sh
#Program: script to replace a word in a file with another word

echo "Enter the file name"
read -r filename
if [ -f $filename ]; then
    echo "Enter the word to be replaced"
    read -r word1
    echo "Enter the word to be replaced with"
    read -r word2
    echo "The initial file"
    cat $filename 
    sed -i "s/$word1/$word2/g" $filename
    echo "The word $word1 is replaced with $word2 in the file $filename"
    echo "File after replacing the word"
    cat $filename
else
    echo "The file $filename does not exist"
fi