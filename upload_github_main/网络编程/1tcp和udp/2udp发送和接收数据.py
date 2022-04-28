from socket import socket,AF_INET,SOCK_DGRAM

with socket(AF_INET,SOCK_DGRAM) as udp_socket:
    addr=('192.168.1.106',8080)
    # 绑定一个端口,''代表本机
    udp_socket.bind(('',8989))
    data=input("请输入要发送的信息:")
    udp_socket.sendto(data.encode('gb2312'),addr)
    # 表示本次接收的最大字节数1024
    recv_data = udp_socket.recvfrom(1024)
    print('接收到%s的消息是%s'%(recv_data[1],recv_data[0].decode('gb2312')))
    # udp_socket.close()