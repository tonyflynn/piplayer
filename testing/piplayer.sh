#!/bin/sh
python lcd.py &
echo Testing...
#sleep 10

gpio -g mode 15 in
for (( ; ; ))
do
	if [ $(gpio -g read 15) = 0 ]
	then
		mpc stop
	fi
done

sudo pkill -2 -f "python lcd.py"
echo The end.
