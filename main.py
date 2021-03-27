# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 4000  # port number
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        ﬁlename = message.split()[1]
        f = open(ﬁlename[1:])
        outputdata = f.read()  # read ontent of file
        # Fill in start
        connectionSocket.sendall('HTTP/1.1 200 OK\r\n\r\n'.encode())  # Send a HTTP header line
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:

        # Send response message for file not found
        # Fill in start
        connectionSocket.sendall(
            b'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<doctype html><html><body><h1>404 Not Found&#9785<h1></body></html>')
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
