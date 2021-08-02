import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import time

# spacing = 0.5 => 56.911   (two mhd file for L-R legs)
# spacing = 3.0 => 21.574   (two mhd file for L-R legs)

start = time.time()
input_path="Osteoid/Leg_Cases/caseExp/input"
output_path="Osteoid/Leg_Cases/caseExp/output"

for file_name in os.listdir(input_path):
    file_path = os.path.join(input_path, file_name)
    for file in os.listdir(file_path):
        if file.endswith(".mhd"):
            img=sitk.ReadImage(os.path.join(file_path,file))
            # original image information
            print(file_path, "Original Image Information")
            print(img.GetSize())
            print(img.GetSpacing())
            print("Direction: ", img.GetDirection())
            dimension = img.GetDimension()
            # Physical image size corresponds to the largest physical size in the training set, or any other arbitrary size.
            #reference_physical_size = (512,512,512)
            # Create the reference image with a zero origin, identity direction cosine matrix and dimension
            reference_origin = np.zeros(dimension)
            reference_direction = np.identity(dimension).flatten()
            print("dimension direction: ", dimension)
            reference_size = [400,400,900]
            reference_spacing = [1.0,1.0,1.0]
#           reference_outputPixelType=sitk.sitkUInt16
            reference_image = sitk.Image(reference_size, img.GetPixelIDValue())
            reference_image.SetOrigin(reference_origin)
            reference_image.SetSpacing(reference_spacing)
            reference_image.SetDirection(reference_direction)

#           reference_image.SetOutputPixelType(reference_outputPixelType)
            # Always use the TransformContinuousIndexToPhysicalPoint to compute an indexed point's physical coordinates as
            # this takes into account size, spacing and direction cosines. For the vast majority of images the direction
            # cosines are the identity matrix, but when this isn't the case simply multiplying the central index by the
            # spacing will not yield the correct coordinates resulting in a long debugging session.

            reference_center = np.array(reference_image.TransformContinuousIndexToPhysicalPoint(np.array(reference_image.GetSize())/2.0))
            # Transform which maps from the reference_image to the current img with the translation mapping the image
            # origins to each other.
            transform = sitk.AffineTransform(dimension)
            transform.SetMatrix(img.GetDirection())
            transform.SetTranslation(np.array(img.GetOrigin()) - reference_origin)
            # Modify the transformation to align the centers of the original and reference image instead of their origins.
            centering_transform = sitk.TranslationTransform(dimension)
            img_center = np.array(img.TransformContinuousIndexToPhysicalPoint(np.array(img.GetSize())/2.0))
            centering_transform.SetOffset(np.array(transform.GetInverse().TransformPoint(img_center) - reference_center))
            #centered_transform = sitk.Transform(transform)
            centered_transform=sitk.CompositeTransform([transform, centering_transform])
            # Using the linear interpolator as these are intensity images, if there is a need to resample a ground truth
            # segmentation then the segmentation image should be resampled using the NearestNeighbor interpolator so that
            # no new labels are introduced.
            imj =sitk.Resample(img, reference_image, centered_transform, sitk.sitkBSpline, -1024)
            print("resized image size: ")
            print(imj.GetSize())
            print(imj.GetOrigin())
            print(imj.GetSpacing())
            os.makedirs(os.path.join(output_path,file_name), exist_ok=True)
            sitk.WriteImage(imj, os.path.join(output_path,file_name,file), useCompression=True)
end = time.time()
print('Finally! Total time: {}'.format(end-start))

"""
z = int(img.GetDepth()/1)
npa_zsl = sitk.GetArrayFromImage(img)[z,:,:]
plt.imshow(npa_zsl, cmap=plt.cm.Greys_r)
plt.show()
"""




