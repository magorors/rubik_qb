import socket

IPaddress = "192.168.10.100"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IPaddress, 4574))
    s.listen(5)
    print("Server is started")
    client, addr = s.accept()
    # print(s.accept())
    while True:
        algorithm =input("Enter string: ")
        print(algorithm)
        client.send(bytes(algorithm, "utf-8"))