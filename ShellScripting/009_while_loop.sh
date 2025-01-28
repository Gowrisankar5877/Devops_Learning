#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning while loop
#usage: sh filename.sh or ./filename.sh 

echo "Enter a number"
read -r n
echo "Multiplication Table of $n"
counter=1
while [ $counter -le 10 ] 
do
	multiplication=`expr $n \* $counter`
	echo "$n * $counter = $multiplication"
	counter=`expr $counter + 1`
done

