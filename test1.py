#!/usr/bin/python

import os,pynmea2



a=1
while a:
	rcv = port.readline()
	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		time=msg.timestamp
		print lat
    #os.system('date -s "2 OCT 2006 18:00:00"')
    #os.system('date')
		print "GPS Time Syncronized"
		a=0
