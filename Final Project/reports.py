#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

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


def generate_report(self,attachment, title, paragraph):
    # generates the PDF
    styles = getSampleStyleSheet()

    doc_template = []

    report_attachment = SimpleDocTemplate(attachment)

    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["BodyText"])
    doc_template.append(report_title, report_body)

    pdf_doc = report_attachment.build(doc_template)

    print("Report Generated")
    return pdf_doc
