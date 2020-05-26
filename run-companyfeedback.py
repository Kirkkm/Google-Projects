#!/usr/bin/env python3
import os
import requests

feedback = []
#pulls the list of files to read
feedbackFiles = os.listdir("/data/feedback")

i = 2
#loops through each file
for files in feedbackFiles:
    #sets the filename as the key for the parent dictionary and the value is another dictionary
    #Reads each line in file and sets each line to the appropriate key for the child dictionary
    with open("/data/feedback/" + files, "r") as f:
        feedback.append({"title":f.readline().strip("\n"),
                       "name":f.readline().strip("\n"),
                       "date":f.readline().strip("\n"),
                       "feedback":f.read().strip("\n")})
        f.close()
    i += 1

#Now to post the data in the dictionaries
url = "http://<corpweb-external-IP>/feedback"

for userfeedback in feedback:
    data = requests.post(url, data=userfeedback)
    print(userfeedback)
    print("")
    #print(data.text)



#Troubleshooting print statements
#print(feedback)
#print(feedback.values())
#print(data.text)
print("Status code is " + str(requests.status_codes))