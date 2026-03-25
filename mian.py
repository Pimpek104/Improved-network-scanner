from scapy.all import *
import socket
import os
import sys

if os.geteuid() != 0:
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

ip = socket.gethostbyname(socket.gethostname()).split('.')
ip[-1]=0
ip_string = '.'.join(str(part) for part in ip)
print(ip_string)

ans, _ = srp(
    Ether(dst="ff:ff:ff:ff:ff:ff") /
    ARP(pdst=f"{ip_string}/24"),
    timeout=2
)

for _, rcv in ans:
    print(rcv.psrc)
