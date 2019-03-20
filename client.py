# client program
import socket, sys

if (len(sys.argv) != 6):
	print("ERROR: wrong number of arguments")
	exit()
server_name = sys.argv[1]
port = sys.argv[2]
ex_cnt = sys.argv[3]
delay = sys.argv[4]
command = sys.argv[5]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = socket.gethostbyname(server_name)

