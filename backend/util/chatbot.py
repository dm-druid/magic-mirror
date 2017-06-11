import requests

KEY = 'fdd2570a79a64a5b859b41df89b24ab6'
URL = 'http://www.tuling123.com/openapi/api'


def chat(text):
    data = {
        'key': KEY,
        'info': text,
        'userid': '666'
    }
    res = requests.request('post', URL, data=data)
    if res.status_code != 200:
        raise AssertionError
    return res.json()['text']
