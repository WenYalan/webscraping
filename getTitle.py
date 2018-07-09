from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	else:
		try:
			bsObj = BeautifulSoup(html.read(),"html.parser")
			title = bsObj.body.h1
		except AttributeError as e:
			return None

		return title

# title = getTitle("http://pythonscraping.com/pages/page1.html")
title = getTitle("http://www.html4872389.html")
if title == None:
	print("Title was not found")
else:
	print(title)
		
