#!/usr/bin/env python3

import os
from datetime import date
import requests
from . import run, reports

'''
Create another script named report_email.py to process supplier fruit description data from supplier-data/descriptions directory. 
Use the following command to create report_email.py.

Import all the necessary libraries(os, datetime and reports) that will be used to process the text data from the 
supplier-data/descriptions directory into the format below:

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]

...

Once you have completed this, call the main method which will process the data and call the generate_report method from the reports module
'''

def main():

    # setting the report's file location/attachment
    report_attachment = "/tmp/processed.pdf"

    # setting up the Report's Title
    today = date.today()
    report_title = "Processed Update on " + str(today) + "\n\n"

    # this list will store all of the pdf parts in a specified order to be built later
    report_body = []

    # calls a method to in run.py script to read the fruit data from the .txt files and turn it into JSON format
    # if this method does not work then need to look at creating a REST GET request
    fruit_data = run.read_data()

    # iterates through the 2 dimensional dictionary to post each fruits data and image
    for key, value in fruit_data.items():
        report_body_name = value['name'] + "\n"
        report_body_weight = value['weight'] + "\n\n"

        report_body.append(report_body_name, report_body_weight)

    pdf = reports.generate_report(report_attachment, report_title, report_body)


if __name__ == "__main__":
    main()

