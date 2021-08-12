import select as sl
import socket as s
import queue

# 保存客户端发送过来的消息，将消息放入队列中
message = {}
# 初始化select列表，内为可接收元素
inputs = []
# 初始化select列表，内为可发送元素
outputs = []


def main():
    tcpServer = s.socket(s.AF_INET, s.SOCK_STREAM)
    tcpServer.bind(('', 8085))
    tcpServer.listen(5)
    tcpServer.setblocking(False)
    # 添加套接字
    inputs.append(tcpServer)

    while True:
        # 开始监听，阻塞等待
        in_put, out_put, extra_put = sl.select(inputs, outputs, inputs)
        # 数据抵达，循环
        for obj in in_put:
            # 监听到有新的连接
            if obj == tcpServer:
                newClient, clientAddr = tcpServer.accept()
                print(f'Client {clientAddr} connected!')
                # select监听返回的客户端
                inputs.append(newClient)
                # 为连接的客户端单独创建一个消息队列，用于保存客户端发送的消息
                message[newClient] = queue.Queue()

            else:
                # 判断是否是客户端对象触发
                try:
                    # 读取客户端连接发送的数据
                    recvData = obj.recv(1024)
                    if len(recvData) > 0:
                        # 将收到的消息放入到各客户端的消息队列中
                        message[obj].put(recvData.decode('utf-8'))
                        # 若使用下面的语句，即为echo服务器
                        # obj.send(data)

                        # 将回复操作放到output列表中，让select监听
                        if obj not in outputs:
                            outputs.append(obj)

                except ConnectionResetError:
                    # 客户端断开连接了，移除select监听的客户端
                    inputs.remove(obj)
                    del message[obj]
                    print(f'inputs Client {clientAddr} disconnected')

        for sendobj in out_put:
            try:
                # 若消息队列中有消息，从消息队列中获取要发送的消息
                if not message[sendobj].empty():
                    # 从该客户端对象的消息队列中获取要发送的消息
                    sendData = message[sendobj].get()
                    sendobj.send(sendData.encode('utf-8'))
                else:
                    # 将监听移除等待下一次客户端发送消息
                    outputs.remove(sendobj)

            except ConnectionResetError:
                # 客户端连接断开了
                outputs.remove(sendobj)
                del message[sendobj]
                print(f'outputs Client {clientAddr} disconnected')


if __name__ == '__main__':
    main()
