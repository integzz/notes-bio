import socket as s
from time import sleep

# 用于存储所有的新链接的socket
newList = []


def main():
    # 创建socket，并设置为可重复使用绑定信息
    tcpServer = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpServer.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    # 绑定本地信息
    localAddr = ('', 8080)
    tcpServer.bind(localAddr)
    connNum = input('请输入要链接服务器的次数:')
    tcpServer.listen(int(connNum))
    # 将套接字设置为非堵塞
    tcpServer.setblocking(False)

    while True:
        try:
            newSocket, clientAddr = tcpServer.accept()
        except:
            pass
        else:
            print(f'一个新的客户端到来:{(newSocket, clientAddr)}')
            # 将新套接字设置为非阻塞模式
            newSocket.setblocking(False)
            newList.append((newSocket, clientAddr))

        # 创建废弃客户端列表
        wasteList = []

        for newSocket, clientAddr in newList:
            try:
                recvData = newSocket.recv(1024)
                if len(recvData) > 0:
                    print(f'recv[{clientAddr}]:{recvData}')
                else:
                    print(f'[{clientAddr}]客户端已关闭')
                    newSocket.close()
                    # 添加已关闭的客户端到废弃客户端列表
                    wasteList.append((newSocket, clientAddr))
            except:
                pass

        # 遍历删除废弃客户端
        for wasteSocket in wasteList:
            newList.remove(wasteSocket)


if __name__ == '__main__':
    main()
