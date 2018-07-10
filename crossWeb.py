from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime
import random
import time

pages = set()
random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()
#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
	# includeUrl = urlparse(includeUrl).scheme+"://"+urlparse
	internalLinks = []
	#找出所有以""开头的链接
	# for link in bsObj.findAll("a",href=re.compile("^(|.*"+includeUrl+")")):
	for link in bsObj.findAll("a",href=re.compile("^(http|www)("+includeUrl+")*")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
			else:
				internalLinks.append(link.attrs['href'])
	return internalLinks

def splitAddress(address):
	addressParts = address.replace('http://','').split('/')
	return addressParts

#获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
	externalLinks = []
	#找出所有以"http"或"www"开头且不包含当前URL的链接
	for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html,"html.parser")
	externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = []
		print("No external links,looking around the site for one")
		# domain = urlparse(startingPage).scheme+"://"+urlparse
		internalLinks = getInternalLinks(bsObj,splitAddress(startingPage)[0])
		return internalLinks[random.randint(0,len(internalLinks)-1)]
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print("Random external link is:"+externalLink)
	try:
		followExternalOnly(externalLink)
		time.sleep(2) #休眠两秒钟
	except(HTTPError,ValueError,URLError):
		followExternalOnly(externalLink)

def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
	externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])

	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			allIntLinks.add(link)
			print("既将获取连接的URL是："+link)
			time.sleep(5)#休眠5秒
			getAllExternalLinks(link)
			

#main部分
# followExternalOnly("http://oreilly.com")
try:
	getAllExternalLinks("http://oreilly.com")
except(HTTPError,ValueError,URLError):
	print("Error!")