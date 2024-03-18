import time
from socket import *
import sqlite3
conn = sqlite3.connect('test.db')
conn.execute("INSERT INTO STUDENT (ID,NAME,DEPARTMENT) VALUES (?,?,?)",(self.id,self.name,self.department))

sensor1= bytes([0x01,0x03,0x00,0x04,0x00,0x01,0xC5,0xCB])
# 读获取传感器数据时用,地址是1
sensor2= bytes([0x02,0x03,0x00,0x04,0x00,0x01,0xC5,0xF8])
# 读获取传感器数据时用,地址是2


tcp_client_socket = socket(AF_INET, SOCK_STREAM)
server_ip = ("127.0.0.1", 8886)
tcp_client_socket.connect(server_ip)

tcp_client_socket.send(sensor2)
recvData = tcp_client_socket.recv(7)
data = recvData.hex()
print("sensor2测得的数据是：",data)
print("接收到的数据是：", data)
time.sleep(0.1)

tcp_client_socket.send(sensor1)
recvData = tcp_client_socket.recv(7)
data = recvData.hex()
print("sensor1测得的数据是：",data)
print("接收到的数据是：", data)

tcp_client_socket.close()
