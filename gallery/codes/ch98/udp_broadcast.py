import socket as s

# 创建UDP套接字
udp1 = s.socket(s.AF_INET, s.SOCK_DGRAM)
# 修改套接字设置，否则不能发送广播数据
udp1.setsockopt(s.SOL_SOCKET, s.SO_BROADCAST, 1)

# <broadcast>会自动检测广播的IP地址
dest = ('<broadcast>', 8080)

# 以广播的形式发送数据到本网络的所有电脑中
sendData = input('Message: ').encode('utf-8')
udp1.sendto(sendData, dest)
print('等待对方回复')

# 读取消息
while True:
    msg, address = udp1.recvfrom(2048)
    print(f'Received from {address}: {msg.decode("utf-8")}')
