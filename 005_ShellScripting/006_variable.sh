#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: Checking whether file exists with multiple spaces in file name and without spaces in file name
#usage: sh filename.sh or ./filename.sh 

file=$1
if [ -f "$file" ]; then 
	echo "file exist $file"
else
	echo "file doesnot exist"
fi
if [ -f $file ]; then 
	echo "file exist $file"
else
	echo "file doesnot exist"
fi


