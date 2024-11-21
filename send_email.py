import yagmail
import os


################## SEND A SINGLE EMAIL#############
sender = 'app7flask@gmail.com'
receiver = '2jjnkjca@10mail.tk'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")


############SEND EMAIL AT CERTAIN TIME ###############
# import yagmail
# import os
# import time
# from datetime import datetime as dt
#
# sender = 'app7flask@gmail.com'
# receiver = 'fbcmakfsd@emltmp.com'
#
# subject = """
# This is the subject!
# """
# contents = """
# Here is the content of the email!
# Hi!
# """
# while True:
#   now = dt.now()
#   if now.hour == 13 and now.minute == 18:
#     yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
#     yag.send(to=receiver, subject=subject, contents=contents)
#     print("Email Sent!")
#     time.sleep(60)

#############SEND EMAILS TO A CSV LIST OF CONTACTS ###########


import yagmail
import os
import pandas

sender = 'your_gmail_address@gmail.com'

subject = """
This is the subject!
"""
# The password should be a Gmail app password.

yag = yagmail.SMTP(user=sender, password="Your Gmail App Password")
df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
  contents = f"""
Hi {row['name']} the content of the email! 
Hi!
"""
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("Email Sent!")


  ################ SEND EMAIL WITH ATTACHMENTS ##############
  import yagmail
  import os

  sender = 'app7flask@gmail.com'
  receiver = 'app7flask@gmail.com'

  subject = """
  This is the subject!
  """
  contents = ["""
  Here is the content of the email! 
  Hi!
  """, 'text.txt']

  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))  # Set your own PASSWORD in Repl Secrets
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")

###############

import yagmail
import os
import pandas

sender = 'app7flask@gmail.com'
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))  # Set your own PASSWORD in Repl Secrets

df = pandas.read_csv('contacts.csv')

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index, row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    amount = row['amount']
    receiver_email = row['email']

    generate_file(filename, amount)

    subject = "This is the subject!"
    contents = [f"""
  Hey, {name} you have to pay {amount}
  Bill is attached!""",
                filename,
                ]

    yag.send(to=receiver_email, subject=subject, contents=contents)
    print("Email Sent!")



################# SEND EMAIL USING OUTLOOK #############
import smtplib
import os

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()


############## SEND EMAIL WITH HTML ########

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()


############## SEND OUTLOOK MAIL WITH ATTACHMETS#########

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = 'tiger.jpeg'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()

