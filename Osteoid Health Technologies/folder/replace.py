import os
from shutil import copytree,rmtree
dest_path = "D:/legs/"
source_path = "C:/Users/Utku/Desktop/Osteoid/cases/"

dest_files =  os.listdir(dest_path)
source_files = os.listdir(source_path)

source = []
for i in source_files:
    source.append(i[0 : 11])
    if i[0 : 11] in dest_files:
        print(i)
        filename = i[0 : 11]
        rmtree(dest_path+filename)
        copytree(source_path+i,dest_path+i)
        
        


#inter_list = set(dest_files) & set(source_files)
#print(sorted(inter_list))



