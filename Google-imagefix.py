import os
from PIL import Image

#setting variables to be used in the code
size = 128, 128
imgDir = 'Test Photos\\'
fixedImgDir = 'Updated Photos\\'

#this will pull a list of all the images we need to correct
image_list = os.listdir(imgDir)

#for troubleshooting, both print statement help with what direcotry the code is currently on
print(os.getcwd())
#for troubleshooting, both print statement help with what is save on the list
print(image_list)




#loops through all of the images in a give directory, as it loops through it changed the size and roates them
#after that is done it saves the updated images in a seperate file
for brokenImage in image_list:
    #print("updated\\" + brokenImage)

    bim = Image.open(imgDir + brokenImage)
    fixedImage = bim.convert('RGB')
    fixedImage.thumbnail(size)
    #this was odd, in order for the rotation to save I had to call a save on the same line as the rotation
    #also I could not find a way to rotate the image clockwise, only counter clockwise
    fixedImage.rotate(270,expand = 1,).save(fixedImgDir + brokenImage,'JPEG')



