import json
from urllib.error import HTTPError
from urllib.request import urlopen

#用json模块来解析get请求
def getCountry(ipAddress):
	try:
		response = urlopen("https://ipstack.com/ipstack_api.php?ip="+ipAddress).read().decode('utf-8')
	except HTTPError:
		return none
	else:
	 	responseJson = json.loads(response)
	 	# print(response)
	 	result = responseJson.get("country_name")
	 	return result


# print(getCountry("47.52.137.83"))