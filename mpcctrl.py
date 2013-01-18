#!/usr/bin/env python
from time import sleep 
import os 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(15, GPIO.IN)

while True:
	if ( GPIO.input(15) == False ): # button pressed
		os.system('mpc toggle')
		sleep(0.4);
