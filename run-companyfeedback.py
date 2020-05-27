#!/usr/bin/env python3
import os
import requests
import json

#feedback = []
#pulls the list of files to read
feedbackFiles = os.listdir("/data/feedback")

#loops through each file
for files in feedbackFiles:
    #sets the filename as the key for the parent dictionary and the value is another dictionary
    #Reads each line in file and sets each line to the appropriate key for the child dictionary
    with open("/data/feedback/" + files, "r") as f:
        '''
        feedback.append({"title":f.readline().strip("\n"),
                       "name":f.readline().strip("\n"),
                       "date":f.readline().strip("\n"),
                       "feedback":f.read().strip("\n")})
        '''
        feedbackPost = {"title":f.readline().strip("\n"),
                       "name":f.readline().strip("\n"),
                       "date":f.readline().strip("\n"),
                       "feedback":f.read().strip("\n")}

        feedbackJSON = json.dumps(feedbackPost)

        f.close()

        # Now to post the data in the dictionaries
        #url = "http://<corpweb-external-IP>/feedback"
        url = "http://35.222.41.65/feedback"

        data = requests.post(url, json=feedbackJSON)

        data.raise_for_status()

        print("connection is " + str(requests.get(url)))
        print("")
        print("JSON data being sent is: ")
        print(feedbackJSON)
        print("Status code is " + str(data.status_code))


#Troubleshooting print statements

print("Status code is " + str(requests.status_codes))