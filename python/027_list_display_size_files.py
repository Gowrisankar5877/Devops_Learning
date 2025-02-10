import os
def list_files(directory):
    if os.path.exists(directory):
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                print(f"{file_name}: {os.path.getsize(file_path)} bytes")
    else:
        print("Directory does not exist.")

directory = input("Enter the path of the directory")
list_files(directory)
