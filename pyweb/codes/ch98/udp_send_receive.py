import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8090
# Normally use 1024, to get fast response from the server
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "Hello, World!"

# Create an AF_INET (IPv4), STREAM socket (TCP)
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print(
        f'Error occurred while creating socket. Error code: {e[0]}) , Error message: {e[0]}'
    )
    sys.exit()

# Sending message
connection = tcp_socket.connect((TCP_IP, TCP_PORT))
try:
    tcp_socket.send(MESSAGE_TO_SERVER)
    # infinite loop to keep the thread alive.
    while True:
        # Receiving data from client
        data = connection.recv(BUFFER_SIZE)
        reply = f'Data received: {data}'
        if not data:
            break
        # Exiting loop
        connection.sendall(reply)

except socket.error as e:
    print(
        f'Error occurred while creating socket. Error code: {e[0]}) , Error message: {e[0]}'
    )
    sys.exit()

print('Message to the server send successfully')

# Listen for incoming connections (max queued connections: 2)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(2)
print('Listening..')
# Waits for incoming connection (blocking call)
connection, address = tcp_socket.accept()
print(f'Connected with: {address}')
