#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Getting backup
#usage: sh filename.sh or ./filename.sh

function backup {
    echo "Enter the file name to take backup"
    read -r backupfile
    if [ -f $backupfile ]; then
        echo "File exists"
        cp $backupfile /tmp/backupfile
        echo "Backup is taken"
    else
        echo "File does not exist"
    fi
    cp $backupfile /tmp/backupfile
    #echo $?
    if [ $? -ne 0 ]; then #ne is not equal to
        echo "Backup failed"
    fi
}
backup
