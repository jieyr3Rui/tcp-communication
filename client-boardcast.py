import socket


if __name__ == "__main__":
    host='localhost'
    port=12344
    addr=(host,port)
    tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    buffsize=1024  
    print("connecting...")
    tcpCliSock.connect(addr)
    print("connected!")

    while True:
        recv_data = tcpCliSock.recv(buffsize).decode('utf-8')
        print(recv_data)

