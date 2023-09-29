# Code adapted from Prof. Alghamdi's provided code.
from socket import *
 
# Our host and port we will be using for our calculator.
serverName = "eustis3.eecs.ucf.edu"
serverPort = 12345

# Our TCP connection with the server above.
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
 
while True:
    print("Enter '0 / 0 =' to end both client and server program. Otherwise...")
    print("Enter the operation you wish to compute in the format 'x OP y =':")
    
    # Get input from user.
    inp = input()

    clientSocket.send(inp.encode())
 
    # Recieve answer from server.
    answer = clientSocket.recv(1024).decode()
    if (answer == "0 / 0 ="):
        print("Closing connection.")
        break
    elif (answer == "Error"):
        print("Input error. Re-type the math question again.")
    else:
        print("Answer from server: " + answer)
 
clientSocket.close()