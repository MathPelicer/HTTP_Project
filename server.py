from socket import *
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
                split_request = request.split()

                if split_request[0] == "GET":
                    params = split_request[1]

                    # procura arquivo solicitado
                    # se achar 200 OK
                    # se nao, 404 not found

                    test = find_files('index.html', PATH)
                    print(test)

                    print("Solicitação do tipo GET, buscando o recurso {}".format(params))

                    response = ("200 OK").encode()
                    connectionSocket.send(response)

                elif split_request[0] == "POST":
                    print("post code")

                    params = split_request[1]
                    print("Solicitação do tipo POST, buscando o recurso {}".format(params))

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

                    response = ("ERRO! Servidor não reconhece esse comando!").encode()
                    connectionSocket.send(response)
                    
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