from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',8200))
serverSocket.listen(5)
clientSocket,clientinfo = serverSocket.accept()
recvData = clientSocket.recv(1024)
print(str(clientinfo),recvData.decode('gb2312'))
clientSocket.close()
serverSocket.close()