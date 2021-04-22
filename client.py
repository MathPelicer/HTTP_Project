from socket import *

serverName = "127.0.0.1"

#cria socket TCP, porta
#remota # 12000
serverPort = 8081
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
sentence = input("Digite algo em letra minúscula:")

#Envia a mensagem
sen = sentence.encode() #formata a mensagem
clientSocket.send(sen)  #chama encode para mandar 
modifiedSentence = clientSocket.recv(1024)

print("From Server: ", modifiedSentence.decode())
clientSocket.close()