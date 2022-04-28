from socket import socket,AF_INET,SOCK_STREAM

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',9001))
server_socket.listen()
# 等待客户端的连接
client_socket,client_info = server_socket.accept()
while True:
    recv_data = client_socket.recv(1024)
    print('客户端说:',recv_data.decode('utf-8'))
    msg=input('>')
    client_socket.send(msg.encode('utf-8'))