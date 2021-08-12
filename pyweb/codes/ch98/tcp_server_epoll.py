import socket as s
import select as sl

# 创建套接字
tcpServer = s.socket(s.AF_INET, s.SOCK_STREAM)
tcpServer.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
tcpServer.bind(('', 8080))
tcpServer.listen(5)
# 创建一个epoll对象
epoll = sl.epoll()
# epoll.register(FD[, eventmask])
# 注册事件到epoll中，若FD已经注册过，则会发生异常
# 将创建的套接字的文件描述符添加到epoll的事件监听中
epoll.register(tcpServer.fileno(), sl.EPOLLIN | sl.EPOLLET)

clientDict = {}
addressDict = {}

while True:
    # 扫描确定符合要求的套接字，未指定超时时间，则为阻塞等待
    # poll返回值为(FD, events)元组
    epollList = epoll.poll()
    # 对事件进行判断
    for fd, events in epollList:
        # 若是主进程套接字，则被激活
        if fd == tcpServer.fileno():
            newClient, clientAddr = tcpServer.accept()
            print(f'有新的客户端{clientAddr}')
            # 将 newClient 和 clientAddr 信息分别保存起来
            clientDict[newClient.fileno()] = newClient
            addressDict[newClient.fileno()] = clientAddr
            # 向epoll中注册，添加套接字为可接收事件
            epoll.register(newClient.fileno(), sl.EPOLLIN | sl.EPOLLET)

        # 当事件为可接收事件
        elif events == sl.EPOLLIN:
            # 从激活的FD上接收
            recvData = clientDict[fd].recv(1024)
            if len(recvData) > 0:
                print(f'recv:{recvData}')
            else:
                # 从epoll中移除该连接fd
                epoll.unregister(fd)
                # 主动关闭该连接fd
                clientDict[fd].close()
                print(f'{addressDict[fd]} is offline')
