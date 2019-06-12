#!/usr/bin/python3
# -*- coding: utf-8 -*
import time
import serial
import gammu.smsd

smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')


import sys

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
ser.close()
ser.open()
ser.isOpen()
print ('Enter your commands below. \r\nInsert "exit" to leave the application.')

input=1
while 1 :
	# get keyboard input
	#input = raw_input(">> ")
	# python 3 users
	#input = input(">> ")
	if input == 'exit':
		ser.close()
		exit()
	else:
		# send the character to the device
		#ser.write(input + ' \r\n ')
		out = ''
		time.sleep(1)
		while ser.inWaiting() > 0:
			
			out += ser.read(1).decode('ISO-8859-1')
			
		if out != '':
			print (out)
			message = {'Text': out, 'SMSC': {'Location': 1}, 'Number': '0605189427'}
			smsd.InjectSMS([message])
