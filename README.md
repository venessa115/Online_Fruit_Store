# Online_Fruit_Store

The  Online Fruits Store is a system that will update the catalog information with data provided by suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file is  uploaded to a web service that is already running using Django. A python script will process the images and descriptions and then update the online website to add the new products.Once the task is complete, the supplier will be notified through an email that indicates the total weight of fruit (in lbs) that were uploaded. The email will also contain a PDF attached with the name of the fruit and its total weight (in lbs).Finally, in parallel to the automation running, a python script is used to check the health of the system and send an email if something goes wrong.

The script  'changeImage.py' is implemented to process the supplier images and converts the image to the required format. 

The script 'supplier_image_upload.py'  is used to upload these modified images to the web server that is handling the fruit catalog. 

The script 'run.py'  will process the images and descriptions from the supplier-data/descriptions/ folder and then update the online website to add the products.

The script 'reports.py' is used to generate PDF reports with the help of the ReportLab library

The script 'emails.py' is used to format and sent the email to the SMTP configured server.

The script 'report_email.py' is used process the data and create a PDF report. This scripts calls the 'reports.py' and 'emails.py' to create the PDF and send the email respectively

The script 'health_check.py' is used to check the health of the system and send an email if something goes wrong.



