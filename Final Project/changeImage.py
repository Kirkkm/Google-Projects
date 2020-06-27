#!/usr/bin/env python3
from PIL import Image
import os

'''
In this section, you will write a Python script named changeImage.py to process the supplier images. 
You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG

After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.

'''

size = 600, 400

# sets the variables for the source images and fixed images path
ImgDir = "/supplier-data/images/"
FixedImgDir = "/supplier-data/images/"

# pulls the list of images to be modified
ImgList = os.listdir(ImgDir)


# loops through all of the images in a given directory, as it loops through it changes the size
# after that is done it saves the updated images in a separate file
for originalImage in ImgList:
    # print("updated\\" + brokenImage)

    bim = Image.open(ImgDir + originalImage)
    fixedImage = bim.convert('RGB')
    fixedImage.thumbnail(size)
    # also I could not find a way to rotate the image clockwise, only counter clockwise
    fixedImage.save(FixedImgDir + originalImage,'JPEG')