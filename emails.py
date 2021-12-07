#!/usr/bin/env python3
import reports
import mimetypes
import os.path
import smtplib
import email.message

def generate_email(sender, recipient, subject, body, attachment_path):
        """creates an email with an attachment."""
        #Basic email formatting
        message=email.message.EmailMessage()
        message["From"]=sender
        message["To"]=recipient
        message["Subject"]=subject
        message.set_content(body)

        #Process the attachment and add it to the email
        attachment_filename=os.path.basename(attachment_path)
        mime_type,_=mimetypes.guess_type(attachment_path)
        mime_type,mime_subtype=mime_type.split('/',1)

        with open(attachment_path,'rb') as ap:
                message.add_attachment(ap.read(),
                                        maintype=mime_type,
                                        subtype=mime_subtype,
                                        filename=attachment_filename)
        return message

def generate_error_report(sender, recipient, subject, body):
        """creates an email"""
        #Basic email formatting
        message=email.message.EmailMessage()
        message["From"]=sender
        message["To"]=recipient
        message["Subject"]=subject
        message.set_content(body)
        return message

def send_email(message):
        mail_server=smtplib.SMTP('localhost')
        mail_server.send_message(message)
        mail_server.quit()
