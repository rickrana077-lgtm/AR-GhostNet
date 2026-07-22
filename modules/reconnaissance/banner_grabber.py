# AR-GhostNet | Module: Banner Grabber (The Whisperer)
# Location: modules/reconnaissance/banner_grabber.py

import socket
from utils.colors import Colors
from core.network_manager import NetworkManager

class BannerGrabber:
    def __init__(self):
        self.net_manager = NetworkManager()

    def grab_banner(self, target, port):
        """Attempts to grab the service banner from a specific port."""
        try:
            # Create a socket connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3) # Give it a bit more time to respond
                s.connect((target, port))
                
                # Some services require a trigger to send the banner
                # We send a generic request to provoke a response
                s.send(b"HEAD / HTTP/1.1\r\n\r\n") 
                
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    return banner
                return "No banner returned (Silent Service)"
        except Exception as e:
            return f"Could not grab banner: {str(e)}"

    def start_grabbing(self, target, ports):
        """Grabs banners for a list of open ports."""
        # Resolve domain to IP
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            Colors.log_error(f"Invalid target: {target}")
            return

        Colors.log_info(f"Listening for whispers from {target} ({target_ip})...")
        
        for port in ports:
            Colors.log_info(f"Querying Port {port}...")
            banner = self.grab_banner(target_ip, port)
            if "Error" not in banner:
                Colors.log_success(f"[+] Port {port} Banner: {banner}")
            else:
                Colors.log_error(f"[-] Port {port}: {banner}")

    def start(self, target):
        """Wrapper method to get ports manually from user input."""
        print(f"{Colors.CYAN}[!] Enter the ports you want to grab banners from.")
        ports_input = input("Enter ports (comma separated): ").strip()
        if not ports_input:
            Colors.log_error("No ports provided.")
            return
        try:
            ports = [int(p.strip()) for p in ports_input.split(',')]
        except ValueError:
            Colors.log_error("Invalid port list. Please use numbers separated by commas.")
            return
        self.start_grabbing(target, ports)

# Testing Block
if __name__ == "__main__":
    grabber = BannerGrabber()
    target = input("Enter Target (e.g., google.com): ")
    grabber.start(target)