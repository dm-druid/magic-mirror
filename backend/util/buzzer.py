import time
import RPi.GPIO as GPIO


def beep(buzzer, interval=0.5, repeat=1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)
    for _ in range(1, repeat + 1):
        GPIO.output(buzzer, True)
        time.sleep(interval)
        GPIO.output(buzzer, False)
    GPIO.clenaup()
