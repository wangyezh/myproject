import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
 return '15859057471894'


def get_sign():
 return '36a538b751b30d75deca4b304e1b1158'


def get_ts():
        import time
        ts=time.time()
        ts=str(int(round(ts*1000)))
        return ts

        #'1586066770186'




form_data={
 'i':'我和你',
 'from':'AUTO',
 'to':'AUTO',
 'smartresult':'dict',
 'client':'fanyideskweb',
 'salt': get_salt(),
 'sign': get_sign(),
 'ts': get_ts(),
 'bv':'e2a78ed30c66e16a857c5b6486a1d326',
 'doctype':'json',
 'version':'2.1',
 'keyfrom':'fanyi.web',
 'action':'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)