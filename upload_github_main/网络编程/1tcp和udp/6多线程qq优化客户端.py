from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread


def readMsg(client_socket):
    while True:
        recv_data = client_socket.recv(1024)
        print('收到:',recv_data.decode('utf-8'))


def writeMsg(client_socket):
    while True:
        msg=input('>')
        msg=user_name+"说:"+msg
        client_socket.send(msg.encode('utf-8'))

client_socket = socket(AF_INET,SOCK_STREAM)
# connect
client_socket.connect(('192.168.1.106',9001))
user_name=input('请输入用户名：')
# 线程1处理客户端读取消息
t1 = Thread(target=readMsg, args=(client_socket,))
t1.start()
# 线程2处理客户端发送消息
t2 = Thread(target=writeMsg, args=(client_socket,))
t2.start()