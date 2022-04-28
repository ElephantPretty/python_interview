from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread

sockets = []


def readMsg(client_socket):
    # 读取客户端发送的消息
    while True:
        recv_data = client_socket.recv(1024)
        # 将消息发送给所有在线的客户端[qq群]
        # 这就是服务器将消息发放给当前连接的所有客户端,看起来像群发！！
        for socket in sockets:
            socket.send(recv_data)




def main():
    # 1-创建
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 2-绑定
    server_socket.bind(('', 9001))
    # 3-监听
    server_socket.listen()
    # 4-接收客户端请求
    while True:
        client_socket, client_info = server_socket.accept()
        sockets.append(client_socket)
        # 开启线程处理客户端的请求
        t = Thread(target=readMsg, args=(client_socket,))
        t.start()


if __name__ == '__main__':
    main()
