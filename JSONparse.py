import json
from urllib.error import HTTPError
from urllib.request import urlopen


def getCountry(ipAddress):
	try:
		response = urlopen("https://ipstack.com/ipstack_api.php?ip="+ipAddress)
	except HTTPError:
		return none
	else:
	 	res = response.read().decode('utf-8')
	 	responseJson = json.loads(res)
	 	result = responseJson.get("country_code"
	    return result

print(getCountry("47.52.137.83"))