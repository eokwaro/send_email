# -*- coding: utf-8 -*-
"""test_mail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QpHOmxBWXBH2WPz2YX2rL7QkF52JTUrO
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import os
import urllib
import  requests
import json

def sendMail():
  smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
  smtp_ssl_port = 465
  username = 'edwinokwaro3@gmail.com'
  password = 'qbsjpjcykvlfcpmb'
  sender = 'edwinokwaro3@gmail.com'
  targets = ['edwinokwaro3@gmail.com','piuskanuti@gmail.com']

  msg = MIMEMultipart()
  msg['Subject'] = 'Streak Data'
  msg['From'] = sender
  msg['To'] = ', '.join(targets)

  txt = MIMEText('please find the attached streak data.')
  msg.attach(txt)

  filepath = 'dataset.csv'
  with open(filepath, 'rb') as f:
    msg.attach(MIMEApplication(f.read(), Name="dataset.csv"))
  
  server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
  server.login(username, password)
  server.sendmail(sender, targets, msg.as_string())
sendMail()

