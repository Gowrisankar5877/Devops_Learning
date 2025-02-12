import os
directory = input("Enter directory Path")

def list_files(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            filepath = os.path.join(directory,filename)
            if os.path.isfile(filepath):
                print(f"{filename}: {os.path.getsize(filepath)}")
    else:
        print("Directory Does not exists")
list_files(directory)