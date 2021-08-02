import os
import SimpleITK as sitk
inputFile = "Osteoid/Leg_Cases/abc"
txtPath = "mhd_data.txt"

spacer = "-------------------------------------\n-------------------------------------"
f = open(txtPath,"w")
for folder in os.listdir(inputFile):
        inputFileLocation = os.path.join(inputFile,folder)
        for file in os.listdir(inputFileLocation):
            total_path = os.path.join(inputFileLocation, file)
            
            if ".mhd" in file:                
                image=sitk.ReadImage(total_path)

                size = image.GetSize()
                origin = image.GetOrigin()
                spacing = image.GetSpacing()
                pixel_id = image.GetPixelID()
                pixel_id_str = image.GetPixelIDTypeAsString()
                direction = image.GetDirection()

                f.write("{}\n".format("Path of the file: " + str(total_path))) 
                f.write("{}\n".format("Size of the file: " + str(size))) 
                f.write("{}\n".format("Origin of the file: " + str(origin))) 
                f.write("{}\n".format("Spacing of the file: " + str(spacing))) 
                f.write("{}\n".format("Pixel ID of the file: " + str(pixel_id))) 
                f.write("{}\n".format("Pixel ID as String of the file: " + str(pixel_id_str))) 
                f.write("{}\n".format("Direction of the file: " + str(direction)))
                f.write("{}\n".format("" + spacer))  
                


f.close()
