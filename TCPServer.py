## Author: Yin Huang
## This creates a server listening on the port 13037

from socket import *
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
port = 13037
server_address = ('localhost', port)
print >>sys.stderr, 'starting up on %s port %s' % server_address

sock.bind(server_address)

#set the socket to be listening
sock.listen(1)
while True:
	#wait for connection
	print >>sys.stderr, 'Waiting for a connection'
	connection, client_address = sock.accept()
	# accept() returns an open connection between the server and the client
	# The connection is a different socket on another port assigned by the kernel
	try:
		print >>sys.stderr, 'connection from', client_address

		#Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(16)
			print >> sys.stderr, 'received "%s"' % data
			if data: 
				print >>sys.stderr, 'sending data back to the client'
				connection.sendall(data.upper())
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
	finally:
		connection.close()