import socket

ip = '127.0.0.1'
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cone = (ip, port)
s.bind(cone)
s.listen(5)
cliente, srvidor = s.accept()
msg = cliente.recv(1024)
texto = msg.decode('utf-8')
print(texto)
s.close()