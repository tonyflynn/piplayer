#!/bin/sh
python lcd.py> /dev/null 2>&1 & echo $! > "lcd.pid"
echo Testing...
sleep 10
sudo pkill -2 -f "python lcd.py"
echo The end.
