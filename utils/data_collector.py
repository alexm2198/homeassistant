import socket
from utils import globals

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("rob-dduta-wx", 64326)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            if data:
                print('received {!r}'.format(data))
            else:
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()
