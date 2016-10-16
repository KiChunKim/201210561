import os 
KEY="697a486559636e3037304356486844" 
TYPE='json'
SERVICE = 'StationAdresTelno' 
START_INDEX='1'
END_INDEX='20'
LINE_NUM='2'

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM

import requests
data=requests.get(url)

print data.text