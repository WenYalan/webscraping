# -*- coding: utf-8 -*-
import csv 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://zh.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html,"html.parser")

csvFile = open("python内置数据类型.csv","wt", newline='',encoding='utf-8')
writer = csv.writer(csvFile)

table = bsObj.findAll("table",{"class":"wikitable"})
# for table in tables:

rows = table[0].find_all("tr")

for row in rows:
	csvRow = []
	for cell in row.find_all(["td","th"]):
		print(cell.get_text())
		csvRow.append(cell.get_text())
	writer.writerow(csvRow)

csvFile.close()
print("success!!!")

# csvFile.close()

# print(type(table[0]))
# print(table[1])

# for row in table:
# 	text = row.get_text()
# 	if re.match("^(?! )",text) is not None:
# 		print(text)
# print(type(table))
# rows = table.attrs['td']
# pinrt(rows)
# csvFile = open("python内置数据类型","wt", newline='',encoding='utf-8')
# writer = csv.writer(csvFile)