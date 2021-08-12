import sys
import time
import gevent as ge
from gevent import socket, monkey

# 将下面的代码修改为gevent的相应功能
monkey.patch_all()


# 创建主进程套接字
def tcp_server(port):
    server = socket.socket()
    server.bind(('', port))
    server.listen(5)
    # 创建协程
    while True:
        newClient, clientAddr = server.accept()
        ge.spawn(coroutine, newClient)


# 协程函数，用于收发
def coroutine(client):
    while True:
        recvData = client.recv(1024)
        # 消息为空时，关闭套接字
        if not recvData:
            client.close()
            break
        print(f'recv: {recvData}')
        client.send(recvData)


if __name__ == '__main__':
    tcp_server(8080)
