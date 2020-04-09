import random
import requests
import time
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
 s=str(random.randint(0,10))
 t=get_ts()
 #print("random = ",s)
 #print("ts= ",t)
 #print("salt= ",t+s)
 return t+s
     #'15864380563960'


def get_sign():
 return '27206453f157241971c871cfdba38aed'


def get_ts():

        ts = time.time()
        ts=str(int(round(ts*1000)))
        return ts
        #1586438056396
        #1586438056396




form_data={
 'i':'我和你',
 'from':'AUTO',
 'to':'AUTO',
 'smartresult':'dict',
 'client':'fanyideskweb',
 'salt':get_salt(),
 'sign':get_sign(),
 'ts':get_ts(),
 'bv':'5158ae48583349ec7168cd8d4689c03e',
 'doctype':'json',
 'version':'2.1',
 'keyfrom':'fanyi.web',
 'action':'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)