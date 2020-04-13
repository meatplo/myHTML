import random
import requests
import time

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content = "我爱中国"


class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_salt(self):
        s = random.randint(0, 10)
        t = self.ts
        # print("random=",s)
        # print("ts=",t)
        # print("salt=",t+str(s))
        return t+str(s)

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i = self.salt
        e = self.content
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print("s=",s,"md5=",get_md5(s))
        return self.get_md5(s)
        # return '2a57c66e7e063f81f8b730a87a41514b'

    def get_ts(self):
        t = time.time()
        ts = str(int(round(t*1000)))
        return ts

    # def get_content(self):
        # return '我爱中国'

    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '70244e0061db49a9ee62d341c5fed82a',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTIONi',
        }
        return form_data

    def get_headers(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=552218048@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=1027920486.8660557; JSESSIONID=aaaSCabsZTj3hc01bLIfx; ___rl__test__cookies=1586498032499',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    youdao = Youdao('我爱中国')
    print(youdao.fanyi())
