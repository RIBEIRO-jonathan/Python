#!/usr/bin/python3
# -*- coding: utf-8 -*
import time
import serial
import gammu.smsd
import signal
from threading import Timer

smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')


import sys

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.close()
ser.open()
ser.isOpen()
print ('Enter your commands below.\nInsert "exit" to leave the application.')

input=1
#ser.flushInput()
#inbuff = ser.inWaiting()
while 1 :
	if input == 'exit':
		ser.close()
		exit()
	else:
		fin = False
		out = ''
	if fin == False:
		while ser.inWaiting() > 0:
			car = ser.read(1)
			if car == '\n' or '\r':
				time.sleep(1)
				if ser.inWaiting == 0:
					fin = True
			out += car.decode('ISO-8859-1')
	#while ser.inWaiting() > 0:
	#	out += ser.read(1).decode('ISO-8859-1')
	if out != '':
		time.sleep(1)
		print (out)
		message = {'Text': out, 'SMSC': {'Location': 1}, 'Number': '0605189427'}
		smsd.InjectSMS([message])
		ser.flush()
