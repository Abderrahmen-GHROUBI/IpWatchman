# PINGGing.py

import subprocess
import ipaddress
import time

def ping_ip(ip, packet_size, timeout=1000):
    try:
        
        ipaddress.ip_address(ip)

        def perform_ping():
            return subprocess.Popen(['ping', '-n', '1', '-l', str(packet_size), '-w', str(timeout), ip], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        
        output_decoded = perform_ping()
        
        if f'Reply from {ip}' in output_decoded:
            return True
        else:
            
            for _ in range(2):
                if "Destination host unreachable" in output_decoded:
                    return ip, "Destination host unreachable"
                elif "Request timed out" in output_decoded:
                    output_decoded = perform_ping()
                    if f'Reply from {ip}' in output_decoded:
                        return True

            
            if "Destination host unreachable" in output_decoded:
                return ip, "Destination host unreachable"
            elif "Request timed out" in output_decoded:
                return ip, "Request timed out"
            else:
                return ip, "Unknown error"
                
    except ValueError:
        return f"Invalid IP address: {ip}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    ip_address = "192.168.1.8"
    packet_size = 0.1
    timeout = 1000  

   
    print(ping_ip(ip_address, packet_size, timeout))

if __name__ == "__main__":
     while True:
        main()
        
