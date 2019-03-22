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

# init socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = socket.gethostbyname(server_name)
port = int(port)
addr = (IP,port)

# create str & send
cmdstr = ex_cnt+'@'+delay+'@'+command
blah = cmdstr.split('@')
print(blah)
cmdstr = bytearray(cmdstr,'utf-8')
s.sendto(cmdstr,addr)
