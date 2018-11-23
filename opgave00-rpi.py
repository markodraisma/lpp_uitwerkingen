#!/usr/bin/env python3

import RPi.GPIO as GPIO

lighton = False

pluspin = 13
pushpin = 15
lightpin = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pluspin, GPIO.OUT)
GPIO.output(pluspin, True)   # for switch

GPIO.setup(lightpin, GPIO.OUT)
GPIO.setup(pushpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    GPIO.wait_for_edge(pushpin, GPIO.FALLING, bouncetime=300)
    if lighton:
        GPIO.output(lightpin, False)
        lighton = False
    else:
        GPIO.output(lightpin, True)
        lighton = True

GPIO.cleanup()
