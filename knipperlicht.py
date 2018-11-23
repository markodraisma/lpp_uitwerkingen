#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

lightpin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightpin, GPIO.OUT)

for i in range(15):
    GPIO.output(lightpin, True)
    time.sleep(1)
    GPIO.output(lightpin, False)
    time.sleep(1)
   
GPIO.cleanup() 
