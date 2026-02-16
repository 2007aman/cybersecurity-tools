import dpkt
import socket
import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Your Location (Moradabad example)
MY_LAT = 28.8386 
MY_LON = 78.7733

def retKML(ip):
    try:
        rec = gi.record_by_name(ip)
        if rec:
            lat = rec['latitude']
            lon = rec['longitude']
            # LineString connects your Lon/Lat to Target Lon/Lat
            kml = (
                '<Placemark>\n'
                f'<name>{ip}</name>\n'
                '<styleUrl>#redLine</styleUrl>\n'
                '<LineString>\n'
                '<tessellate>1</tessellate>\n'
                f'<coordinates>{MY_LON},{MY_LAT} {lon},{lat}</coordinates>\n'
                '</LineString>\n'
                '</Placemark>\n'
            )
            return kml
    except:
        return ''
    return ''

def main():
    try:
        f = open('wire.pcap', 'rb')
        pcap = dpkt.pcap.Reader(f)
    except:
        print("Check if wire.pcap exists!")
        return

    kmlheader = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
        '<Style id="redLine"><LineStyle><color>ff0000ff</color><width>2</width></LineStyle></Style>\n'
    )
    kmlfooter = '</Document>\n</kml>\n'
    
    body = ""
    seen_ips = set() # THIS IS NEW: Prevents duplicate lines
    
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            
            ip = eth.data
            dst = socket.inet_ntoa(ip.dst)
            
            # Skip local IPs and IPs we already mapped
            if not dst.startswith(('192.', '10.', '127.')) and dst not in seen_ips:
                kml_segment = retKML(dst)
                if kml_segment:
                    body += kml_segment
                    seen_ips.add(dst) # Mark this IP as "mapped"
        except:
            continue
            
    with open('map_output.kml', 'w') as out:
        out.write(kmlheader + body + kmlfooter)
    print(f"Done! Mapped {len(seen_ips)} unique connections.")

if __name__ == '__main__':
    main()
