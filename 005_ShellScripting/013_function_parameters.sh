#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning Vfunction with parameters
#Usage: sh Filename.sh or ./filename.sh

function sum {
    local total=$(($1 + $2))
    echo $total
}
sum 10 20