from os import close
import socket


if __name__=='__main__':
    try:
        port=2009
        host=""
        #Creating the socket
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("->Socket has been successfully created!")
    except socket.error as m1:
        print("Socket could not be created....ERROR:- " +str(m1))
        exit()
        
    try:
        serverSocket.bind((host,port))
        serverSocket.listen(10)
        print("->Socket was successfully Binded\n Server is now waiting for client to connect")
    except socket.error as m2:
        print("->socket could not bind.... ERROR:- " +str(m2))

    connection , clientAddress = serverSocket.accept()
    print("->Connected to Client with IP:" +clientAddress[0] + "and Port:" +str(clientAddress[1]))
    
    while True:
        clientMsg=str(connection.recv(1024),"utf-8")
        print("Client: " + clientMsg, end="\n")
        if clientMsg.lower()=="end":
            print("Client disconnected....")
            connection,address=serverSocket.accept()
            print("ReConnected to Client!!!")                    
        entry=input("Server: ")            
        if len(str.encode(entry))>0:
            connection.send(str.encode(entry))
