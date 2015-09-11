#!/usr/bin/env python
# avec linux et netcat, on peut envoyer un message:
# echo "hello" | nc 127.0.0.1 5005


import socket


TCP_IP = '' # fonctione aussi avec quote vide
TCP_PORT = 20668
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#conn, addr = s.accept()
#print 'Connection address:', addr

while 1:
	try:
		conn, addr = s.accept()
		#print 'Connection address:', addr
		data = conn.recv(BUFFER_SIZE)
		
		if data:
			print "received data:", data
			conn.send(data)  # echo
		
		conn.close()

	except KeyboardInterrupt:
		#conn.close()
		exit()


