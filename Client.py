import socket
import threading
import time
import yaml


class ChatClient:
    def __init__(self, host='127.0.0.1', port=123):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = ""
        self.password = None

    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))
        except ConnectionError:
            print("The Client hasn't manage to connect to the server")
            return
        self.run()

    def run(self):
        self.log_in()
        if self.is_manager():
            self.name = "@" + self.name
        while True:
            threading.Thread(target=self.handle_input_server, daemon=True).start()
            message = input()
            if message:
                print(self.construct_message("You", message))

            if message.lower() == 'quit':
                message = self.name + " HAS QUIT THE CHAT!"
                self.client_socket.send(message.encode('utf-8'))
                break
            self.client_socket.send(self.construct_message(self.name,message).encode('utf-8'))
        self.client_socket.close()

    def log_in(self):  # add cryptography
        self.name = input("What's your username? ")
        self.password = input("What's your password? ")

    def handle_input_server(self):
        while True:
            data = self.client_socket.recv(1024).decode('utf-8')  # check how to recieve
            print(data)

    def construct_message(self, name, msg):
        if name != "You":
            name = self.name  # in order to make the function not static
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        return f"{hour:02d}:{minute:02d}" + " " + name + ": " + msg

    def is_manager(self):
        with open('config.yaml', 'r') as file:
            data = yaml.safe_load(file)
        if self.name in data["MANAGERS"]:
            return True
        return False


if __name__ == "__main__":
    ChatClient().start()
