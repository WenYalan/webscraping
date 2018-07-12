from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/")
#通过beautifulsoup来下载url图片
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a",{"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")