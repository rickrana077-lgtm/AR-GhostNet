# AR-GhostNet | Module: Port Scanner (The Eye)
# Location: modules/reconnaissance/port_scanner.py

import socket
from concurrent.futures import ThreadPoolExecutor
from utils.colors import Colors
from core.network_manager import NetworkManager

class PortScanner:
    def __init__(self):
        self.net_manager = NetworkManager()
        # Common ports to scan first for speed, then full range if needed
        self.common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

    def scan_single_port(self, target, port):
        """Attempts to connect to a specific port to see if it's open."""
        try:
            # socket.AF_INET = IPv4, socket.SOCK_STREAM = TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5) # Fast timeout for speed
                result = s.connect_ex((target, port))
                if result == 0:
                    return port
        except Exception:
            pass
        return None

    def start_scan(self, target):
        """Main function to execute the scan using multi-threading."""
        # Resolve domain to IP if necessary
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            Colors.log_error(f"Could not resolve hostname: {target}")
            return

        Colors.log_info(f"Initiating Deadly Scan on: {target} ({target_ip})")
        Colors.log_info("Scanning common ports... Please wait.")
        
        open_ports = []
        
        # Using ThreadPoolExecutor to scan multiple ports simultaneously (Deadly Speed)
        with ThreadPoolExecutor(max_workers=100) as executor:
            # Mapping the scan function over the list of common ports
            results = executor.map(lambda p: self.scan_single_port(target_ip, p), self.common_ports)
            
            for port in results:
                if port:
                    open_ports.append(port)

        if open_ports:
            Colors.log_success(f"Scan Complete! Found {len(open_ports)} open ports:")
            for p in open_ports:
                print(f"{Colors.INFO} [!] Port {p} is OPEN")
        else:
            Colors.log_error("No open ports found. Target is heavily shielded.")

    def scan(self, target):
        """Wrapper for main.py compatibility."""
        self.start_scan(target)

# Testing Block
if __name__ == "__main__":
    scanner = PortScanner()
    target = input("Enter Target IP or Domain (e.g., google.com): ")
    scanner.start_scan(target)