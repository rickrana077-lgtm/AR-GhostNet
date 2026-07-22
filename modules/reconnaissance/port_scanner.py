import socket
import threading
from concurrent.futures import ThreadPoolExecutor

class TheEyeGodMode:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        # Common ports and their likely services
        self.service_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 
            8080: "HTTP-Proxy", 27017: "MongoDB"
        }

    def grab_banner(self, s):
        """Attempts to pull the service banner for detailed intel."""
        try:
            s.send(b'Hello\r\n') # Send a probe
            banner = s.recv(1024).decode().strip()
            return banner if banner else "No banner returned"
        except:
            return "Banner hidden"

    def scan_port(self, port):
        try:
            # Socket creation for the specific port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1) # Fast timeout for speed
                result = s.connect_ex((self.target, port))
                
                if result == 0: # Port is open
                    service = self.service_map.get(port, "Unknown Service")
                    banner = self.grab_banner(s)
                    self.open_ports.append((port, service, banner))
        except Exception:
            pass

    def run(self):
        print(f"\n[!] THE EYE: GOD MODE ACTIVATED")
        print(f"[*] Target Analysis: {self.target}")
        print("-" * 60)
        
        # Scanning common critical ports first for speed
        common_ports = list(self.service_map.keys())
        # Then scanning a broader range (1-1024)
        full_range = range(1, 1025)
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.scan_port, full_range)

        if self.open_ports:
            print(f"{'PORT':<10} {'SERVICE':<15} {'BANNER/INTEL'}")
            print("-" * 60)
            for port, service, banner in sorted(self.open_ports):
                print(f"{port:<10} {service:<15} {banner}")
        else:
            print("[!] No open ports detected. Target might be stealthy or firewalled.")
        
        print("-" * 60)
        print("[+] Intelligence Gathering Complete.")

# Example usage for testing:
# eye = TheEyeGodMode("testphp.vulnweb.com")
# eye.run()