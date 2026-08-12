# CodeAlpha Network Sniffer

## Overview

This project is a basic network packet sniffer developed in Python using the built-in `socket` library.

The purpose of the project is to capture network packets and display basic information about the traffic being observed.

## Features

The network sniffer can display:

* Source IP address
* Destination IP address
* Network protocol
* Packet size
* A short payload preview

The program recognizes common protocols including:

* TCP
* UDP
* ICMP

## Technologies Used

* Python 3
* Python `socket` library
* Windows Command Prompt

No external Python libraries are required.

## How It Works

The program creates a raw IPv4 socket and listens for network packets on the local network interface.

When a packet is received, the program extracts information from the IPv4 header, including the source IP, destination IP, and protocol.

It then displays the packet size and a short hexadecimal preview of the packet payload.

## How to Run

1. Open Command Prompt as Administrator.
2. Navigate to the project directory.
3. Run:

```text
python network_sniffer.py
```

4. The program begins displaying captured packets.
5. Press `Ctrl + C` to stop the capture.

## Example Output

The program produces output similar to:

```text
Source IP      : 192.168.x.x
Destination IP : xxx.xxx.xxx.xxx
Protocol       : TCP
Packet Size    : 60 bytes
Payload Preview: ...
```

## Learning Outcome

This project helped me understand basic packet structure, IPv4 headers, network protocols, raw sockets, and how network traffic can be inspected programmatically.

## Ethical Use

This tool is intended for educational purposes and should only be used on networks or systems where you have permission to monitor traffic.
