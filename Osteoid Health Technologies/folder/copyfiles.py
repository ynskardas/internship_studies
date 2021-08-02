import os
import shutil

path = "C:/Users/Yunus Kardaş/Desktop/Osteoid/Leg_Cases/cases/"
dest_path = "C:/Users/Yunus Kardaş/Desktop/Osteoid/Leg_Cases/L-R_rotated/"

for root, dirs, files in os.walk(path):
    for file in files:
        
        if "d_L" in file or "d_R" in file:
            # print(os.path.join(root,file))
            copy_path = os.path.join(dest_path,root[54:])
            os.makedirs(copy_path,exist_ok=True)
            shutil.copy(os.path.join(root,file),copy_path)
            print(copy_path)