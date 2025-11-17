import socket
import threading


class ChatServer:
    def __init__(self, host='127.0.0.1', port=123):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.addr = None
        self.socket_to_addr = {}
        self.clients = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        while True:
            print(f"Server listening on {self.host}:{self.port}")
            self.client_socket, self.addr = self.server_socket.accept()
            print("Connection from", self.addr)
            self.socket_to_addr[self.client_socket] = self.addr
            self.clients.append(self.client_socket)
            threading.Thread(target=self.handle_client, args=(self.client_socket, self.addr), daemon=True).start()


    def handle_client(self, client_socket, addr):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data or data.lower() == 'exit':
                    break
                print(f"{addr}: {data}")
                self.handle_data(client_socket,data)
            except ConnectionResetError:
                break
        print(f"Connection closed: {addr}")
        client_socket.close()
        self.clients.remove(client_socket)

    def handle_data(self,client_socket,data):  # send the message from one client to all the other clients
        for client in self.clients:
            if client != client_socket:
                client.sendall(data.encode('utf-8'))


if __name__ == "__main__":
    ChatServer().start()