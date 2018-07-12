import csv

# csvFile = open("../files/test.csv",'w+')
#只能在当前路径下创建新文件
csvFile = open("test.csv",'w+')
try:
	writer = csv.writer(csvFile)
	writer.writerow(('number','number plus 2','number times2'))
	for i in range(10):
		writer.writerow((i,i+2,i*2))
finally:
		csvFile.close()

print("Success!")