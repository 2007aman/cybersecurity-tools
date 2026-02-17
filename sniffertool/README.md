# Network Traffic Sniffer

A lightweight, Python-based network analysis tool designed to monitor and log active IP traffic on a specific network interface. Built using the Scapy library, this tool is optimized for monitoring USB-tethered interfaces.

## 🔍 Features
* **Real-time Interception:** Capture and analyze IP-layer packets as they move through the interface.
* **Interface Targeting:** Configurable to listen on specific hardware interfaces (e.g., `enx...`).
* **Unique Probe Detection:** Automatically identifies and logs unique destination IP addresses to filter out redundant traffic data.
* **Sober Logging:** Clean console output for active traffic monitoring.

## 🛠️ Prerequisites
* **Python 3.x**
* **Scapy Library:** Install via pip:
  ```bash
  pip install scapy
