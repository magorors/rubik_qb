import socket

HOST = "127.0.0.1"
PORT = 1235

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    to_send = input("Data to be sent: ")
    to_send = bytes(to_send, "utf-8")
    s.sendall(to_send)
    data = s.recv(1024)

data = data.decode('utf-8')
print(f"Received {data!r}")