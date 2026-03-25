# Improved-network-scanner
A Python-based tool for discovering active devices on a local network using an efficient and clean approach.

## Why I Made it:
This project was created to improve my understanding of network scanning techniques in cybersecurity.  
It replaces my earlier approach, which relied on large IP arrays and inefficient processing, with a more optimized solution using packet-level interactions.


## Features
- Discovers active devices in a local network
- Uses ARP requests for efficient scanning
- Cleaner and more scalable implementation compared to previous version

## How It Works
The scanner uses the `scapy` library to send ARP requests across a specified IP range and listens for responses from active hosts.  
This approach is faster and more reliable than iterating through large lists of IP addresses manually.

Installation
```bash
git clone https://github.com/Pimpek104/improved-network-scanner.git
cd improved-network-scanner
pip install scapy
python scanner.py
