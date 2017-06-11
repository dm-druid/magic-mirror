from io import BytesIO
import requests
import picamera

URL = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
KEY = '8e324b3a6578461d806d999a88432c37'
    # 'cdf047a980cb468588893fc1e55af2ca'


def get_emotional_values(binary_data):
    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Content-Type': 'application/octet-stream'
    }
    result = requests.request('post', URL, data=binary_data, headers=headers)
    response = result.json()
    if not response:
        return {'error': 'no face detected'}
    else:
        return response[0]['scores']


def take_and_judge_photo():
    stream = BytesIO()
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.capture(stream, format='jpeg', quality=50)
    camera.close()

    stream.seek(0)
    with open('picture.jpg', 'wb') as f:
        f.write(stream.read())
        f.close()

    stream.seek(0)
    return get_emotional_values(stream.read())
