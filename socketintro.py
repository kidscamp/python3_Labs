#!/usr/local/bin/python3

# This is intro to socket programming

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHOST: " + server + "\n\n"

s.connect((server,port))
s.send(request.encode())
request = s.recv(4096)
print(request)
