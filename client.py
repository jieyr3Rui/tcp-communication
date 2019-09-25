import socket
host='localhost'
port=12344
addr=(host,port)
tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffsize=1024  
tcpCliSock.connect(addr)
while True:
    msg=input('Please input: ')
    if not msg:
        break
    tcpCliSock.send(msg.encode('utf-8'))
    recv_data = tcpCliSock.recv(buffsize).decode('utf-8')
    print(recv_data)

