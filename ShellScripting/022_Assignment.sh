#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Assignment
#Usage: sh Filename.sh or ./filename.sh
#Program: Reads marks of 3 subjects of a student and grades him.

echo "Enter the marks of math subject"
read -r math_score
echo "Enter the marks of Physics subject"
read -r physics_score
echo "Enter the marks of chemistry subject"
read -r chemistry_score
if [[ $math_score -lt 30 || $physics_score -lt 30 || $chemistry_score -lt 30 ]];
then 
    echo "Student Failed"
else
    avg=$(($(($math_score+$physics_score+$chemistry_score))/3))
    #echo $avg
    if [[ $avg -ge 80 ]]
    then
        echo "Student got distinction"
    elif [[ $avg -ge 60 ]]
    then
        echo "Student got first class"
    elif [[ $avg -ge 50 ]]
    then
        echo "Student got second class"
    else
        echo "Student Passed"
    fi
fi
