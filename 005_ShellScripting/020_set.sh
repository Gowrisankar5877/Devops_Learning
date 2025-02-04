#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning set command
#Usage: sh Filename.sh or ./filename.sh

set `date`
set -x #It prints the command before executing it
echo "Today's  is $1"
echo "Month is $2"
echo "Date is $3"
echo "Year is $4"
echo "Time is $5"
echo "Timezone is $6"


