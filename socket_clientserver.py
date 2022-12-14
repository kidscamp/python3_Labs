#!/usr/local/bin/python3

# This socket binding and listening.

from  _thread import *
import socket
import sys

host = ''
port = 5556

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)
print("Waiting for connection")

def threaded_client(conn):
    conn.send(str.encode('Welcome, Message'))

    while True:
        data = conn.recv(2048)
        reply = 'Server output : ' + data.decode('utf-8')

        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
 conn, addr = s.accept()

 print(conn)
 print('connected' + addr[0] + ':' + str(addr[1]))
 start_new_thread(threaded_client, (conn,))

