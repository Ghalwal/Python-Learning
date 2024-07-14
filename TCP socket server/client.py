#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.8.196'

port = 444
clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()
print(message.decode('ascii'))
 