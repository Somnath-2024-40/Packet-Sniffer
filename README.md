# Packet Sniffer

A simple network packet sniffer built using Python and Scapy.  
This tool captures TCP packets on a specified network interface and prints the source and destination IP addresses and ports in a color-coded format.

## Features

- Sniffs TCP packets on a given network interface
- Displays source IP and port and destination IP and port
- Color-coded terminal output using colorama for better readability

## Requirements

- Python 3.x
- [Scapy](https://scapy.net/)
- [colorama](https://pypi.org/project/colorama/)
- Run with administrator/root privileges (required for packet sniffing)
- On Windows, ensure [Npcap](https://npcap.com/) is installed with WinPcap compatibility mode

## Installation

1. Clone this repository:
