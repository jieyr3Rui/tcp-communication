import socket
import threading

def keyboard():
    global sock_l, addr_l
    msg = ""
    while True:
        if len(sock_l) > 0:
            msg=input('Please input: ')
            # empty msg
            if not msg:
                continue
            # try to remove a socket connection
            elif msg == "close socket":
                print("connected sock: ")
                print(addr_l)
                index = int(input('Please input remove_index: '))
                if index < len(sock_l):
                    sock_l[index].shutdown(socket.SHUT_WR)
                    sock_l[index].close()
                    sock_l.remove(sock_l[index])
                    addr_l.remove(addr_l[index])
                    print("successfully remove socket")
                else:
                    print("cancel remove socket")
            # boardcast msg
            else:
                for sock in sock_l:
                    sock.send(msg.encode())
    return


if __name__ == "__main__":
    global sock_l, addr_l
    sock_l = []
    addr_l = []
    address='localhost' 
    port=12344 
    buffsize=1024     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address,port))
    s.listen(5)   


    print("connecting to clients...")
    ii = 0

    tk=threading.Thread(target=keyboard,args=()) 
    tk.start()

    while True:
        ii = ii + 1
        # create a new sock for the client
        clientsock,clientaddress=s.accept()
        print(clientsock)
        print("\nconnect to the " + str(ii) + "th client: " + str(clientaddress))
        sock_l.append(clientsock)
        addr_l.append(clientaddress)
    
    
    s.close()
    
