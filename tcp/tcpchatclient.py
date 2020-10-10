from socket import *
from threading import Thread

flag = True

def readMSG(client_socket):
    while flag:
        recv_data=client_socket.recv(1024)
        print(recv_data.decode('utf-8'))


def writeMSG(client_socket):
    global flag
    while flag:
        msg= input('>')
        # msg=uid+' : '+msg
        client_socket.send(msg.encode('utf-8'))
        if msg.endswith('exit'):
            flag=False
            break



client_socket = socket(AF_INET,SOCK_STREAM)
# client_socket.connect(('192.168.1.243',8200))
client_socket.connect(('192.168.1.215',8200))
# uid = input('ID:')
t1= Thread(target=readMSG,args=(client_socket,))
t2= Thread(target=writeMSG,args=(client_socket,))
t1.start()
t2.start()
t1.join()
t2.join()

client_socket.close()


