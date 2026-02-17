import nmap3
import json
import sys

def scan_target(host):
    """
    Performs a top-port scan on a given host.
    """
    nmap = nmap3.Nmap()
    try:
        print(f"[*] Initializing scan for: {host}")
        results = nmap.scan_top_ports("192.168.1.1")
        os_results=nmap.nmap_os_detection("192.168.1.1")
       # version_results=nmap.nmap_version_Detection("192.168.1.1")
        # Pretty-print the results
        print(json.dumps(results, indent=4))
        print(json.dumps(os_results,indent=4))
        #print(json.dumps(version_results, indent=4))
        
    except Exception as e:
        print(f"[!] Error occurred: {e}")

if __name__ == "__main__":
    # You can now pass the host as a command line argument!
    target = sys.argv[1] if len(sys.argv) > 1 else "scanme.nmap.org"
    scan_target(target)
