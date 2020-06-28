#!/usr/bin/env python3
from PIL import Image
import os
import re

size = 600, 400

# sets the variables for the source images and fixed images path
ImgDir = "supplier-data/images/"
FixedImgDir = "supplier-data/images/"

# pulls the list of images to be modified
ImgList = os.listdir(ImgDir)

# filters the list using regex to only pull all the tiff files into a list
TIFF_finder = re.compile(".*\.tiff$")
TIFF_List = list(filter(TIFF_finder.search, ImgList))

print (TIFF_List)

# loops through all of the images in a given directory, as it loops through it changes the size
# after that is done it saves the updated images in a separate file
for originalImage in TIFF_List:
    # print("updated\\" + brokenImage)

    print(ImgDir + originalImage)

    bim = Image.open(ImgDir + originalImage)
    fixedImage = bim.convert('RGB')
    fixedImage.thumbnail(size)
    fixedImage.save(FixedImgDir + originalImage.replace('tiff','jpeg'))

    print("Image reformatted")