#pip install xmltodict requests matplotlib
import xmltodict
import requests
import json
import matplotlib.pyplot as plt

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
queryParams = "?ServiceKey=hJ1gcOgUq0k%2F2DLu0BVpkgVelUaGFGr0RiT7%2Br94vpTWGvNDiVn390MvVkTH0ZkwjDuBymy7m1t%2FyB5nP5E5lQ%3D%3D&numOfRows=200&pageNo=1&stationName=한솔동&dataTerm=MONTH&ver=1.3"

res = requests.get(url + queryParams)
cc = xmltodict.parse(res.text)
jsontemp = json.loads(json.dumps(cc))

print("so2Value\ncoValue\no3Value\nno2Value\npm10Value\npm25Value\n")
choose = input("INPUT : ")

plt.xlabel('HOUR')
plt.ylabel(choose)
plt.title(choose)

a = []

for i in jsontemp['response']['body']['items']['item'] :
    a.append(float(i[choose]))
plt.plot(a)
plt.show()
