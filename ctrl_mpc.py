#!/usr/bin/python

from lcdlib import *
from time import sleep
import sys
from subprocess import *

# Start the LCD (may combine these defs in future)
lcd_setup()
lcd_init()

# Example Text
#lcd_byte(LCD_LINE_1, LCD_CMD)
#lcd_string("LCD STRING", 1) # Text on LCD Line 1
lcd_print(3, "Line 3 is here", 2) # centred text on line 3
sleep(2)

# Test the autoscroll def
lcd_scroll("This is line 1", "This is text that is too long for line 2",
  "Line 3 is here", "Line 4")

sleep(5)
lcd_clear()
