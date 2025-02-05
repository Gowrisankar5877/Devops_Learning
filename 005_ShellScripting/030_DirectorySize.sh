#!/bin/sh
#Author: Gowri Sankar Marepalli
#Purpose: printing the size of the directory
#usage: ./Filename.sh or sh Filename.sh

echo "Enter the directory you want to know the size"
read -r directory
du -h "$directory"