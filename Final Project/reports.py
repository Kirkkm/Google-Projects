#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
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
styles = getSampleStyleSheet()
today = date.today()
report = SimpleDocTemplate("/tmp/processed.pdf")
report_title = Paragraph("Processed Update on " + str(today), styles["h1"])
report_body = ""

report.build(report_title)