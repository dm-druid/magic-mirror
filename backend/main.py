import time
from util.buzzer import beep
from util.pir import detect
from util.chatbot import chat
from util.photo import take_and_judge_photo
from util.dht import get_environment_data
from util.recorder import record_and_recognize

DHT = 4
BUZZER = 21
DETECTOR = 24

flag = False


def welcome():
    flag = True
    print('您好，朱彦樵先生！')
    now_time = int(time.strftime("%H", time.localtime()))
    if now_time > 23 or now_time < 5:
        print('这么晚了还不睡吗？')
    elif 6 <= now_time <= 7:
        print('您起的真早！')
    face_score = take_and_judge_photo()
    if face_score.get('error', None) is not None:
        print('关闭屏幕')
        flag = False
    else:
        if float(face_score['neutral']) > 0.5\
            or float(face_score['anger']) > 0.5\
            or float(face_score['disgust'] > 0.5):
            emotion_text = '您今天看上去不太开心呢！'
            print(emotion_text)
            print(chat(emotion_text))
        elif float(face_score['surprise']) > 0.5:
            emotion_text = '您看上去有小惊喜！'
            print(emotion_text)
            print(chat(emotion_text))
        elif float(face_score['happiness']) > 0.5:
            emotion_text = '您看上去很开心哦！'
            print(emotion_text)
            print(chat(emotion_text))
        elif float(face_score['sadness']) > 0.5:
            emotion_text = '有什么烦恼就尽管和我说吧'
            print(emotion_text)
            print(chat(emotion_text))
        else:
            emotion_text = '看不出来您在想什么……真是个神秘的人呐……'
            print(emotion_text)
    pass

def main():
    while True:
        if True:  #detect(DETECTOR) == 1:
            if flag == True:
                text = record_and_recognize()
                if text.get('error', None) is not None:
                    print('您说啥？没听清……')
                else:
                    print(text['text'])
                    print(chat(text['text']))
                    if text['text'] == '再见':
                        flag = False
            else:
                welcome()
        time.sleep(0.5)

if __name__ == '__main__':
    flag = False
    main()
