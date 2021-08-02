import os
import SimpleITK as sitk
path = "C:/Users/Utku/Desktop/rotated_leg_all/"
spacer = "-------------------------------------\n-------------------------------------"

f =  open("mhd_info.txt","w")
    
for root, dirs, files in os.walk(path):
    for file in files:
        if file=="left_leg_cropped.mhd" or file=="right_leg_cropped.mhd" or file=="leg_cropped_right.mhd" or file=="leg_cropped_left.mhd" or file=="leg_cropped_L.mhd" or file=="leg_cropped_R.mhd":
            image=sitk.ReadImage(os.path.join(root,file))

            size = image.GetSize()
            origin = image.GetOrigin()
            spacing = image.GetSpacing()
            pixel_id = image.GetPixelID()
            pixel_id_str = image.GetPixelIDTypeAsString()
            direction = image.GetDirection()

            f.write("{}\n".format("Path of the file: " + str(os.path.join(root,file)))) 
            f.write("{}\n".format("Size of the file: " + str(size))) 
            f.write("{}\n".format("Origin of the file: " + str(origin))) 
            f.write("{}\n".format("Spacing of the file: " + str(spacing))) 
            f.write("{}\n".format("Pixel ID of the file: " + str(pixel_id))) 
            f.write("{}\n".format("Pixel ID as String of the file: " + str(pixel_id_str))) 
            f.write("{}\n".format("Direction of the file: " + str(direction)))
            f.write("{}\n".format("" + spacer)) 

f.close()