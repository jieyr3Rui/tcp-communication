import socket
import threading
address='127.0.0.1' 
port=12344 
buffsize=1024     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address,port))
s.listen(3)   

def tcplink(sock,addr):
    while True:  
        recv_data=clientsock.recv(buffsize).decode('utf-8')
        if recv_data=='exit' or not recv_data:
            break
        print("form client: " + str(addr) +", data:  " + recv_data)
        send_data= "from sever: [" + recv_data + "]"
        clientsock.send(send_data.encode())

    clientsock.close()

print("connecting to clients...")
ii = 0
while True:
    ii = ii + 1
    # create a new sock for the client
    clientsock,clientaddress=s.accept()
    print("connect to the " + str(ii) + "th client: ",clientaddress)
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress)) 
    t.start()
s.close()
