A high-level Python automation script that interfaces with the Nmap engine to perform deep-packet inspection and active reconnaissance. This tool is designed to identify open services, software versions, and the underlying operating system of a target host.
 Key Capabilities

    OS Fingerprinting: Analyzes TCP/IP stack responses to identify the target Operating System (e.g., Cisco ASA, Linux, Windows) with accuracy percentages.

    Service Version Detection: Probes open ports to extract service banners and identify exact software versions (via -sV logic).

    Attack Surface Mapping: Automates the discovery of filtered vs. open ports to understand firewall behaviors.

    Structured Output: Generates JSON-formatted reports for integration into larger security workflows.

Prerequisites

    Nmap System Engine:
    Bash

    sudo apt update && sudo apt install nmap -y

    Python Dependencies:
    Bash

    pip install python-nmap3

 Execution

Because this tool performs Raw Socket manipulation for OS detection, it must be run with root privileges. To use the libraries from your virtual environment, use the absolute path:
Bash

sudo ./venv/bin/python3 nmap_scanner.py <target-ip>
