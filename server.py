import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

clients = []

def broadcast(data, exclude_socket=None):
    for client in clients:
        if client != exclude_socket:
            try:
                client.sendall(data)
            except:
                pass

def handle_client(connect):
    while True:
        try:
            data = connect.recv(4096)
            if not data:
                break
            broadcast(data, exclude_socket=connect)
        except:
            break

    if connect in clients:
        clients.remove(connect)
    connect.close()


def main():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    server_socket.bind((HOST, PORT))

    server_socket.listen(5)
    print(f'Сервер запущено на {HOST}:{PORT}')
    while True:
        connect, address = server_socket.accept()
        print(f'Новенький доєднався')
        clients.append(connect)
        t = threading.Thread(target=handle_client, args=(connect,))
        t.start()

if __name__ == '__main__':
    main()