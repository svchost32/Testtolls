from socket import *
from threading import Thread
import os

sockets=[]

def main():
    server_socket = socket(AF_INET,SOCK_STREAM)
    server_socket.bind(('',8200))
    server_socket.listen()

    while True:
        client_socket,client_info=server_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=readMSG,args=(client_socket,))
        t.start()
        print('thread restart')


def readMSG(client_socket):
    while True:
        try:
            recv_data=client_socket.recv(1024)
        except:
            print('失去连接')
            sockets.remove(client_socket)
            client_socket.close()
            break
        # recv_data.decode('utf-8')
        if recv_data.decode('utf-8').endswith('exit'):
            sockets.remove(client_socket)
            client_socket.close()
            print('结束服务')
            os._exit(0)
        if len(recv_data) > 0:
            for socket in sockets:
                print('发送消息来自'+str(socket))
                # print(recv_data.decode('utf-8'))
                socket.send(recv_data)


if __name__ == '__main__':
    main()