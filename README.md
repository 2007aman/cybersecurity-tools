Cybersecurity Python Suite

A collection of professional-grade cybersecurity tools developed in Python. This repository covers multiple domains including network reconnaissance, cryptography, forensic tracking, and social engineering defense.
🚀 Tools Included
1. Network Geo Tracker (/Network-Geo-Tracker)

    Purpose: Traces the physical location of an IP address.

    Guidance: Run the script and input a target IP address. It uses external APIs to fetch the City, Country, and Coordinates of the host.

    Key Skills: API integration, JSON parsing, OSINT.

2. File Encryptor (/encryptor)

    Purpose: Securely locks and unlocks files using the Fernet (AES-128) standard.

    Guidance: 1. Run the script to generate a key.
    2. Use the encrypt function to hide file contents.
    3. Use the same key to decrypt. Warning: If you lose the key, the data is unrecoverable.

    Key Skills: Symmetric Cryptography, File I/O.

3. Nmap Tool Wrapper (/nmap-tool)

    Purpose: A Python-based interface for the industry-standard Nmap scanner.

    Guidance: Requires Nmap installed on the system. It automates common scan types like OS detection and service versioning.

    Key Skills: Subprocess management, Network auditing.

4. Password Cracker (/passwordcracker)

    Purpose: A dictionary-attack tool for MD5 hashes.

    Guidance: Provide an MD5 hash and a path to a wordlist (e.g., rockyou.txt). The tool hashes wordlist entries in real-time to find a match.

    Key Skills: Hashing algorithms, Algorithm efficiency.

5. Phishing Link Scanner (/phishinglink)

    Purpose: Detects typosquatting and "look-alike" URLs using fuzzy string matching.

    Guidance: Input a URL to check it against a database of trusted domains. It calculates a similarity score to flag potential scams.

    Key Skills: Levenshtein distance, URL parsing.

6. Port Scanner (/portscanner)

    Purpose: Scans a target IP for open TCP ports.

    Guidance: Enter a hostname or IP. The tool checks common ports (80, 443, 22, etc.) to identify the target's attack surface.

    Key Skills: Socket programming, TCP/IP networking.

7. Network Sniffer (/sniffertool)

    Purpose: Captures and analyzes live network traffic.

    Guidance: Requires administrative/sudo privileges. It monitors packets passing through your network interface and displays headers.

    Key Skills: Raw sockets, Packet header analysis.

🛠️ Installation & Setup

    Clone the Repository:

    Set up a Virtual Environment:

    Install Dependencies:

⚠️ Ethical Disclosure & Disclaimer

For Educational and Ethical Testing Only. This suite is designed to help security researchers and students understand common vulnerabilities. Unauthorized use of these tools against systems you do not own or have explicit permission to test is illegal and unethical. The developer is not responsible for any misuse of this software.
⚖️ License

This project is licensed under the MIT License.

Developed by AMAN KUMAR
