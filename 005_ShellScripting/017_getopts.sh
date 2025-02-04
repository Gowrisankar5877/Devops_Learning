#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpuse: learn getopts
#usage: sh filename.sh or ./filename.sh 

while getopts :a:b: flag; do
    case $flag in
    a) ab=$OPTARG;;
    b) bc=$OPTARG;;
    ?) echo "I don't know what value is this"
    esac
done
echo "first value $ab Second Value $bc"