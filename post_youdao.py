import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
 'i':'我和你',
 'from':'AUTO',
 'to':'AUTO',
 'smartresult':'dict',
 'client':'fanyideskweb',
 'salt':'15859057471894',
 'sign':'36a538b751b30d75deca4b304e1b1158',
 'ts':'1585905747189',
 'bv':'e2a78ed30c66e16a857c5b6486a1d326',
 'doctype':'json',
 'version':'2.1',
 'keyfrom':'fanyi.web',
 'action':'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)