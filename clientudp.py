import socket, sys, datetime

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
cmdstr = bytes(cmdstr,'utf-8')
s.sendto(cmdstr,addr)

# receive
while True:
    msg,addr = s.recvfrom(1024)
    msg = msg.decode('utf-8')
    if msg[0] == '@':   # rx done msg
        break
    print(msg)

# print time & terminate
timp = datetime.datetime.now()
finish = bytes('Finished: '+str(timp),'utf-8')
s.sendto(finish,addr)

