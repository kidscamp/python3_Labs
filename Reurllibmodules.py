#!/usr/local/bin/python3

# This combined usage of urllib and regular expressions

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))


for eachP in paragraphs:
    print(eachP)
