#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning Variables
#Usage: sh Filename.sh or ./filename.sh
var1=10
var2='Hello'
hostname={`hostname`}
date=`date`
#The following definition variables are not allowed
1value=100
false@linux=false
echo "var1 = $var1"
echo "var2=$var2"
echo "hostname=$hostname"
echo "date=$date"
echo "1value=$value"
echo "false@linux = $false@linux"
