#!/usr/bin/python

import subprocess
import os
import sys
import signal
from time import sleep
import RPi.GPIO as GPIO

# set up GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN) # test button

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_main)

  print "Defaulting to Pandora..."
  source = "pandora"

  # Start the player script
  if source == "pandora":
    lp = subprocess.Popen(["/home/pi/piplayer/play_pandora.py", source])
  elif source == "mpc":
    lp = subprocess.Popen(["/home/pi/piplayer/play_mpc.py", source])
  exitPlayer = False

  ### BEGIN THE LOOP ###
  while exitPlayer == False:
    if (GPIO.input(15) == False): # Button 1 pressed
      ### Switch source ###
      if source == "mpc": 
      # Change source
        source = "pandora"
        mainp = subprocess.Popen(["/home/pi/piplayer/play_pandora.py", source])
      elif source == "pandora":
        # Change source
        source = "mpc"
        mainp = subprocess.Popen(["/home/pi/piplayer/play_mpc.py", source])

  ### END OF LOOP ###
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
  os.system("sudo pkill -2 play_mpc.py")
  os.system("sudo pkill -2 play_pandora.py")

if __name__ == "__main__":
    main()

