import socket, sys, os, datetime, time, subprocess

if (len(sys.argv) != 2): 
    print("ERROR: wrong number of arguments")
    exit()
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

# listen
while True:
    # receive
    msg,addr = s.recvfrom(1024)
    IP_client = addr[0]
    
    # parse message
    msg = msg.decode('utf-8')
    cmdstr = msg.split('@')
    xcnt = int(cmdstr[0])   # execution cnt
    delay = float(cmdstr[1])
    command = cmdstr[2]

    # execute
    for i in range(0,xcnt):
        output = subprocess.run(command,stdout=subprocess.PIPE)
        result = output.stdout.decode('utf-8')

        # print in server
        timp = 'Time: '+str(datetime.datetime.now())+'\n'
        IP = 'Src IP: '+IP_client+'\n'
        cmd = 'Command: '+command+'\n'
        status = 'Status: Connected\n'
        server_msg = timp+IP+cmd+status
        print(server_msg)    

        # to client: time+result
        timp = str(datetime.datetime.now())
        s.sendto(bytes(timp+'\n'+result,'utf-8'),addr)
        # wait
        time.sleep(delay)   
    
    # terminate
    donemsg = '@Done'
    s.sendto(bytes(donemsg,'utf-8'),addr)
   
    # rx ending msg
    msg,addr = s.recvfrom(1024)
    print(msg.decode('utf-8'))

