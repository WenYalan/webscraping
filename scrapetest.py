from urllib.request import urlopen
from bs4 import BeautifulSoup

# try:
# 	html = urlopen("http://pythonscraping.com/pages/page1.html")
# except HTTPError as e:
# 	print(e)
# else:
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
try:
	badContent = bsObj.nonExistingTag.anotherTag
	#第二个异常，直接调用不存在的属性
except AttributeError as e:
	print("Tag was not found1")
else:
	if badContent == None:
		print("Tag was not found2")
		#第一个异常，bs返回了None对象
	else:
		print(badContent)
# print(bsObj.h1)