#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

def led_on_off():
    LED = 2 #GPIO Number
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)

    #Main loop
    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(LED, GPIO.LOW)
            sleep(0.5)

    #When Ctl +C pushed
    except KeyboardInterrupt :
        pass  #Noting to do

    #clean up GPIO
    GPIO.cleanup()

if __name__ == '__main__':
    led_on_off()
