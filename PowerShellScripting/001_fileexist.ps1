#Author: Gowri Sankar Marepalli
#Purpose: Learning basic powershell scripting
#Usage: sh Filename.sh or ./filename.sh
#Program: power shell script to check whether the desktop folder exists or not and listing files
$folderpath = Read-Host "Enter the folder path"
if( Test-Path $folderpath)
{
    Write-Host "Folder exists"
    cd $folderpath
    echo "Files in the folder are:"
    ls
}
else
{
    Write-Host "Folder does not exist"
}
