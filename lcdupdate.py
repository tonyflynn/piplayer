#!/usr/bin/python
# Python LCD update script
# Take the data we throw at it and update the LCD
#
# Handles MPC at the moment

import lcdlib

# # Define GPIO to LCD mapping
# LCD_RS = 7
# LCD_E  = 8
# LCD_D4 = 25 
# LCD_D5 = 24
# LCD_D6 = 23
# LCD_D7 = 18
# LED_ON = 15

# # Define some device constants
# LCD_WIDTH = 20    # Maximum characters per line
# LCD_CHR = True
# LCD_CMD = False

# LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
# LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
# LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
# LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line 

# # Timing constants
# E_PULSE = 0.00005
# E_DELAY = 0.00005

def signal_handler(signal, frame):
  # handle interrupt
  print("Exiting...")
  # clear the LCD
  lcd_clear()
  # Exit program
  sys.exit(0)

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler)

  # # Main program block
  # GPIO.setwarnings(False)      # supress warning messages
  # GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  # GPIO.setup(LCD_E, GPIO.OUT)  # E
  # GPIO.setup(LCD_RS, GPIO.OUT) # RS
  # GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  # GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  # GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  # GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  # GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable

  # Initialise display
  lcd_init()
  lcd_clear()
  
  # Toggle backlight off-on
  GPIO.output(LED_ON, False)
  time.sleep(1)
  GPIO.output(LED_ON, True)
  time.sleep(1)

  station = ""
  song = ""

  while True:
    # Send command output to the LCD
    cmd = "mpc|head -n1"
    mpcinfo = run_cmd(cmd)
    channeldata = mpcinfo.split(": ")
    if (channeldata[0].strip == station):
      samesong = True
    else:
      samesong = False
    station = channeldata[0].strip()
    song = channeldata[1].strip()
        
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string(station, 1)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    if (samesong == False):
      lcd_string(song, 1)
    time.sleep(1)
  
    # if either of the lines are longer than the LCD can handle
    if (len(station) > 20) or (len(song)) > 20:
      # work out which line is longer and work from that
      if len(station) > len(song):
        maxline = len(station)
      else:
        maxline = len(song)
  
      # loop through the lines to scroll the text
      # and stop a line if it hits the end
      for i in range (0, maxline - 19):
        lcdtext1 = station[i:(i + 20)]
        lcdtext2 = song[i:(i + 20)]
        # if we're at the end of the string, no more scrolling
        if (i + 19) < len(station):
          lcd_byte(LCD_LINE_1, LCD_CMD)
          lcd_string(lcdtext1, 1)
        if (i + 19) < len(song):
          lcd_byte(LCD_LINE_2, LCD_CMD)
          lcd_string(lcdtext2, 1)
        time.sleep(0.3)
    time.sleep(3)

  # Turn off backlight
  GPIO.output(LED_ON, False)

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

if __name__ == '__main__':
  main()