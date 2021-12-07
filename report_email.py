#!/usr/bin/python3
import reports
import emails
import os
from os import listdir
from datetime import date

def pdfcontent(src_path):
   content=[]
   for filename in listdir(src_path):
      filepath=src_path+filename
      with open(filepath) as file:
         fruit_name=file.readline()
         content.append("name: "+fruit_name.strip())
         weight=file.readline()
         content.append("weight: "+weight.strip())
   return content


if __name__=='__main__':
   # Generate a PDF report
   summary=pdfcontent('./supplier-data/descriptions/')
   print(summary)
   pdfcontent="<br />".join(summary)
   print(pdfcontent)
   reports.generate_report("/tmp/processed.pdf", "Processed Update on "+str(date.today().strftime("%B %d, %Y")),pdfcontent.replace('lbs<br />','lbs<br /><br />'))
   # send the PDF report as an email attachment
   sender = "automation@example.com"
   receiver = "{}@example.com".format(os.environ.get('USER'))
   subject = "Upload Completed - Online Fruit Store"
   body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
   message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
   emails.send_email(message)
