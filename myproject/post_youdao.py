import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846841472292'


def get_sign():
    return '2a57c66e7e063f81f8b730a87a41514b'


def get_ts():
    return '1584684147229'


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