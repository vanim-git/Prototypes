import socket

def start_backend_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)
    print(f"Backend server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} on port {port}")
        data = client_socket.recv(1024)
        if data:
            response = f"Response from backend {port}: {data.decode()}"
            client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == "__main__":
    port = int(input("Enter backend port (e.g., 5001, 5002, 5003): "))
    start_backend_server(port)