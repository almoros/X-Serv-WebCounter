#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket


# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

cont = 6

def counter():
    global cont;

    if cont == 0:
        cont = 5
    else:
        cont -= 1
    return cont

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        solicitud = str(recvSocket.recv(2048), 'utf-8')
        print ('Answering back...')
        resource = solicitud.split(" ")[1]
        print(resource)

        if resource == "/contador":
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1> CUENTA ATRÁS... " + str(counter()) + "</p>" + "</h1></body></html>" + "\r\n", 'ISO-8859-1'))

        else:
            recvSocket.send(bytes("HTTP/1.1 404 KO\r\n\r\n" +
                            "<html><body><h1>404 KO!</h1></body></html>" +
                            "<img src='http://sr.photos2.fotosearch.com/bthumb/CSP/CSP992/k13916036.jpg'></h1></body></html>" + "\r\n", 'ISO-8859-1'))

        recvSocket.close()

except KeyboardInterrupt:
	print ("Closing binded socket")
mySocket.close()
