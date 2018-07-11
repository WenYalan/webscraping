from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# def splitAddress(address):
# 	addressParts = address.replace('http://','')
# 	# .split('/')
# 	return addressParts


# startingPage = "http://oreilly.com"
# # elem = splitAddress(startingPage)
# elem = urlparse(startingPage).scheme+"://"
# # +urlparse
# # print(type(elem))
# print(elem)

# Time = int(time.time())
# print(str(Time))
# print(len(str(Time))
# print("1412649030")
historyUrl = "https://en.m.wikipedia.org/wiki/Special:History/Python"
print("history url is: "+historyUrl)
html = urlopen(historyUrl)
bsObj = BeautifulSoup(html,"html.parser")
ipAddresses = bsObj.findAll("p",{"class":"mw-ui-icon-mf-anonymous"})
for ipAddress in ipAddresses:
	ip = ipAddress.get_text()
	if re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ip):
		print(ip)