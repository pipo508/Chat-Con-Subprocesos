import socket
import threading
import os

def receive_messages(client_socket):
    while True:
        try:
            username = client_socket.recv(1024).decode('utf-8')
            message = client_socket.recv(1024).decode('utf-8')
            print(f"{username}:{message}")
            
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Conexión establecida con {host}:{port}")

    # Solicitar el nombre al usuario
    username = input("Ingresa tu nombre: ")

    # Enviar el nombre al servidor
    client.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    count = 0
    while True:
        if count == 0:
            """print("\033[A\033[K", end='', flush=True)"""
            count += 1
        message = input(f"{username}:")
        if message == "exit":
            break
        client.send(username.encode('utf-8'))
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
