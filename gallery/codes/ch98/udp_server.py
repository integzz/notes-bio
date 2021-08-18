import socket as s
from time import ctime


def main():
    # 创建UDP套接字
    udp1 = s.socket(s.AF_INET, s.SOCK_DGRAM)
    # 绑定本地网络地址信息，接收方必须创建
    bindAddr = ('', 8080)
    udp1.bind(bindAddr)

    num = 1
    while True:
        # 等待接收对方发送的数据
        recvData = udp1.recvfrom(1024).decode('gb2313')
        # 1024表示本次接收的最大字节数
        print(f'收到的第{num}个消息内容为:{recvData[0]}')
        num += 1
        # 加上下面的语句聊天室将被改造为Echo服务器
        # udp1.sendto(recvData[0].encode('gb2313'), recvData[1])
        print(f'将收到的第{num}个消息返回，时间为{ctime()}')

    # 关闭套接字
    udp1.close()


if __name__ == '__main__':
    main()
