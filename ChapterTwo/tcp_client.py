import socket

target_host = "www.google.com"
target_port = 80

# create a socket object 
# AF_INET is the address family for IPv4
# SOCK_STREAM is the socket type for TCP connection
client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
client.connect((target_host, target_port))

# sending data 
# HTTP request send as bytes
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data 
# 4096 is the buffer size
response = client.recv(4096)

print(response.decode())
client.close()