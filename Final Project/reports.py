#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import requests
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

# TODO: Update this variable to the appropriate ip address provide by the final project
# url to be used for getting the data
url = "http://[linux-instance-external-IP]/fruit"

# TODO: create a get request to pull the data that was just posted in run.py in order to help generate a PDF of the fruit, don't forget to leave comments on what everything does

# pulls the data to be formatted into a PDF
data = requests.get(url)

# statement to raise any errors in the GET
data.raise_for_status()

# generates the PDF
styles = getSampleStyleSheet()
today = date.today()
report = SimpleDocTemplate("/tmp/processed.pdf")
report_title = Paragraph("Processed Update on " + str(today), styles["h1"])
report_body = ""

report.build(report_title)