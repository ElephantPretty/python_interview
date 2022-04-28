from socket import socket,AF_INET,SOCK_DGRAM
from threading import Thread

udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(('',8989))

# 接收
def recv_fun():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(">>%s:%s"%(recv_data[1],recv_data[0].decode('gb2312')))

# 发送
def send_fun():
    while True:
        addr = ('192.168.1.106',8989)
        data = input("<<:")
        udp_socket.sendto(data.encode('gb2312'),addr)



if __name__ == '__main__':
    t1 = Thread(target=send_fun)
    t2 = Thread(target=recv_fun)
    t1.start()
    t2.start()
    t1.join()
    #　因为t1这个子线程一直在执行,其实根本不会执行到t2.join()这一步
    print(111)
    t2.join()
    print(222)