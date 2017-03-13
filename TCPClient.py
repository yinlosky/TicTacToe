## Author: Yin Huang
## This file will create the client side code to connect with the tic tac toe server


from socket import *
import sys

# create a socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening 
port = 13037
server_address = ('localhost', port) // use localhost for now

print >>sys.stderr, 'connecting to %s port %s' % server_address

sock.connect(server_address)
###############################

try: 
	#send data
	message = 'this is the message. it will be upper-cased.'
	print >>sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	# waiting for response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
	print >>sys.stderr, 'received "%s"' % data
finally:
	print >>sys.stderr, 'closing socket'
	sock.close()