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

# pulls the data to be formatted into a PDF
# data = requests.get(url)

# statement to raise any errors in the GET
# data.raise_for_status()

# method to generate/build the PDF file with the fruit data in the .txt files


def generate_report(self,attachment, title, paragraph):
    # generates the PDF
    styles = getSampleStyleSheet()

    doc_template = []

    report_title = Paragraph(title, styles["h1"])
    report_body= Paragraph(paragraph, styles["BodyText"])
    doc_template.append(report_title,report_body)

    pdf_doc = attachment.build(doc_template)
    return pdf_doc


def main():
    report_attachment = SimpleDocTemplate("/tmp/processed.pdf")
    today = date.today()
    report_title = "Processed Update on " + str(today) + "\n\n"

    # this list will store all of the pdf parts in a specified order to be built later
    report_body = []

    # calls a method to in run.py script to read the fruit data from the .txt files and turn it into JSON format
    fruit_data = run.read_data()

    # iterates through the 2 dimensional dictionary to post each fruits data and image
    for key,value in fruit_data.items():
        report_body_name = value['name'] + "\n"
        report_body_weight = value['weight'] + "\n\n"

        report_body.append(report_body_name,report_body_weight)

    generate_report(report_attachment,report_title,report_body)


if __name__ == "__main__":
    main()