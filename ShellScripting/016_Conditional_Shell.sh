#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning Basic Commands of linux shell scripting
#Usage: sh Filename.sh or ./filename.sh
hour=$(date +%H)
if [ $hour -le 12 ]
then
    echo "Good Morning"
elif [ $hour -le 16 ]
then
    echo "Good Afternoon"
elif [] $hour -le 20 ]
then
    echo "Good Evening"
else
    echo "Good Night"
fi