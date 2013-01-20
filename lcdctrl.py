#!/usr/bin/python

from lcdlib import *
from time import sleep
import os
import sys
#from subprocess import *

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_lcd)

  # Command line args
  player = sys.argv[1]

# Start the LCD
  lcd_init()

# Example Text
#lcd_print(line, text, format) # centred text on line 3
#lcd_scroll(line1, line2, line3, line4)

  # Show the system info first
  ipinfo = run_cmd("ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1")
  dayinfo = run_cmd("date +'%A'")
  dateinfo = run_cmd("date +'%d %b %Y'")
  timeinfo = run_cmd("date +'%I:%M %p'")
  lcd_scroll(dayinfo.strip(), dateinfo.strip(), timeinfo.strip(), ipinfo.strip())
  sleep(5)

  while True:
    if player == "mpc":
      songdata = get_list_mpc("mpc Stream")
    elif player == "pandora":
      songdata = get_list_pandora("Pandora")

    #Display scrolling data on the L:CD
    lcd_scroll(songdata[3], songdata[0], songdata[2], songdata[1])

# List functions must return a 4-element list: 
# - Station/Title/Artist/Label
def get_list_mpc(label):
  station = ""
  artist = ""
  song = ""
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
  datalist = [station, song, artist, label]
  #print mpcinfo
  #print datalist
  return datalist

def get_list_pandora(label):
	station = ""
	artist = ""
	song = ""
	# Get song info from Pandora out file: pandoraout
	f = open('pandoraout', 'r')
	pandorainfo = f.read()
	f.close
	pandorainfo =  pandorainfo.split("|")
	station = pandorainfo[0].strip()
	song = pandorainfo[1].strip()
	artist = pandorainfo[2].strip()
	datalist = [station, song, artist, label]
	return datalist

def signal_handler_lcd(signal, frame):
  # handle interrupt
  print("Closing LCD updater...")
  lcd_clear()
  # Exit program
  sys.exit(0)

if __name__ == "__main__":
    main()
