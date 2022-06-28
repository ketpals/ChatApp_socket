from os import close
import socket
if __name__=='__main__':

    try:
        host='127.0.0.1'
        port=2009
        clientSocket=socket.socket()
        clientSocket.connect((host,port))
        print("Successfully connected to server!!")
    except socket.error as m:
        print("Socket not created, nor connected...Error:- " +str(m))
        exit()
        
    while True:        
        clientMsg=input("Client: ")
        if len(str.encode(clientMsg))>0:
            clientSocket.send(str.encode(clientMsg))
        if clientMsg.lower()=="end":    # Client enters end for closing connection with server
            clientSocket.close()
            print("You have closed the connection from server!!!!")
            print("You can enter connect to re-establish connection!")
            while True:
                clientMsg=input()
                if clientMsg.lower()=="connect":   # Client enters connect for reconnecting with server
                    # Recreate the socket
                    clientSocket=socket.socket()
                    clientSocket.connect((host,port))
                    print("Yay!!!! Reconnected with server!")
                    break
        if clientMsg.lower()=="close":  # Exit program ???
            clientSocket.close()
            exit()
        serverMsg = str(clientSocket.recv(1024),"utf-8")      
        print("Server: "+serverMsg, end="\n")
            
