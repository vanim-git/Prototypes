import socket
import select

class L4LoadBalancer:
    def __init__(self, host, port, backend_servers):
        self.host = host
        self.port = port
        self.backend_servers = backend_servers
        self.server_socket = None
        self.client_to_backend = {}  # Maps client sockets to backend sockets
        self.backend_index = 0  # For round-robin selection

    def start(self):
        """Starts the load balancer."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(100)

        print(f"[*] Load balancer started on {self.host}:{self.port}")
        
        self.run()

    def run(self):
        """Main event loop for handling connections."""
        sockets_list = [self.server_socket]

        while True:
            readable, _, exceptional = select.select(sockets_list, [], sockets_list)

            for sock in readable:
                if sock is self.server_socket:
                    self.accept_new_connection(sockets_list)
                else:
                    self.forward_traffic(sock, sockets_list)

            for sock in exceptional:
                self.close_connection(sock, sockets_list)

    def accept_new_connection(self, sockets_list):
        """Accepts a new client connection and forwards it to a backend server."""
        client_socket, client_address = self.server_socket.accept()
        backend_socket = self.get_next_backend()

        if backend_socket:
            self.client_to_backend[client_socket] = backend_socket
            self.client_to_backend[backend_socket] = client_socket

            sockets_list.extend([client_socket, backend_socket])

            print(f"[+] New connection from {client_address} -> Forwarding to {backend_socket.getpeername()}")
        else:
            print("[!] No backend servers available, rejecting connection.")
            client_socket.close()

    def forward_traffic(self, sock, sockets_list):
        """Handles data forwarding between clients and backend servers."""
        data = sock.recv(4096)
        if data:
            peer_socket = self.client_to_backend.get(sock)
            if peer_socket:
                peer_socket.sendall(data)
        else:
            self.close_connection(sock, sockets_list)

    def close_connection(self, sock, sockets_list):
        """Closes a connection and removes it from the tracking list."""
        peer_socket = self.client_to_backend.pop(sock, None)
        if peer_socket:
            self.client_to_backend.pop(peer_socket, None)
            sockets_list.remove(peer_socket)
            peer_socket.close()

        sockets_list.remove(sock)
        sock.close()

        print(f"[-] Connection closed: {sock}")

    def get_next_backend(self):
        """Selects the next backend server in a round-robin fashion."""
        if not self.backend_servers:
            return None
        
        backend_ip, backend_port = self.backend_servers[self.backend_index]
        self.backend_index = (self.backend_index + 1) % len(self.backend_servers)

        try:
            backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            backend_socket.connect((backend_ip, backend_port))
            return backend_socket
        except Exception as e:
            print(f"[!] Failed to connect to backend {backend_ip}:{backend_port} - {e}")
            return None

if __name__ == "__main__":
    # Define backend servers (IP, Port)
    backend_servers = [
        ("127.0.0.1", 5001),
        ("127.0.0.1", 5002),
        ("127.0.0.1", 5003)
    ]

    load_balancer = L4LoadBalancer("0.0.0.0", 8080, backend_servers)
    load_balancer.start()
