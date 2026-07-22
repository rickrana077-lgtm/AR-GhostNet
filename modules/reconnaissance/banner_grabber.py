import socket
from concurrent.futures import ThreadPoolExecutor

class TheWhisperer:
    def __init__(self, target):
        self.target = target
        self.banners = {}

    def grab_banner(self, port):
        """Connects to a port and listens for the service banner."""
        try:
            # Creating a socket with a short timeout to avoid hanging
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                # Attempt to connect
                result = s.connect_ex((self.target, port))
                
                if result == 0:
                    # Some services require a probe to send a banner
                    # We send a generic request to trigger a response
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n") 
                    banner = s.recv(1024).decode(errors='ignore').strip()
                    
                    if banner:
                        self.banners[port] = banner
                    else:
                        self.banners[port] = "Open (Silent/No Banner)"
        except Exception:
            pass

    def run(self, open_ports):
        """
        Takes a list of open ports (usually from The Eye/Port Scanner) 
        and grabs banners for each.
        """
        print(f"\n[!] THE WHISPERER: LISTENING FOR SERVICE BANNERS")
        print(f"[*] Target: {self.target}")
        print("-" * 60)

        if not open_ports:
            print("[!] No open ports provided. Provide a list of ports to grab banners.")
            return

        # Multi-threaded grabbing for efficiency
        with ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(self.grab_banner, open_ports)

        if self.banners:
            print(f"{'PORT':<10} | {'SERVICE BANNER / INTEL'}")
            print("-" * 60)
            for port, banner in sorted(self.banners.items()):
                # Clean the banner to remove excess noise
                clean_banner = banner.split('\n')[0] # Get first line only
                print(f"{port:<10} | {clean_banner}")
        else:
            print("[!] No banners leaked. Target is likely using banner-grabbing protection.")

        print("-" * 60)
        print("[+] Banner Intelligence Gathering Complete.")

# Example for testing:
# whisper = TheWhisperer("scanme.nmap.org")
# whisper.run([22, 80, 443]) # Pass a list of open ports