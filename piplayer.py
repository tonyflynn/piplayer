#!/usr/bin/python

import subprocess
import os
import sys
import signal
from time import sleep
import RPi.GPIO as GPIO

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN) # test button

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_main)

  print "Starting the player in the background..."
  print "Defaulting to mpc..."
  source = "mpc"
  # Start mpc
  os.system("mpc play")

  # Start the LCD script
  subprocess.Popen(["/home/pi/piplayer/lcdctrl.py", source])

  exitPlayer = False
  ### BEGIN THE LOOP ###
  while exitPlayer != True:
    if (GPIO.input(15) == False): # Button 1 pressed
      os.system("mpc toggle")
      #print GPIO.input(15)
      sleep(0.4)

#  sleep(10)
  kill_procs()

def signal_handler_main(signal, frame):
  # handle interrupt
  print("Closing other processes...")
  # Kill subprocesses
  kill_procs()
  # Exit
  sys.exit(0)

def kill_procs():
  # kill any sub processes we've started in case we have any rogues
  # send SIGINT so they close happily
  # have signal handlers on anything you kill here...
  os.system("sudo pkill -2 lcdctrl.py")

if __name__ == "__main__":
    main()

