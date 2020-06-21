#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import requests
from . import run

'''
Using the reportlab Python library, define the method generate_report to build the PDF reports.
We have already covered how to generate PDF reports in an earlier lesson;
you will want to use similar concepts to create a PDF report named processed.pdf.

Once the images and descriptions have been uploaded to the fruit store web-server,
you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed.
To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:

Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]

...
'''

# TODO: create a get request to pull the data that was just posted in run.py
# in order to help generate a PDF of the fruit, don't forget to leave comments on what everything does

# pulls the data to be formatted into a PDF
# data = requests.get(url)

# statement to raise any errors in the GET
# data.raise_for_status()

# generates the PDF
styles = getSampleStyleSheet()
today = date.today()
report = SimpleDocTemplate("/tmp/processed.pdf")

# this list will store all of the pdf parts in a specified order to be built later
doc_template = []

report_title = Paragraph("Processed Update on " + str(today), styles["h1"])

doc_template.append(report_title)

# calls a method to in run.py script to read the fruit data from the .txt files and turn it into JSON format
fruit_data = run.read_data()
report_body_date = Paragraph("Processed Update on " + date.today() + "\n\n", styles["BodyText"])

doc_template.append(report_body_date)

# iterates through the 2 dimensional dictionary to post each fruits data and image
for key,value in fruit_data.items():
    report_body_name = value['name'] + "\n"
    report_body_weight = value['weight'] + "\n\n"

    doc_template.append(report_body_name,report_body_weight)


report.build(doc_template)