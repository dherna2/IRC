#TCPServer.py

from socket import socket, SOCK_STREAM, AF_INET
#Create TCP socket use SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort=6667
# Assign IP address and port number to socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "Close Server with CTRL-C"
print "waiting for connection..."
while True:
	try:
		connectionSocket, addr = serverSocket.accept()
		print "Client connecting from %s port %s" % addr
		# Receive the client packet with address
		while 1:
			message = connectionSocket.recv(2048)
			if not message: break
			# Capitalize the message from the client
			#message = message.upper()
			connectionSocket.send(message)
		connectionSocket.close()
	except KeyboardInterrupt:
		print "\nInterrupted by CTRL-C"
		break
serverSocket.close()
