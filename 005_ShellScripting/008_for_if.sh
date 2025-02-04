#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: Learning for loop
#usage: sh filename.sh or ./filename.sh 

fruits=("apple" "banana" "Grapes")
for i in "${!fruits[@]}"; do
	if ((i%2 == 0)); then
		echo "I like to eat ${fruits[$i]}"
	else
		echo " I dont like to eat ${fruits[$i]}"
	fi
done
