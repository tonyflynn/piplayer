#!/usr/bin/env python
from time import sleep 
import os 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(23, GPIO.IN)

while True:
	if ( GPIO.input(23) != False ):
		print("Button press...")
	sleep(0.3);
