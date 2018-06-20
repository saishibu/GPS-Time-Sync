#!/usr/bin/python

import os,pynmea2,serial
import datetime
import subprocess

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
a=1
while a:
	rcv = port.readline()
	print rcv[0:6]
	if rcv[0:6] == '$GPRMC':
		msg=pynmea2.parse(rcv)
		print msg
		time=msg.datetime
		print time
		time=time.replace(microsecond=0)
		time=time+datetime.timedelta(hours=5.3)
		#time=time.strftime("%d/%b/%Y  %H:%M:%S")
		#time=datetime.datetime(time)
		#time=unicode(time)
		print time
		#dateset= 'date -s +'+time
		print dateset
		subprocess.call(['sudo', 'date', '-s', '{:}'.format(time)]) #Sets system time (Requires root, obviously)
		#os.system(dateset)
		os.system('date')
		print "GPS Time Syncronized"
		a=0
