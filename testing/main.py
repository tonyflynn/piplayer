import signal
import os
import sys
import subprocess
from time import sleep

def main():
  # Add the SIGINT handler
  signal.signal(signal.SIGINT, signal_handler_main)
  
  exitprog = False
  while exitprog == False:
    # Start process 1
    print "Starting control 1"
    p = subprocess.Popen("python control1.py")
    #print p
    print "waiting for control 1..."
    p.communicate()
    #print p
    print "Control 1 complete."
    # Wait 5
    print "Main waiting 5..."
    sleep(5)
    # Start process 2
    print "Starting control 2"
    p = subprocess.Popen("python control2.py")
    #print p
    print "waiting for control 2..."
    p.communicate()
    #print p
    print "Control 2 complete."
    # Get out
    print "Main complete."
    exitprog = True
    
def signal_handler_main(signal, frame):
  # handle interrupt
  print("Exiting...")
    # Exit program
  sys.exit(0)    
  
if __name__ == '__main__':
  main()