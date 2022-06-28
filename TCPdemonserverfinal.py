from os import close
import socket
if __name__=='__main__':

    try:
        port=6969
        host=""
        s=socket.socket()
        print("Socket created")
    except socket.error as message:
        print("Socket not created....error." +str(message))

    try:
        s.bind((host,port))
        s.listen(10)
        print("Socket Binded")
    except socket.error as message2:
        print("socket could not bind.... error" +str(message2))

    connection,address=s.accept()
    print("Connected to Client with IP:" +address[0] + "and Port:" +str(address[1]))


    while True:
        msgfromclient=str(connection.recv(1024),"utf-8")
        print("CLient: "+msgfromclient, end="\n")
        if msgfromclient=="exit":
            print("Client disconnected....")
            connection,address=s.accept()
            print("Connected to Client with IP:" +address[0] + "and Port:" +str(address[1]))
            continue
        entry=input("Server: ")
        if entry=="exit":
            connection.close()
            s.close()
        if len(str.encode(entry))>0:
            connection.send(str.encode(entry))
