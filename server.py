from socket import *
from multiprocessing import Process
import os
import sys

PATH = os.path.abspath(os.getcwd())

def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


def Server():
    HOST = ''
    PORT = 0

    serverSocket = socket(AF_INET, SOCK_STREAM)
    #orig = (HOST, PORT)
    #serverSocket.bind(orig)
    serverSocket.bind(('', 8888))
    serverSocket.listen()

    try:
        while(19):
            (connectionSocket, addr) = serverSocket.accept()
            print(addr)
            data = connectionSocket.recv(1024)
            print('Receive message from client: {0}'.format(data.decode()))

            connectionSocket.send("hello there by server".encode())
            connectionSocket.close()
            serverSocket.close
    except KeyboardInterrupt:
        print("\n Shutting down... \n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

print("Access http://localhost:9000")
Server()