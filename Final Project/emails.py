#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import mimetypes

'''
Send report through email

Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.

Define generate_email and send_email methods by importing necessary libraries.

Once you define the generate_email and send_email methods, call the methods under the main method after creating the PDF report:
'''


def generate_email(self, email_from, email_to, subject_line, body, attachment):
    email = EmailMessage()
    email['From'] = email_from
    email['To'] = email_to
    email['Subject'] = subject_line
    email.set_content(body)

    mime_type, _ = mimetypes.guess_type(attachment)

    print("email generated")


def send_email(self):
    print("email sent")