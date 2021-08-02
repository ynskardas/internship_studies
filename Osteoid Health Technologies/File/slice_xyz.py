
import numpy as np
import SimpleITK as sitk
import os
import shutil
from PIL import Image

path="/home/ubuntu/NATURE19/NATURE_LIDC_DATA_ALL_MHD_128/"
output ="/home/ubuntu/NATURE19/NATURE_LIDC_DATA_ALL_MHD_128_XYZ/"

counter =0
files = os.listdir(path)
for folder in files:
    counter=counter+1
    print("all counter: ", counter)
    file_list = os.listdir(path+folder)
    for file in file_list:
        if file.endswith(".mhd"):
            img = sitk.ReadImage(os.path.join(path, folder, file))
            img=sitk.Cast(sitk.RescaleIntensity(img), sitk.sitkUInt8)
            print("Size: ",img.GetSize())
            #slice_number =img.GetSize()[2]
            layerx = sitk.GetArrayFromImage(img)[:,:,64]
            imx = Image.fromarray(layerx)
            imx.save(output+folder+"_X_"+str(64)+".png")
            layery = sitk.GetArrayFromImage(img)[:,64,:]
            imy = Image.fromarray(layery)
            imy.save(output+folder+"_Y_"+str(64)+".png")
            layerz = sitk.GetArrayFromImage(img)[64,:,:]
            imz = Image.fromarray(layerz)
            imz.save(output+folder+"_Z_"+str(64)+".png")







