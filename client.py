import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
    cliente_socket.connect((HOST, PORT))
    print(f"Conectado al servidor en {HOST}:{PORT}")

    while True:
        # Enviar un mensaje al servidor
        mensaje = input("Mensaje a enviar al servidor: ")
        cliente_socket.sendall(mensaje.encode())

        # Recibir la respuesta del servidor
        data = cliente_socket.recv(1024)
        print(f"Respuesta del servidor: {data.decode()}")
