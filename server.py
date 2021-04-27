from socket import *
import os
import sys
import codecs

PATH = os.path.abspath(os.getcwd())
print(PATH)

def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


def Server():
    HOST = ''
    PORT = 9000

    server_socket = socket(AF_INET, SOCK_STREAM)
    orig = (HOST, PORT)
    server_socket.bind(orig)
    server_socket.listen(1)

    try:
        while(1):
            (connectionSocket, addr) = server_socket.accept()
            pid = os.fork()

            if pid == 0:
                print("Cliente {} conectado ao servidor".format(addr))

                request = connectionSocket.recv(1024).decode()
                print(f"Request -> {request}")
                split_request = request.split()
                print(f"Splited Request -> {split_request}")

                if split_request[0] == "GET":
                    params = split_request[1]

                    file_path = PATH + params

                    try:
                        html_file = open(file_path, 'r')

                        data = "HTTP/1.1 200 OK\r\n"
                        data += "Content-Type: text/html; charset=utf-8\r\n"
                        data += "\r\n"
                        data += html_file.read()

                        print("Solicitação do tipo GET, buscando o recurso {}".format(params))

                        connectionSocket.sendall(data.encode())
                        
                    except:
                        data = "HTTP/1.1 404 NOT FOUND\r\n"
                        data += "Content-Type: text/html; charset=utf-8\r\n"
                        data += "\r\n"
                        data += "<html><head></head><body><h1>404 Not Found</h1></body></html>"
                        connectionSocket.sendall(data.encode())    

                    # 403 
                    # 301 - movido

                elif split_request[0] == "POST":
                    print("post code")

                    # the vars sent by the POST request are on the last position
                    # of the split_request and if more than just a single variable
                    # they're sapareted by '&'
                    vars_list = split_request[-1]

                    if "&" in vars_list:
                        vars_list = vars_list.split('&')

                    print("====== POST REQUEST =====\n")
                    print(f"Recieved variables -> {vars_list}")

                    response = ("200 OK").encode()
                    connectionSocket.send(response)

                elif split_request[0] == "PUT":
                    print("put code")
                    params = split_request[1]
                    print("Solicitação do tipo PUT, buscando o recurso {}".format(params))

                    response = ("200 OK").encode()
                    connectionSocket.send(response)

                elif split_request[0] == "DELETE":
                    print("delete code")
                    params = split_request[1]
                    print("Solicitação do tipo DELETE, buscando o recurso {}".format(params))

                    response = ("200 OK").encode()
                    connectionSocket.send(response)

                else:
                    print("Comando não pode ser interpretado por esse servidor!")
                    data = "HTTP/1.1 400 Bad Request\r\n"
                    data += "Content-Type: text/html; charset=utf-8\r\n"
                    data += "\r\n"
                    data += "<html><head></head><body><h1>400 Bad Request</h1></body></html>"
                    connectionSocket.sendall(data.encode()) 
                    connectionSocket.close()
                    
                connectionSocket.close()
                sys.exit(0)
            else:
                connectionSocket.close()

    except KeyboardInterrupt:
        print("\n Shutting down... \n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

print("Access http://localhost:9000")
Server()