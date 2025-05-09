import socket

def send(data):
    host = "127.0.0.1"
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print("waiting for connection...")
        conn, addr = sock.accept()
        with conn:
            print(f"connected by {addr}.")
            conn.sendall(data.encode())

print("what data would you like to send?")
stuff = input("> ")
send(stuff)