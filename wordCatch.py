from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")
# nameList = bsObj.findAll("span",{"class":"green"})
# for name in nameList:
# 	print(name.get_text())

# name = bsObj.find("span",{"class":"green"})
# print(name)
#limit可以设置为数值1，2，3
# nameList = bsObj.findAll(text="the prince")
# print(len(nameList))

#keyword功能
allText = bsObj.findAll(id="text")
print(allText[0].get_text)
	