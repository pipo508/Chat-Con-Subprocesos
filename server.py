import socket
import threading

def handle_client(client_socket, address, clients, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            # Reenviar el mensaje a todos los clientes conectados
            for c in clients:
                if c != client_socket:
                    c.send(username.encode('utf-8'))
                    c.send(message.encode('utf-8'))
                    print(f"Mensaje de {username}: {message}")
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Conexión con {username} cerrada.")
    clients.remove(client_socket)
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Servidor escuchando en {host}:{port}")

    clients = []

    while True:
        client_socket, address = server.accept()
        username = client_socket.recv(1024).decode('utf-8')
        clients.append(client_socket)
        print(f"Conexión establecida con {username} [Host: {address[0]} Port: {port}]")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, address, clients, username))
        client_handler.start()

if __name__ == "__main__":
    main()
