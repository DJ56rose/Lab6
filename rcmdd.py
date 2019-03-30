# ===== server TCP =====
import socket, sys, datetime, time, subprocess

if (len(sys.argv) != 2):
	print("ERROR: wrong number of args")
	exit()
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',port))

server.listen(5)

while True:
	client,addr = s.accept()
	msg = client.recv(1024)
	msg.decode('utf-8')

	
