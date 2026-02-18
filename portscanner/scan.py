import socket
from datetime import datetime

def scan_ports(target, ports):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {str(datetime.now())}")
    print("-" * 50)

    try:
        for port in ports:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout so it doesn't hang forever
            socket.setdefaulttimeout(1)
            
            # Attempt to connect to the port
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\n[!] Exiting program.")
    except socket.gaierror:
        print("\n[!] Hostname Could Not Be Resolved.")
    except socket.error:
        print("\n[!] Server not responding.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP or Domain: ")
    
    # Common ports to check: 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443]
    
    scan_ports(target_ip, common_ports)
