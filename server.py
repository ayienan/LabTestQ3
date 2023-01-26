import random
import threading
import socket

quotes = ["“The elevator to success is out of order. You will have to use the stairs, one step at a time.” \t — Joe Girard",
          "“Be a positive energy trampoline, absorb what you need and rebound more back.” \t — Dave Carolan",
          "“People often say that motivation does not last. Well, neither does bathing, that is why we recommend it daily.” \t — Zig Ziglar",
          "“Just one small positive thought in the morning can change your whole day.” \t — Dalai Lama",
          "“I did rather regret the things I have done than regret the things I have not done.” \t —Lucille Ball",
          "“If you believe something needs to exist, if it is something you want to use yourself, do not let anyone ever stop you from doing it.” \t —Tobias Lütke",
          "“Someone is sitting in the shade today because someone planted a tree a long time ago.” \t — Warren Buffet"]

def handle_Client(client_Socket):
    quote = random.choice(quotes)
    client_Socket.sendall(quote.encode())
    client_Socket.close()

def main():
    bind_ip = "192.168.56.1" 
    bind_port = 8888

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))

    server.listen(5)
    print("[*] waiting for %s:%d requesting.." % (bind_ip, bind_port))

    while True:
        clients, addr = server.accept()
        print("[*] Got a connection from %s" % str(addr))
        client_Handler = threading.Thread(target=handle_Client, args=(clients,))
        client_Handler.start()
        
main()
