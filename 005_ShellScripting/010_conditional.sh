#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Multiple Ifs and its usage
#Usage: ./filename.sh or sh filename.sh

echo "Enter the number of players"
read -r n
for i in $(seq 1 "$n"); do
	echo "Enter batsman score"
	read -r score
	if [ "$score" -ge 20 ] && [ "$score" -lt 40 ]; then
		echo "Score is good"
	elif [ "$score" -gt  40 ] && [ "$score" -lt 100 ]; then
		echo "Score is excellent"
	else
		echo "Score is bad"
	fi
done
