import os
import signal
import sys
from time import sleep

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_ctrl2)
  
  print "control 2 waiting 5..."
  for n in range(1, 6):
    print n
    sleep(1)
  #print "control 2 done."
  
def signal_handler_ctrl2(signal, frame):
  # handle interrupt
  print("Exiting control 2...")
    # Exit program
  sys.exit(0)
  
if __name__ == '__main__':
  main()