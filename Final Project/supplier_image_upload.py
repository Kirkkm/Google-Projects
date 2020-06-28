#!/usr/bin/env python3
import requests
import os
import re

'''
Now, you will have to upload these modified images to the web server that is handling the fruit catalog. 
To do that, you'll have to use the Python requests module to send the 
file contents to the [linux-instance-IP-Address]/upload URL.

In a similar way, you are going to write a script named supplier_image_upload.py 
that takes the jpeg images from the supplier-data/images directorythat you've 
processed previously and uploads them to the web server fruit catalog
'''

# variables for the urls and directories needed for this script
# TODO: change localhost to the ipaddress provided by the project
url = "http://localhost/upload/"
SupplierImages = "/supplier-data/images/"


# pulls all the files in the directory
ImageList = os.listdir(SupplierImages)

# filters the list using regex to only pull all the JPEG files into a list
JPEG_finder = re.compile(".*\.jpeg$")
JPEG_List = list(filter(JPEG_finder, ImageList))

# for troubleshooting
print(JPEG_List)

# opens & uploads all of the JPEG files to the url provided
for file in JPEG_List:
    with open(SupplierImages, 'rb') as opened:
        r = requests.post(url, files={"file": opened})
        # statement to raise any errors in the POST
        r.raise_for_status()

        print("image uploaded")