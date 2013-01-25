import os
import signal
import sys
from time import sleep

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_ctrl1)
  
  print "control 1 waiting 5..."
  for n in range(1, 6):
    print n
    sleep(1)
  #print "control 1 done."
  
def signal_handler_ctrl1(signal, frame):
  # handle interrupt
  print("Exiting control 1...")
    # Exit program
  sys.exit(0)
  
if __name__ == '__main__':
  main()