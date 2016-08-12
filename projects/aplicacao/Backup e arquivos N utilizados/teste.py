import requests
import datetime
import time

headers = {'Authorization':'token %s' % "efd7b8057d8eb6951a3138cbfd9b72cf68b17295"}

date_now = datetime.datetime.now()
date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

payload = {'collectDate': date_str, 'value': '10', 'sensor': '1', 'contextServer':'1'}

r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)

print(date_str)

print(r.text)
#print(date_now)
