import os

def rename_files():
    #(1) get file names from a folder
    home_directory = os.getcwd()
    file_list = os.listdir(home_directory+"/directory_of_message")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(home_directory+"/directory_of_message")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()

