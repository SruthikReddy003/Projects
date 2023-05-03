import socket

# Define the port and IP address to use
PORT = 12345    
IP_ADDRESS = '127.0.0.1'

# Create a socket object
s = socket.socket()

# Bind the socket to a specific IP address and port
s.bind((IP_ADDRESS, PORT))

# Listen for incoming connections
s.listen(1)

print("Server started listening...")

# Accept a connection from a client
client_socket, client_address = s.accept()

print(f"Connection established with {client_address}")

# Open the file to be transferred
with open("D:/VSCode/Communication Systems/Y2S2/Trail.txt", "rb") as f:
    # Read the contents of the file
    data = f.read()

# Send the contents of the file to the client
client_socket.send(data)

# Close the connection and the socket
client_socket.close()
s.close()

print("File transferred successfully!")
