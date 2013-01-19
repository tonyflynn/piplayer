#!/usr/bin/python

from lcdlib import *
from time import sleep
import os
import sys
#from subprocess import *

# Add the SIGINT handler
signal.signal(signal.SIGINT, signal_handler)

# Start the LCD
lcd_init()

# Example Text
#lcd_print(line, text, format) # centred text on line 3
#lcd_scroll(line1, line2, line3, line4)

station = ""
artist = ""
song = ""

player = "pandora"
#player = "mpc"
while True:
  if player == "mpc":
    #print os.environ.get('PIPLAYER')
    mpcinfo = run_cmd("mpc current")
    mpcinfo = mpcinfo.strip()
    # check that the data is valid ie. contains a colon
    if (mpcinfo.count(": ") != 0):
      channeldata = mpcinfo.split(": ")
      station = channeldata[0].strip()
      if len(channeldata) > 1:
        songdata = channeldata[1].split(" - ")
        artist = songdata[0].strip()
        song = songdata[1].strip()
      else:
        artist = ""
        song = ""
    else:
      station = ""
  elif player == "pandora":
    # Get song info from Pandora out file: pandoraout
    f = open('pandoraout', 'r')
    pandorainfo = f.read()
    f.close
    pandorainfo =  pandorainfo.split("|")
    station = "Pandora: " + pandorainfo[0].strip()
    song = pandorainfo[1].strip()
    artist = pandorainfo[2].strip()

  # we have the results, now scroll them on the LCD
  lcd_scroll(station, "", song, artist)

def signal_handler(signal, frame):
  # handle interrupt
  print("Exiting...")
  lcd_clear
  # Exit program
  sys.exit(0)

