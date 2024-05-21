import socket
ip = input("Ip input: ")
print (socket.gethostbyaddr(ip)[0])