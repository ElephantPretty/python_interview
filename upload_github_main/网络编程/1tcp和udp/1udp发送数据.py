from socket import socket,AF_INET,SOCK_DGRAM

# 1-创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
data = input("请输入要发送的消息:")
# 我使用127.0.0.1是接收不到数据的,这时接收数据的端口是随机分配的
addr = ('192.168.1.106',8080)

# 2-调用sendto方法发送信息 网络编程助手编码是gb2312
# print(type(data.encode('gb2312','127.0.0.1:8080')))
udp_socket.sendto(data.encode('gb2312'),addr)
# 3-关闭套接字
udp_socket.close()