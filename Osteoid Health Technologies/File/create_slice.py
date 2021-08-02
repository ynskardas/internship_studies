import os 
import SimpleITK as sitk
from PIL import Image

path = "Resample/output/"
dest_path = "Resample_Slice/"

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".mhd"):
            print("File found.")
            os.makedirs(dest_path+root[-11:],exist_ok=True)
            os.makedirs(dest_path+root[-11:]+"/"+file[:-4],exist_ok=True)
            img = sitk.ReadImage(os.path.join(root,file))
            img=sitk.Cast(sitk.RescaleIntensity(img), sitk.sitkUInt8)
            size = img.GetSize()
            print("Size: ",size)
            for i in range(size[2]):
                if i%20==0:
                    layerz = sitk.GetArrayFromImage(img)[i,:,:]
                    imz = Image.fromarray(layerz)
                    imz.save(dest_path+root[-11:]+"/"+file[:-4]+"/Z"+str(i)+".png")