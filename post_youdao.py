import random
import requests
import time
import  json
import hashlib
class Youdao():
    def __init__(self,content):
        self.content=content
        self.url=" http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()
    def get_salt(self):
        return self.ts + str(random.randint(0, 10))


    def get_md5(self,value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)


    def get_ts(self):
        ts = str(int(round(time.time() * 1000)))
        return ts

    def yield_form_data(self):
        form_data={
            'i':self.content,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv':'5158ae48583349ec7168cd8d4689c03e',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_CLICKBUTTION',
        }
        return form_data
    def get_headers(self):
        return {
                    'Cookie': 'OUTFOX_SEARCH_USER_ID=461655988@10.108.160.17; JSESSIONID=aaaFE8--wD_8--zByeFfx; OUTFOX_SEARCH_USER_ID_NCOO=2098111493.268126; ___rl__test__cookies=1586775128482',
                    'Referer': 'http://fanyi.youdao.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        }



    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    while(True):
        try:
           i=input("please input:")
           youdao=Youdao(i)
           print("fanyi result",youdao.fanyi())
        except:
             pass

