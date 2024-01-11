import socket

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
    cliente_socket.connect((HOST, PORT))
    print(f"Conectado al servidor en {HOST}:{PORT}")

    # Enviar un mensaje al servidor
    mensaje = "Estoy mandando un menaje al servidor"
    cliente_socket.sendall(mensaje.encode())

    # Esperar la respuesta del servidor
    data = cliente_socket.recv(1024)
    print(f"Respuesta del servidor: {data.decode()}")
