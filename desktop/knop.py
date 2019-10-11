#! /usr/bin/env python3

import time
import RPi.GPIO as GPIO

outpin = 13
inpin = 15
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(outpin, GPIO.OUT)
    GPIO.setup(inpin, GPIO.IN)
    GPIO.output(outpin, True)
    teller = 0
    while teller < 50:
        time.sleep(.1)
        if GPIO.input(inpin):
            print("ingedrukt")
        else:
            print("niet ingedrukt")
        teller += 1

finally:
    GPIO.cleanup()



