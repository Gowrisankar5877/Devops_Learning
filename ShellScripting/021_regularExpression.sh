#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning regular Expression
#Usage: sh Filename.sh or ./filename.sh

numstring="123456789"
if [[ $numstring =~ ^1 ]]; then
    echo "$numstring starts with 1"
else
    echo "$numstring does not start with 1"
fi
if [[ $numstring =~ ^1.*8 ]]; then
    echo "$numstring starts with 1 and contains 8"
fi
numstring="Abcdef"
if [[ $numstring =~ ^[a-zA-Z]+$ ]]; then
    echo "$numstring starts with a and contains b"
fi