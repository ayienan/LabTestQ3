import socket

def main():
    # Set the IP and port of the server
    server_ip = "192.168.56.1"
    server_port = 8888

    # Create a socket 
    client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_Socket.connect((server_ip, server_port))

    # Request a quote from the server
    quote = client_Socket.recv(1024)
    print("Quotes of the Day for Today is !! : \n %s" % quote.decode())

    # Close the socket 
    client_Socket.close()

#execute main func
main()
