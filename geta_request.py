import requests
from bs4 import BeautifulSoup
url="http://www.cntour.cn"

daan=requests.get(url)
print(daan.text)

soup=BeautifulSoup(daan.text.'lxml')
data=soup.select()
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)