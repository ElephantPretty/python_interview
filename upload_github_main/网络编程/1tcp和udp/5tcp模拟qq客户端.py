from socket import socket,AF_INET,SOCK_STREAM

client_socket = socket(AF_INET,SOCK_STREAM)
# connect
client_socket.connect(('192.168.1.106',9001))
while True:
    # 客户端发送消息
    msg = input('>')
    client_socket.send(msg.encode('utf-8'))
    # 客户端接收消息
    recv_data = client_socket.recv(1024)
    print('服务器端说:',recv_data.decode('utf-8'))