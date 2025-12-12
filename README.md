# Smart Network Behaviour Monitor

A Python-based tool to monitor network traffic, profile devices, and track the protocols.

## Project Goals

This tool is built to help you:
- Understand and implement network-level monitoring
- Gain hands-on experience with `scapy`, packet analysis, and protocol detection
- Build a showcase project for cybersecurity internships (SOC Analyst, Security Engineer, etc.)


##  Features

✅ Real-time device detection  
✅ Tracks MAC and IP addresses  
✅ Profiles communication protocols (TCP, UDP, ICMP, etc.)  
✅ Saves data to `devices.json`  
✅ Color-coded CLI alerts (via `colorama`)  
✅ Expandable for anomaly detection and alerting

## Phases 
- Phase 1: Device Profiling — capturing device MAC and IP addresses.
- Phase 2: Protocol Profiling — tracking protocols used by each device and updating their profiles.

##  Requirements

- Python 3.8+
- Windows or Linux (admin rights required for sniffing)
- [`Npcap`](https://nmap.org/npcap/) (Windows) or `libpcap` (Linux/macOS)


## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Smart-Network-Monitor.git
cd Smart-Network-Monitor

```

2. **Create and activate a virtual environment**
``` bash
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

```
3. **Install dependencies**
``` bash
pip install -r requirements.txt
```
- Python 3.x
- Scapy
- Colorama

4. **Install Npcap from the website (Windows only)**

## Running the script
You must run the script with Administrator privileges on Windows.

```bash
python Smart_Network.py

```
When started, the script will:
- Show available interfaces
- Begin sniffing on the default or selected interface
- Detect and display new devices and protocol changes
- Save data to devices.json when stopped via CTRL+C

## Example
<img width="1338" height="602" alt="example" src="https://github.com/user-attachments/assets/21f8abba-780e-4d95-959c-67c43485b956" />

## License

This project is open-source under the MIT License.
