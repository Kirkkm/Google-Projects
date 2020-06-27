#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import mimetypes
import os

'''
Send report through email

Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.

Define generate_email and send_email methods by importing necessary libraries.

Once you define the generate_email and send_email methods, call the methods under the main method after creating the PDF report:
'''

# method generate the email
def generate_email(self, email_from, email_to, subject_line, body, attachment):
    # sets up the email
    email = EmailMessage()
    email['From'] = email_from
    email['To'] = email_to
    email['Subject'] = subject_line
    email.set_content(body)

    # adds the attachment to the email
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment, 'rb') as ap:
        email.add_attachment(ap.read(),
                             maintype = mime_type,
                             subtype = mime_subtype,
                             filename = os.path.basename(attachment))

    return email
    print("email generated")

# method to receive the generated email and send it through the appropriate smtp
def send_email(self, email):
    # TODO: figure out when the smtp ssl will be for this project and fill out below
    mail_server = smtplib.SMTP_SSL("")

    mail_user = ''
    mail_pass = ''

    mail_server.login(mail_user,mail_pass)
    mail_server.sendmail(email)

    mail_server.quit()

    # debugging
    # mail_server.set_debuglevel(1)

    print("email sent")
