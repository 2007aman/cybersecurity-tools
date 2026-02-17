#usb tethering network sniffer
# the interface name enx3e0aa025da9b

from scapy.all import sniff,IP
interface="enx3e0aa025da9b"
probeReqs=[]

def sniffproves(p):
 if p.haslayer(IP):
   netName=p[IP].dst
   print(f"[+] active traffic to {netName}")
   if netName not in probeReqs:
     probeReqs.append(netName)
     print("[+] detected new probe request :" + str(netName))

sniff(iface=interface, prn=sniffproves,store=0)

