#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Learning until
#Usage: ./filename.sh or sh filename.sh

echo -e  "Please enter ip address to ping\c"
read -r ip
until ping $ip
do
	echo "host in $ip is down"
	sleep 1
done
echo "Host in $ip is up"
