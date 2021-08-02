import SimpleITK as sitk
import numpy as np
import os
import shutil
import re
import glob


def crop_image_left(path,new_path,rate):
    file_reader = sitk.ImageFileReader()
    file_reader.SetFileName(path)
    
    file_reader.ReadImageInformation()
    image_size = file_reader.GetSize()
    print(image_size)
    print("L")

    file_reader.SetExtractIndex((0,0,0))
    file_reader.SetExtractSize(((int(image_size[0]*rate)),image_size[1],image_size[2]))

    
    sitk.WriteImage(file_reader.Execute(),new_path, useCompression=True)

def crop_image_right(path,new_path,rate):
    file_reader = sitk.ImageFileReader()
    file_reader.SetFileName(path)
    
    file_reader.ReadImageInformation()
    image_size = file_reader.GetSize()
    print(image_size)
    print("R")
    x = int(image_size[0]*(1-rate))
    l1= int(image_size[0]) - x

    # print((x, l1))

    file_reader.SetExtractIndex((x,0,0))
    file_reader.SetExtractSize((l1,image_size[1],image_size[2]))

    
    sitk.WriteImage(file_reader.Execute(),new_path, useCompression=True)

#------------------------------MAIN---------------------------

MHD_PATH = "leg_cropped.mhd"
MHD_PATH_NEW_LEFT = "leg_cropped_left.mhd"
MHD_PATH_NEW_RIGHT = "leg_cropped_right.mhd"
RATE = 0.7

mhd_folder_path = []
count_left = 0
count_right = 0
for name in glob.glob('E:/new/legs/case-*/*'):
    check = False
    
    if "leg_cropped.mhd" in os.listdir(name):
        if "leg_cropped_left.mhd" in os.listdir(name):
            count_left += 1
            check = False
        if "leg_cropped_right.mhd" in os.listdir(name):
            count_right += 1
            check = False
        else:
            check = True
    if check:
        mhd_folder_path.append(name)
        # print(name)
        check = False

print("Number of left legs:     " + str(count_left))
print("Number of right legs:    " + str(count_right))    
    

for folder in mhd_folder_path:

    filepath = os.path.join(folder, MHD_PATH)
    left_path = os.path.join(folder, MHD_PATH_NEW_LEFT)
    right_path = os.path.join(folder, MHD_PATH_NEW_RIGHT)

    crop_image_left(filepath, left_path, RATE)
    crop_image_right(filepath, right_path, RATE)



