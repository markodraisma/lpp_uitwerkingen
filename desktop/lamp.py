#! /usr/bin/env python3

import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)
    lightpin = 18
    outpin = 13
    inpin = 15
    GPIO.setup(lightpin, GPIO.OUT)
    GPIO.setup(outpin, GPIO.OUT)
    GPIO.setup(inpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.output(outpin, True)
    lighton = False

    teller = 0
    while True:
        GPIO.wait_for_edge(inpin, GPIO.FALLING, bouncetime=300)
        if lighton:
            GPIO.output(lightpin, False)
            lighton = False
        else:
            GPIO.output(lightpin, True)
            lighton = True
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
