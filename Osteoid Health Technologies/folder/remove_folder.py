from ntpath import join
import os
from shutil import copytree,rmtree
import shutil

source_path = "E:/new/legs/"
dest_path = "E:/new/same_utku/"

dest_files =  os.listdir(dest_path)
source_files = os.listdir(source_path)

for folder in source_files:
    check = False
    if folder != 'savefile.txt':
        old_filepath = os.path.join(source_path,folder)
        new_filepath = os.path.join(dest_path, folder)
        # print(old_filepath)
        for folder2 in os.listdir(old_filepath):
            folder2_path = os.path.join(old_filepath, folder2)
            for file in os.listdir(folder2_path):

                if '.zraw' in file:
                    check = True
                    break
        
            break
        
        if not check:
            print(old_filepath)
            shutil.rmtree(old_filepath)

        
        
                
                
            

    # # print(folder)
    # if folder in txt_data:
    #     shutil.move(old_filepath,new_filepath)
    #     # print(folder)