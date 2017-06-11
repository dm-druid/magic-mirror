import requests
import wave
import os

CUID = '7519663'
APIKEY = 'Ll0c53MSac6GBOtpg22ZSGAU'
SECRET = '44c8af396038a24e34936227d4a19dc2'


def get_token():
    api_key = APIKEY
    secret_key = SECRET
    auth_url = 'https://openapi.baidu.com/oauth/2.0/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': APIKEY,
        'client_secret': SECRET
    }
    result = requests.get(auth_url, params=payload)
    return result.json()['access_token']


def recognize(filename):
    baidu_token = get_token()

    fp = wave.open(filename, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)
    fp.close()
    os.remove(filename)

    url = 'http://vop.baidu.com/server_api'
    payload = {
        'cuid': CUID,
        'token': baidu_token
    }
    headers = {
        'Content-Type': 'audio/pcm; rate=16000',
        'Content-Length': str(f_len)
    }
    result = requests.post(url, params=payload, data=audio_data, headers=headers)
    response = result.json()

    if response['err_msg'] == 'success.':
        text = ''.join(response['result'])
        if text[-1] == '，':
            text = text[:-1]  # remove last comma
        return {
            'text': text
        }
    return {
        'error': response['err_msg']
    }
