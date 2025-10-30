import socket
import threading


class ChatServer:
    def __init__(self, host='127.0.0.1', port=123):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.addr = None
        self.clients = {}
        self.clientCount = 0

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        self.client_socket, self.addr = self.server_socket.accept()
        print("Connection from", self.addr)
        self.clients[self.clientCount] = (client_socket, addr)
        threading.Thread(target=self.handle_client, args=(client_socket, addr), daemon=True).start()
        self.clientCount += 1

    def handle_client(self, client_socket, addr):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data or data.lower() == 'exit':
                    break
                print(f"{addr}: {data}")
                client_socket.send(f"Server received: {data}".encode('utf-8'))
            except ConnectionResetError:
                break
        print(f"Connection closed: {addr}")
        client_socket.close()
        self.clients.remove(client_socket)


if __name__ == "__main__":
    ChatServer().start()
