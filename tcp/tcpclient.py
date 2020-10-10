from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.connect(('192.168.1.243',8200))
while True:
    msg=input('>:')
    client_socket.send(msg.encode('utf-8'))
    recv_data = client_socket.recv(1024)
    print('server<:'+recv_data.decode('utf-8'))