from socket import socket,AF_INET,SOCK_STREAM

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',9000))
# 监听
server_socket.listen()
# 接收客户端的连接
client_socket,client_info = server_socket.accept()
# 接收客户端发送的消息
recv_data = client_socket.recv(1024)
print('接收到%s的消息是%s'%(client_info,recv_data.decode('gb2312')))
client_socket.close()
server_socket.close()