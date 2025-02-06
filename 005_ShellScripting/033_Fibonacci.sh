#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: Finding a number is in fibonacci or not
#usage: sh filename.sh or ./filename.sh 

echo "Enter a number"
read -r n
a=0
b=1
while [ $a -lt $n ]
do
	c=$(($a+$b))
	a=$b
	b=$c
	if [ $c -eq $n ]; then
		echo "Number exists"
		exit 0
	fi
done
