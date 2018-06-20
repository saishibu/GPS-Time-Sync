#!/usr/bin/python

import os,pynmea2,serial

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
a=1
while a:
	rcv = port.readline()
	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		print msg
		time=msg.timestamp
		print lat
		#os.system('date -s "2 OCT 2006 18:00:00"')
		#os.system('date')
		print "GPS Time Syncronized"
		a=0
