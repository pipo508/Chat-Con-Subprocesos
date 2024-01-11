import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Crear un socket del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen()

    print(f"Servidor escuchando en {HOST}:{PORT}")

    # Esperar a que un cliente se conecte
    conexion_cliente, direccion_cliente = servidor_socket.accept()
    with conexion_cliente:
        print(f"Conectado por {direccion_cliente}")

        # Manejar la conexión con el cliente
        while True:
            data = conexion_cliente.recv(1024)
            if not data:
                break
            print(f"Mensaje del cliente: {data.decode()}")
            conexion_cliente.sendall(data)
            
            # Enviar mensaje de vuelta al cliente
            mensaje_respuesta = input("Responder al cliente: ")
            conexion_cliente.sendall(mensaje_respuesta.encode())