import socket

def main():
    server_ip = "192.168.56.1"
    server_port = 8888

    client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_Socket.connect((server_ip, server_port))

    quote = client_Socket.recv(1024)
    print("Quotes of the Day for Today is !! : \n %s" % quote.decode())

    client_Socket.close()

main()
