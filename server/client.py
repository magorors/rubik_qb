import socket
import time

HOST = "192.168.10.100"
<<<<<<< HEAD
PORT = 4597
=======
PORT = 4586
>>>>>>> 31007ee5b9798f9512c86db5fa8fab32ea17b57c
i = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        if i == 7:
            data = s.recv(1024)
            data = data.decode('utf-8')
            print(f"Received {data!r}")
            break
        to_send = input("Data to be sent: ")
        to_send = bytes(to_send, "utf-8")
        i += 1
        s.sendall(to_send)
        time.sleep(0.1)
        data = s.recv(1024)
        data = data.decode('utf-8')
        print(f"Received {data!r}")
