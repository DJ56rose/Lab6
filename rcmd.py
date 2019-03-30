# ===== client TCP =====
import socket, sys, datetime

if (len(sys.argv) != 6):
	print("ERROR: wrong number of args")
	exit()
server_name = sys.argv[1]
port = int(sys.argv[2])
ex_cnt = sys.argv[3]
delay = sys.argv[4]
command = sys.argv[5]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(server_name)
s.connect((IP,port))

# send command
cmdstr = ex_cnt+'@'+delay+'@'+command
cmdstr = bytes(cmdstr,'utf-8')
s.sendall(cmdstr)

dim = s.recv(10)	# rx input dimensions
result = []
for i in range(0,dim):
	result = result+s.recv(1)	# receive one byte at a time

print(result)
print(type(result))
