#!/bin/sh
python lcd.py &
echo Testing...
sleep 10
sudo pkill -2 -f "python lcd.py"
echo The end.
