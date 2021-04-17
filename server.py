from socket import *
import os

PATH = os.path.abspath(os.getcwd())

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result


def Server():
    server_socket = socket(AF_INET, SOCK_STREAM)

    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)

        while(1):
            (client_socket, addr) = server_socket.accept()

            request = client_socket.recv(2048).decode()
            split_request = request.split()

            if split_request[0] == "GET":

                params = split_request[1]

                file_path = find_files(params, PATH)
                print(file_path)
                print("Solicitação do tipo GET, buscando o recurso {}".format(params))

                # supondo que a solicitação foi de sucesso
                response = ("200 OK").encode()
                client_socket.send(response)
            else:
                #imprimo um erro no servidor
                print("Comando não pode ser interpretado por esse servidor!")

                #crio uma mensagem de erro e envio ao cliente
                response = ("ERRO! Servidor não reconhece esse comando!").encode()
                client_socket.send(response)

    except KeyboardInterrupt:
        print("\n Shutting down... \n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

    server_socket.close()

print("Access http://localhost:9000")
Server()