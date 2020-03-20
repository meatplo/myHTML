import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i': '我爱中国',
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846841472292',
    'sign': '2a57c66e7e063f81f8b730a87a41514b',
    'ts': '1584684147229',
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTIONi',
}
response=requests.post(url,form_data)
print(response.text)