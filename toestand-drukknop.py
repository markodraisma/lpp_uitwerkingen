#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

pluspin = 13
pushpin = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pluspin, GPIO.OUT)
GPIO.output(pluspin, True)


GPIO.setup(pushpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    if GPIO.input(pushpin):
        print('knop ingedrukt')
    else:
        print('knop niet ingedrukt')
    time.sleep(1)

GPIO.cleanup()
