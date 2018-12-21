#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Helper functions to read contatcs' information and the template file.
'''

__author__ = 'Sixian Li'
__date__ = '2018-12-20'

from string import Template

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, 'r', encoding='utf-8') as contact_file:
        # Read each line in a CSV file
        for a_contact in contact_file:
            names.append(a_contact.split(',')[0])
            emails.append(a_contact.split(',')[1])
    return names, emails

# Create a template object from a template file
def get_template(filename):
    with open(filename, 'r', encoding='utf-8') as temp:
        temp_content = temp.read()
    return Template(temp_content)
