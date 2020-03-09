import requests

url="http://www.cntour.cn"

daan=requests.get(url)
print(daan.text)