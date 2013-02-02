#!/usr/bin/python
### Control prog for Pandora ###

import subprocess
import os
import sys
import signal
from time import sleep
import RPi.GPIO as GPIO

# set up GPIO pins
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(15, GPIO.IN) # test button
#GPIO.setup(4, GPIO.OUT) # LCD backlight


def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_pandora)

  print "Starting Pandora..."
  subprocess.Popen(["/home/pi/piplayer/lcdctrl.py", "pandora"])
  sleep(1)
  subprocess.Popen(["pianobar"])

  # Start the LCD script
  #subprocess.Popen(["/home/pi/piplayer/lcdctrl.py", "pandora"])
  #os.system("/home/pi/piplayer/lcdctrl.py pandora")

  exitPlayer = False
  ### BEGIN THE LOOP ###
  while True:# exitPlayer == False:
    pass

#    if (GPIO.input(15) == False): # Button 1 pressed
      # Stop Pandora
#      os.system("echo 'q' >> /root/.config/pianobar/ctl")
      #lp.send_signal(signal.SIGINT)
#      os.system("sudo pkill -2 lcdctrl.py")
      # Write empty song file ready for the next startup
#      os.system("echo '|Loading song data...||' > /home/pi/piplayer/pandoraout")
#      exitPlayer = True
  ### END OF LOOP ###
#  sleep(10)
  kill_procs()

def signal_handler_pandora(signal, frame):
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
  #procid.send_signal(signal.SIGINT)

if __name__ == "__main__":
    main()

