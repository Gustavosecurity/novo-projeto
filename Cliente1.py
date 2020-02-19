import socket

ip = '127.0.0.1'
port = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cone = (ip, port)
s.connect(cone)
texto = input('Digite uma mensagem a ser enviada')
s.send(texto.encode('utf-8'))
s.close()