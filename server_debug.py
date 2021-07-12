import socket
import threading


def tcplink(sock,addr):

    while True:  
        recv_data=sock.recv(1024).decode('utf-8')
        if not recv_data:
            continue
        print("form client: " + str(addr) +", data:  " + recv_data)
    sock.close()

if __name__ == "__main__":
    address='localhost' 
    port=12355  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address,port))
    s.listen(5)   


    print("connecting to clients...")
    ii = 0
    while True:
        ii = ii + 1
        # create a new sock for the client
        clientsock,clientaddress=s.accept()
        print("connect to the " + str(ii) + "th client: " + str(clientaddress))
        t=threading.Thread(target=tcplink,args=(clientsock,clientaddress)) 
        t.start()
    s.close()
    
