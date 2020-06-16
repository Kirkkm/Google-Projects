#!/usr/bin/env python3
import os
import requests


'''
To add fruit images and their descriptions from the supplier on the fruit catalog web-server,
create a new Python script that will automatically POST the fruit images and their respective description in JSON format.

Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields,
including the image associated with the fruit (image_name),
 and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.
'''

# variables to use through out the code
desc_dir = "supplier-data/descriptions/"
desc_list = os.listdir(desc_dir)
# sorts the list via file name to match image and description
desc_list.sort(key=int)

image_dir ="/supplier-data/images/"
image_list = os.listdir(image_dir)
# sorts the list via file name to match image and description
image_list.sort(key=int)

# TODO: Update this variable to the appropriate ip address provide by the final project
# url to be used for posting the data
url = "http://[linux-instance-external-IP]/fruit"

# loop through all of the description & image files in the directory and put them in a JSON format
for files, images in (desc_list, image_list):
    with open(desc_list + files, "r") as f:
        fruit_description = {"name": f.readline().strip("/n"),
                             "weight": f.readline().strip("/n"),
                             "description": f.readline().strip("/n"),
                             "image_name": images}
        f.close()

        data = requests.post(url, data=fruit_description)

        # statement to raise any errors in the POST
        data.raise_for_status()
