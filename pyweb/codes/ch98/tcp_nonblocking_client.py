import socket as s
from time import sleep

serverIp = input('请输入服务器的IP:')
connNum = input('请输入要链接服务器的次数:')
newList = []

for i in range(int(connNum)):
    tcpClient = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpClient.connect((serverIp, 7788))
    newList.append(s)
    print(i)

# 循环提示用户输入数据并发送
while True:
    for newSocket in newList:
        sendData = input('请输入要发送的数据：')
        if len(sendData) > 0:
            tcpClient.send(sendData.encode('utf-8'))
        else:
            break

        # 接收对方发送过来的数据，最大接收1024个字节
        recvData = tcpClient.recv(1024)
        print(f'接收到的数据为: {recvData}')

    # 用于测试用
    sleep(1)

# 关闭套接字
tcpClient.close()
