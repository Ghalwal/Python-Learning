import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.8.196'
port = 444

#Binding to socket
serversocket.bind((host, port))

#Starting TCP Listening
serversocket.listen(3)
print("Listening for incoming connections...")


while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("Recieved connection from %s " % str(address))
          
    message = 'Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    
    clientsocket.close()    
