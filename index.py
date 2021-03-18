import requests;

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
queryParams = "?ServiceKey=서비스키&numOfRows=10&pageNo=1&stationName=종로구&dataTerm=DAILY&ver=1.3"

request = requests.get(url + queryParams)
print(request.text)