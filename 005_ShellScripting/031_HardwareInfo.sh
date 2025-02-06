#!/bin/sh
#Author: Gowri Sankar Marepalli
#Purpose: Knowing the hardware info of the system
#usage: ./Filename.sh or sh Filename.sh

echo "Hardware Info"
lscpu
echo "---------------------------------"
echo "---------------------------------"
echo "Hardware Info through lshw"
lshw
echo "--------------------------------------"
exe=$(free -h)
echo "free command $exe"
echo "--------------------------------------"
uname=$(uname -a)
echo "uname commadn $uname"
echo "--------------------------------------"
meminfo=$(sudo cat /proc/meminfo)
echo "meminfo command $meminfo"
echo "--------------------------------------"
disk=$(lsblk)
echo "diskinfo command $disk"
