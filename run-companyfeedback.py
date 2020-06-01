#!/usr/bin/env python3
import os
import requests

# pulls the list of files to read
feedbackFiles = os.listdir("D:\\Coding\\Google Certificate Project\\git-repo\\data\\feedback")

# loops through each file
for files in feedbackFiles:
    # sets the filename as the key for the parent dictionary and the value is another dictionary
    # Reads each line in file and sets each line to the appropriate key for the child dictionary
    with open("D:\\Coding\\Google Certificate Project\\git-repo\\data\\feedback\\" + files, "r") as f:
        feedbackPost = {"title": f.readline().strip("\n"),
                        "name": f.readline().strip("\n"),
                        "date": f.readline().strip("\n"),
                        "feedback": f.read().strip("\n")}

        f.close()

        # Now to post the data in the dictionaries
        # url = "http://httpbin.org/post" - public test url I found on StackOverflow
        url = "http://<corpweb-external-IP>/feedback"

        # posting the data
        data = requests.post(url, data=feedbackPost)

        # statement to raise any errors in the POST
        data.raise_for_status()

        # Troubleshooting print statements
        '''
        print("connection is " + str(requests.get(url)))
        print("")
        print("JSON data being sent is: ")
        print(feedbackJSON)
        print("Status code is " + str(data.status_code))
        print("ok status code is " + str(requests.codes.ok))
        print(data.content)
        '''
