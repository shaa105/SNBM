# Smart network behaviour monitor project
# Phase 1 & 2: Device profiling (MAC/IP/Protocols)

import json
import os
from datetime import datetime
from scapy.all import sniff, Ether, IP, get_if_list
from colorama import Fore, Style, init

init(autoreset=True)

devices = {}

def load_devices():
    global devices
    if os.path.exists("devices.json"):
        with open("devices.json", "r") as f:
            try:
                devices = json.load(f)
            except json.JSONDecodeError:
                devices = {}

def save_devices():
    with open("devices.json", "w") as f:
        json.dump(devices, f, indent=4)

def process_packet(packet):
    if Ether in packet and IP in packet:
        src_mac = packet[Ether].src
        src_ip = packet[IP].src
        proto = packet[IP].proto
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if src_mac not in devices:
            devices[src_mac] = {
                "ip": src_ip,
                "protocols": [proto],
                "last_seen": now,
                "total_packets": 1
            }
            print(Fore.GREEN + f"[NEW DEVICE] {src_mac} ({src_ip}) - protocol {proto}")
        else:
            if proto not in devices[src_mac]["protocols"]:
                devices[src_mac]["protocols"].append(proto)
                print(Fore.YELLOW + f"[NEW PROTOCOL] {proto} detected from {src_mac}")

            devices[src_mac]["last_seen"] = now
            devices[src_mac]["total_packets"] += 1

def select_interface():
    interfaces = get_if_list()
    print("Available interfaces:")
    for idx, iface in enumerate(interfaces):
        print(f"{idx}: {iface}")
    while True:
        choice = input("Select interface by number: ")
        if choice.isdigit() and 0 <= int(choice) < len(interfaces):
            return interfaces[int(choice)]
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    iface = select_interface()
    try:
        load_devices()
        print(Fore.BLUE + f"[*] Monitoring started on interface '{iface}'. Press CTRL+C to stop...\n")
        sniff(prn=process_packet, store=0, iface=iface)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Stopping and saving devices...")
        save_devices()
        print(Fore.GREEN + "[✓] Devices saved to devices.json")
