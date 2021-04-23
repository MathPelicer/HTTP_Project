import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))


s.send(b'Hello')
data = s.recv(1024)
print('Receive message from server: {0}'.format(data.decode()))


s.close()