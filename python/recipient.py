import socket

def receive():
    host = "127.0.0.1"
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        data = sock.recv(1024)
        print(f"received data: {data.decode()}")

receive()