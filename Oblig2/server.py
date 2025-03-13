from socket import *
import sys # In order to terminate the program

#i will develop a server that handles one http req at a time
#the web server should accept and parse a http req 
#get the requested file from the server’s file system
# create an HTTP response message consisting of the requested file preceded by header line
# and then send the response directly to the client
# if the requested file is not present in the server, the server should sendan HTTP “404 Not Found” message back to the client



""""
Description:
This function takes a port and IP addresses from a user
and checks if the port and IP addresses are in the correct format
Arguments:
ip: holds the ip address of the server
port: port number of the server
Returns: true or false
"""


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Write your code here
#End of your code
while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    try:
#Write your code here
#End of your code
    message = #Write your code here #End of your code
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = #Write your code here #End of your code
#Send one HTTP header line into socket
#Write your code here
#End of your code
#Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
    connectionSocket.send(outputdata[i].encode())
    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
    except IOError:
#Send response message for file not found
#Write your code here
#End of your code
#Close client socket
#Write your code here
#End of your code
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data

