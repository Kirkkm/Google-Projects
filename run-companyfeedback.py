#!/usr/bin/env python3
import os
import requests

feedback = {}
#pulls the list of files to read
feedbackFiles = os.listdir('/data/feedback')

#loops through each file
for files in feedbackFiles:
    #sets the filename as the key for the parent dictionary and the value is another dictionary
    i = 2
    feedback = {i,{}}
    #Reads each line in file and sets each line to the appropriate key for the child dictionary
    with open(files, 'r') as f:
        feedback[files] = {'title':f.readline()}
        feedback[files] = {'name':f.readline()}
        feedback[files] = {'date':f.readline()}
        feedback[files] = {'feedback':f.read(4)}
    i += 1

#Now to post the data in the dictionaries
url = 'http://<corpweb-external-IP>/feedback'

data = requests.post(url, data=feedback)

#Troubleshooting print statements
print(data)
print('Status code is ' + requests.status_codes())