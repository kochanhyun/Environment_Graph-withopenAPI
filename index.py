import xmltodict
import requests
import json
import matplotlib.pyplot as plt

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
queryParams = "?ServiceKey=hJ1gcOgUq0k%2F2DLu0BVpkgVelUaGFGr0RiT7%2Br94vpTWGvNDiVn390MvVkTH0ZkwjDuBymy7m1t%2FyB5nP5E5lQ%3D%3D&numOfRows=10&pageNo=1&stationName=한솔동&dataTerm=DAILY&ver=1.3"

res = requests.get(url + queryParams)
cc = xmltodict.parse(res.text)
data = json.loads(json.dumps(cc))
plt.plot(data['response']['body']['items']['item'][0]['o3Value'], data['response']['body']['items']['item'][1]['o3Value'])
plt.show()