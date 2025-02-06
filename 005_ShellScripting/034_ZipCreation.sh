#!/bin/bash
#Author: Gowri Sankar Marepalli
#Purpose: Creating a zip of a folder
#usage: sh filename.sh or ./filename.sh 
echo "Enter folder you need to create a zip"
read -r folder
if [ -d $folder ]; then
	zip -r Outputzipfile.zip $folder
	echo "Folder Successfully Zipped"
else
	echo "Folder not found"
fi

