import socket as s
from threading import Thread
from time import sleep


def main():
    # 创建TCP服务器，并重复使用绑定的信息
    tcpServer = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpServer.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    localAddr = ('', 8080)
    tcpServer.bind(localAddr)
    # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的
    connNum = input('请输入要链接服务器的次数:')
    tcpServer.listen(int(connNum))

    # 捕获control c时，结束监听
    try:
        while True:
            print('主进程，等待新客户端的到来')
            newSocket, clientAddr = tcpServer.accept()
            print(f'主进程，接下来创建一个线程负责数据处理[{clientAddr}]')
            # 创建线程，将单线程服务器的循环函数作为外部函数，并用线程调用
            client = Thread(target=dealWithClient,
                            args=(newSocket, clientAddr))
            client.start()

    # 无论是否有异常，关闭为这个客户端服务的套接字，若还需要服务，只能再次重新连接
    finally:
        tcpServer.close()


# 处理客户端的请求并执行事情
def dealWithClient(newSocket, clientAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print(f'recv[{clientAddr}]:{recvData}')
        else:
            print(f'[{clientAddr}]客户端已经关闭')
            break

    newSocket.close()


if __name__ == '__main__':
    main()
