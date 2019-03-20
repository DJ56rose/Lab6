import socket, sys, os

if (len(sys.argv) != 2):
	print("ERROR: wrong number of arguments")
	exit()
port = sys.argv[1]

s = socket.socket(socket.AF_INET,socket.SOCKET_DGRAM)
