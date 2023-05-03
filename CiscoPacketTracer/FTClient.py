import socket

# Define the port and IP address to use
PORT = 12345
IP_ADDRESS = '127.0.0.1'

# Create a socket object
s = socket.socket()

# Connect to the server
s.connect((IP_ADDRESS, PORT))

print("Connected to server...")

# Receive the data from the server
data = s.recv(1024)

# Open a new file and write the data to it
with open("received_file.txt", "wb") as f:
    f.write(data)

# Close the connection and the socket
s.close()

print("File received successfully!")
