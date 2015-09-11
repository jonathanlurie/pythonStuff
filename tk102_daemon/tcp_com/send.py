#!/usr/bin/env python

import socket
import time


TCP_IP = '37.187.225.190'
TCP_PORT = 20668
BUFFER_SIZE = 1024
MESSAGE = "140321190607,+33624267358,GPRMC,180607.683,A,4335.9151,N,00127.1699,E,0.00,32.59,210314,,,A*5D,F,, imei:013227007709334,05,144.3,F:3.79V,0,139,21644,208,01,320F,1F24"



i = 0

while(1):
	time.sleep(2)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(MESSAGE)
		data = s.recv(BUFFER_SIZE)
		s.close()
		i = i + 1
		print("envoye " + str(i) + " fois")
	except socket.error:
		print("l'ordi cible a refuse")
	
	
#print "received data:", data

