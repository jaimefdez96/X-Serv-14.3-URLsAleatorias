#!/usr/bin/python3
"""
    Ejercicio URLs aleatorias
    Jaime Fernández Sánchez
"""

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)


try:
    while True:
        random_url = random.randrange(0,10000000000)
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><head><title>Ejercicio URLs aleatorias</title></head>" +
                        "<body><p>Hola. <a href = http://localhost:1234/" +
                        str(random_url) + 
                        ">Dame Otra ' ' </a></p></body></html>" +
                        "\r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
