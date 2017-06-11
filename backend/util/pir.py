# HC-SR501 Passive Infrared (PIR) Motion Sensor

import time
import RPi.GPIO as GPIO


def detect(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)
