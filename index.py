#pip install xmltodict requests matplotlib
import xmltodict
import requests
import json
import matplotlib.pyplot as plt

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
queryParams = "?ServiceKey=wlfnDNqYOsIwBrV%2Fq%2BpR6Qgi2N%2Bn74XgoO0wXYvFRBFpMMlXD98O%2BWHz5GpDTNxCiBTWCHt%2Fb7clHll53zZqqA%3D%3D&numOfRows=200&pageNo=1&stationName=한솔동&dataTerm=MONTH&ver=1.3"

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
    if i[choose] != '-' :
        a.append(float(i[choose]))
plt.plot(a)
plt.show()
