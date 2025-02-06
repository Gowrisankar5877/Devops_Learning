#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Finding odd or even
#Usage: sh Filename.sh or ./filename.sh
echo "enter an number"
read -r n
if [ $((n%2)) -eq 0 ]; then
	echo "Even Number"
else
	echo "Odd Number"
fi
