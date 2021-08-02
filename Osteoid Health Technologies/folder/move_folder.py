import os
from shutil import copytree,rmtree
import shutil

source_path = "E:/new/legs/"
dest_path = "E:/new/same_utku/"

dest_files =  os.listdir(dest_path)
source_files = os.listdir(source_path)

txt_data = []

txt_file = "all_leg_cases.txt"
line = ""
with open(txt_file) as f:
    line =  f.readlines()

for i in range(len(line)):
    txt_data.append(line[0][0:11])
print(len(txt_data))

for folder in source_files:
    old_filepath = os.path.join(source_path,folder)
    new_filepath = os.path.join(dest_path, folder)
    # print(folder)
    if folder in txt_data:
        shutil.move(old_filepath,new_filepath)
        # print(folder)




    
# txt_data = line.split()


# source = []
# for i in source_files:
#     source.append(i[0 : 11])
#     if i[0 : 11] in dest_files:
#         print(i)
#         filename = i[0 : 11]
#         rmtree(dest_path+filename)
#         copytree(source_path+i,dest_path+i)
        
        


#inter_list = set(dest_files) & set(source_files)
#print(sorted(inter_list))


