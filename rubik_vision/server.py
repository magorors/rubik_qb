import socket
import rubik


class Server():

    def __init__(self, HOST="192.168.10.100", PORT=4597):
        self.HOST = HOST
        self.PORT = PORT

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen()
        print("WAITING FOR CLIENT CONNECTION")
        conn, addr = self.sock.accept()
        with conn:
            print(f"connect by {addr}")
            conn.setblocking(0)
            self.rubik = rubik.Rubik(False).run(conn)

        self.sock.close()


if __name__ == '__main__':
    RubikServer = Server()
    RubikServer.run()
    



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(data.decode('utf-8'))
#             conn.sendall(b"It's server")