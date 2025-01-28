#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: Learning for loop
#usage: sh filename.sh or ./filename.sh 

fruits=("apple" "banana" "Grapes")
for i in "${fruits[@]}"; do
	echo "I like to eat ${i}"
done
fruits=("apple" "banana" "Grapes")
for i in "${!fruits[@]}"; do
	echo "fruit ate $i is ${fruits[$i]}"
done
