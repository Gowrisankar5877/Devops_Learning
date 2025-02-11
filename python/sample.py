import os
import time
directory = input("Enter the directory path")
filespath = list(input("Enter the files path").split(" "))

def create_files(directory,filespath):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for files in filespath:
        file = os.path.join(directory,files)
        with open(file,"w") as fileswrite:
            fileswrite.write("This is a sample creation of file")
        print(f"File created")
create_files(directory,filespath)