"""
演示socket服务器开发
"""
import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定IP地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口
socket_server.listen(1)  # 传入一个整数值，去表示允许链接的数量

# 等待客户端连接
# result: tuple = socket_server.accept()
# conn = result[0]  # 客户端和服务端的链接对象
# address = result[1]  # 客户端的地址信息

conn, address = socket_server.accept()  # 二元元组，accept()方法是阻塞方法
print(f"接收到了客户端连接，客户端的信息是{address}")

while True:
    data = conn.recv(1024).decode("UTF=8")
    print(f"客户端发来的消息是：{data}")
    msg = input("请输入你要给客户端回复的消息：")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF=8"))
# # 发送回复消息,要使用conn对象
# data = conn.recv(1024).decode("UTF-8")  # recv接收的参数是缓冲区的大小，一般给1024，返回一个字节数组，也就是byte对象，不是字符串，可以通过decode方法转换成str
# print(f"客户端发来的消息是{data}")
# msg = input("请输入你要和客户端回复的消息：").encode("UTF-8")
# conn.send(msg)

# 关闭链接
conn.close()
socket_server.close()
