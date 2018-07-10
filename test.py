from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime
import random

def splitAddress(address):
	addressParts = address.replace('http://','')
	# .split('/')
	return addressParts


startingPage = "http://oreilly.com"
# elem = splitAddress(startingPage)
elem = urlparse(startingPage).scheme+"://"
# +urlparse
# print(type(elem))
print(elem)