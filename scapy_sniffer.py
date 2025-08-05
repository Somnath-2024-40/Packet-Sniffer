from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest
from colorama import init,Fore

init()
red=Fore.RED
yellow=Fore.YELLOW
blue=Fore.LIGHTBLUE_EX
green=Fore.GREEN
cyan=Fore.LIGHTCYAN_EX
reset=Fore.RESET

def sniff_packets(iface):
    if iface:
        sniff(prn= process_packet,iface= iface, store=False)
    else:
        sniff(prn = process_packet, store=False) 
def process_packet(packets):
    # TCP sniffing
    if packets.haslayer(TCP):
        src_ip = packets[IP].src
        dst_ip=packets[IP].dst
        src_port=packets[TCP].sport
        dst_port= packets[TCP].dport
        print(f"{yellow}[+] {src_ip} is using port {src_port} to connect {dst_ip} at port {dst_port}{reset}")
    # HTTP sniffing
    if packets.haslayer(HTTPRequest):
        url = packets[HTTPRequest].Host.decode() + packet[HTTPRequest].path.decode()
        method=packets[HTTPRequest].Method.decode()
        print(f"{red} [+] {src_ip} is making a HTTP request to {url} with method {method} {reset}")
    print(f"{green} [+] HTTP Data ")
    print(f"{cyan} {packets[HTTPRequest].show()}")

sniff_packets('Wi-Fi')


