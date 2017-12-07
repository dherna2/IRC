#TCPClient.py

from socket import socket, AF_INET, SOCK_STREAM
import sys
import string

serverPort=6667
serverName='localhost'
cmd = ""
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
NICK = raw_input('what is your nickname: ')

print 'Display commands type /? or type a message to send: '

while(cmd != "/quit"):
	#cmd = raw_input("<{}> ".format(NICK)).strip()
	cmd = raw_input()
	if cmd == "/quit":
		print 'Good bye!'
		clientSocket.close()
		exit(0)
#	if cmd and len(cmd) > 0:
	elif cmd == "/?":
		print '/quit /join /leave /create /list'
	while True:
		message = raw_input('Message: ')
		clientSocket.send(message)
		modifiedMessage = clientSocket.recv(2048)
		if modifiedMessage == "/quit":
			print 'Good bye!'
			clientSocket.close()
			exit(0)
		print '<%s>: %s ' % (NICK,modifiedMessage)
clientSocket.close()
