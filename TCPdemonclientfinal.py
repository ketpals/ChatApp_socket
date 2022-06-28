from os import close
import socket
if __name__=='__main__':

    try:
        host='127.0.0.1'
        port=6969
        s=socket.socket()
        s.connect((host,port))
        
    except socket.error as message:
        print("Socket not created.nor connected...error." +str(message))
    while True:
        clientmsg=input("Client: ")
        if len(str.encode(clientmsg))>0:
            s.send(str.encode(clientmsg))
        if clientmsg=="exit":
            s.close()
            break
        datafromserver=str(s.recv(1024),"utf-8")
        if datafromserver=="exit":
            s.close()
        else: print("Server: "+datafromserver, end="\n")
            