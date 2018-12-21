#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
An email sender.
Send the same email to all recipients, replacing the title with each person's name.
'''

__author__ = 'Sixian Li'
__date__ = '2018-12-20'


import sys
import smtplib
import contacts_from_files as cf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# TODO Check argparse tutorial and improve this checker
try:
    contacts, template, server, sender, receiver = sys.argv[1:]
except IndexError as e:
    print("You need at least 5 arguments.", e)

names, emails = cf.get_contacts(contacts)
template = cf.get_template(template) # A template object

# Set up the connection
# McGill: smtp.office365.com
# Outlook: 'smtp-mail.outlook.com'
# TODO make a dictionary of servers and let users decide which one they want
smtpObj = smtplib.SMTP(server, 587)
smtpObj.ehlo()
# Puts SMTP connection in TLS mdoe
smtpObj.starttls() 
# Log in with username and passward
print('Please enter your password for your email:')
smtpObj.login(sender, input())
# Send an Email

for name, email in zip(names, emails):
    # Initialize the message
    message = MIMEMultipart()
    print('Subject line:')
    message['Subject'] = input()
    message['From'] = sender
    message['To'] = email

    # Substitute $NAME with each receiver's actual name
    msg_content = template.substitute(NAME=name)
    # Content part of an email
    message.attach(MIMEText(msg_content, 'plain'))
    try:
        smtpObj.send_message(message)
    except smtplib.SMTPException as e:
        print('An error occurred', e)

