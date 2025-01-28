#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: Reading input from the table
#usage: sh filename.sh or ./filename.sh 

file=$1
if [ -f $file ]; then 
	echo "file exist $file"
else
	echo "file doesnot exist"
fi

