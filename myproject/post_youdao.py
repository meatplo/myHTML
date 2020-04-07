import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=random.randint(0,10)
    t=get_ts()
    # print("random=",s)
    # print("ts=",t)
    # print("salt=",t+str(s))
    return t+str(s)


def get_sign():
    return '2a57c66e7e063f81f8b730a87a41514b'


def get_ts():
    t = time.time()
    ts =str(int(round(t*1000)))
    return ts

form_data={
    'i': '我爱中国',
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTIONi',
}
response=requests.post(url,form_data)
print(response.text)