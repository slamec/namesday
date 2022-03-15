#!/usr/bin/python3
import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from namesday import namesday, find_name

with open('password.txt', 'r') as file:
    read_password = file.read()

subject = "Today namesday has:" + ' ' + find_name()
body = "Hello Dorka and Miro, \n\nplease find below names day report:\n\n" + namesday()
sender_email = "stockreporter841@gmail.com"
receiver_email = ["isidora.konstantinovic5@gmail.com", "kopecky.mir@gmail.com"]
password = read_password



# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_email) #from list to a string, more email addresses 
message["Subject"] = subject
message["Bcc"] = ", ".join(receiver_email)  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))


text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)


