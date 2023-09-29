# Code adapted from Prof. Alghamdi's provided code.
from socket import *

# Create TCP server socket.
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 12345

# Bind the socket to server address and server port.
serverSocket.bind(('',serverPort))

# Listen to at most 1 connection at a time.
serverSocket.listen(1)
serverIP = gethostbyname_ex(getfqdn())[2][1]
print("The server is ready to receive on:", serverIP)
connectionSocket, addr = serverSocket.accept()
print("Connected to client:", addr)
equation = ''
while True:
    print("Waiting for equation to calculate.")
    equation = connectionSocket.recv(1024).decode()

    # Our end code.
    if equation == "0 / 0 =":
        connectionSocket.send(equation.encode())         
        print("Closing connection.")
        break

    print("Recieved equation:", equation)

    # Split the equation into it's individual parts.
    result = 0
    operation_list = equation.split()
    num1 = float(operation_list[0])
    operation = operation_list[1]
    num2 = float(operation_list[2])

    # Calculate the requested result.
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2   

    if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        connectionSocket.send("Error".encode())         
        print("Improper equation. Sending error.")
    else:    
        # Send the calculated result back to client server.
        print("Result sent to client:", result)
        connectionSocket.send(str(result).encode())
connectionSocket.close()
