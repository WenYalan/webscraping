# import urllib
from urllib import request
import json
import time

APIkey = " "
Time = int(time.time())

#python构造get请求
# url = "https://maps.googleapis.com/maps/api/geocode/json?address=1+Science+Park+Boston+MA+02114&key="+APIkey

url = "https://maps.googleapis.com/maps/api/timezone/json?location=42.3677994,-71.0708078&timestamp="+str(Time)+"&key="+APIkey
req = request.Request(url)
data = request.urlopen(req).read()
#将bytes类型转换成str类型
results = data.decode()
#将str类型转成bytes
# dictionary = eval(results)

# print(dictionary['results'][0]['address_components'])
print(results)
# print(type(dictionary))
# print(dictionary)