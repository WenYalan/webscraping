from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from JSONparse import getCountry

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html = urlopen("https://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html,"html.parser")
	return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("/wiki/(?!File)"))

def getHistoryIPs(pageUrl):
	target = pageUrl.replace("/wiki/","")
	print("--------------")
	print("This is the target: "+target)
	print("--------------")
	historyUrl = "https://en.m.wikipedia.org/wiki/Special:History/"+target
	# print("history url is: "+historyUrl)
	html = urlopen(historyUrl)
	bsObj = BeautifulSoup(html,"html.parser")
	ipAddresses = bsObj.findAll("p",{"class":"mw-ui-icon-mf-anonymous"})
	addressList = set()
	for ipAddress in ipAddresses:
		ip = ipAddress.get_text()
		if re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ip):
			# print(ip)
			addressList.add(ip)
	return addressList
#捕获该链接下的其他所有链接
links = getLinks("/wiki/Computer")
while(len(links)>0):
	for link in links:
		#打印各个链接下的historyIP
		print("--------------")
		historyIPs = getHistoryIPs(link.attrs['href'])
		for historyIP in historyIPs:
			# print(historyIP)
			country = getCountry(historyIP)
			if country is not None:
				print(historyIP+" is from "+country)
	# 随机选择主页面中的一个链接，捕获其中的links，进行historyIP打印
	newLink = links[random.randint(0,len(links)-1)].attrs['href']
	links = getLinks(newLink)
    


 
