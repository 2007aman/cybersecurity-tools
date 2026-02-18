# Network Port Scanner 🛰️

A lightweight, high-performance Python tool designed for network reconnaissance. This script utilizes the `socket` library to identify open TCP ports on a target host, helping security researchers map the attack surface of a system.

## 🚀 Features
- **TCP Connect Scanning:** Implements the `connect_ex` error-indicator method for efficient scanning.
- **Service Identification:** Configured to scan the most common industrial ports (HTTP, HTTPS, SSH, FTP, etc.).
- **User-Friendly Interface:** Supports both IP addresses and Domain Names (DNS resolution).
- **Safe Execution:** Includes a built-in timeout and exception handling for connection resets and keyboard interrupts.

## 🛠️ Requirements
- Python 3.x
- No external dependencies (uses standard library `socket` and `datetime`).

## 📖 How to Use
1. Run the script:
   ```bash
   python port_scanner.py
