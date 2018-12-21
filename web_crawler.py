#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A web crawler which extracts all email addresses that are inside links.
In this example, I also extracted names and zipped them with corresponding emails for later use in sender.py.
'''
__author__ = 'Sixian Li'
__date__ = '2018-12-20'



from bs4 import BeautifulSoup
import requests
import re

def email_crawler(url):
    page = requests.get(url)
    content = BeautifulSoup(page.text, 'html.parser')
    # All names are in <h4>
    # NOTE: How I extract names here is for this particular website.
    raw_names = content.find_all('h4')
    names = [x.text for x in raw_names]
    # All emails with links start with 'mailto:'. So I took advantage of that.
    email_links = content.find_all(href=re.compile('mailto:'))
    emails = [x.get('href').split(':')[1] for x in email_links]
    return zip(names, emails)

# To extract all images sources:
# img = content.find_all('img')
# img_src = [x.get('src') for x in img]
# This will give a list of links to image sources


