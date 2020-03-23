import requests
from bs4 import BeautifulSoup
url="http://www.cntour.cn"

daan=requests.get(url)
#print(daan.text)

soup=BeautifulSoup(daan.text,'lxml')
add=soup.select(".Real > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
print(add)

for item in add:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
    print(result)