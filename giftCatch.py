from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

# for child in bsObj.find("table",{"id":"giftList"}).children:
# 	print(child)
#兄弟标签
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
# 	print(sibling)
#父标签.parent;选中前一个兄弟标签.previous_sibling

# print(bsObj.find("img",{
# 	"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# 通过正则表达式来抓取图片的url
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

# for image in images:
# 	print(image["src"])

element = bsObj.find("tr",{"id":"gift1"})

print(element.attrs)