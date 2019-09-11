#!/usr/bin/python
import Adafruit_DHT
import socket
from time import sleep

# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
server_address = ('rob-dduta-wx', 64326)

while True:
    try:
        print('connecting to {} port {}'.format(*server_address))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
    
        while True:
            # Send data
            hum, temp = Adafruit_DHT.read_retry(11, 14)
            hum = str(hum)
            temp = str(temp)
            message = hum + " " + temp
            byte_message = bytearray(message)
            print(message)
            sock.sendall(byte_message)
    except:
        sock.close()
        print('retrying')
        sleep(10)
