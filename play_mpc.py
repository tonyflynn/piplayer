#!/usr/bin/python
### Control prog for mpc ###

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
  signal.signal(signal.SIGINT, signal_handler_mpc)

  print "Starting mpc..."
  #pp = subprocess.Popen(["pianobar"])
  os.system("mpc play")

  # Start the LCD script
  lp = subprocess.Popen(["/home/pi/piplayer/lcdctrl.py", "mpc"])

  exitPlayer = False
  ### BEGIN THE LOOP ###
#  while exitPlayer == False:
#    if (GPIO.input(15) == False): # Button 1 pressed
      # Stop mpc
#      os.system("mpc stop")
#      exitPlayer = True
  ### END OF LOOP ###
#  sleep(10)
#  kill_procs()

def signal_handler_mpc(signal, frame):
  # handle interrupt
  print("Closing other processes...")
  # Kill subprocesses
  kill_procs()
  #lp.send_signal(signal.SIGINT)
#  os.system("sudo pkill -2 lcdctrl.py")

  # Exit
  sys.exit(0)

def kill_procs():
  # kill any sub processes we've started in case we have any rogues
  # send SIGINT so they close happily
  # have signal handlers on anything you kill here...
  os.system("sudo pkill -2 lcdctrl.py")
  os.system("mpc stop")
  #procid.send_signal(signal.SIGINT)

if __name__ == "__main__":
    main()

