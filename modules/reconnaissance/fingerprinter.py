# AR-GhostNet | Server Fingerprinting Engine (UPGRADED)
# Location: modules/reconnaissance/fingerprinter.py

import requests
from utils.colors import Colors
from config.settings import Settings
from core.network_manager import NetworkManager

class Fingerprinter:
    def __init__(self):
        self.timeout = Settings.DEFAULT_TIMEOUT
        # Use the stealthy NetworkManager for requests
        self.net = NetworkManager()

    def analyze(self, url):
        print(f"{Colors.CYAN}[*] The Mimic: Analyzing server signatures for {url}...{Colors.RESET}")
        
        try:
            # Send a stealthy GET request using NetworkManager
            response = self.net.send_request('GET', url)
            
            if response is None:
                Colors.log_error("Failed to get response from target.")
                return

            headers = response.headers
            
            print(f"\n{Colors.YELLOW}--- Server Fingerprint Results ---{Colors.RESET}")
            
            # 1. Server Header (The most important part)
            server = headers.get("Server", "Unknown/Hidden")
            print(f"{Colors.GREEN}[+] Server: {server}{Colors.RESET}")
            
            # 2. Technology Detection via X-Powered-By
            powered_by = headers.get("X-Powered-By", "Unknown")
            print(f"{Colors.GREEN}[+] Powered By: {powered_by}{Colors.RESET}")
            
            # 3. Content-Type Analysis
            content_type = headers.get("Content-Type", "Unknown")
            print(f"{Colors.GREEN}[+] Content-Type: {content_type}{Colors.RESET}")
            
            # 4. Cookie Analysis (Often reveals the framework)
            cookies = headers.get("Set-Cookie", "")
            if cookies:
                print(f"{Colors.GREEN}[+] Cookies detected: {cookies}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}[-] No cookies found.{Colors.RESET}")

            print(f"{Colors.YELLOW}---------------------------------{Colors.RESET}")

        except Exception as e:
            Colors.log_error(f"Error analyzing target: {str(e)}")

    def start(self):
        print(f"{Colors.CYAN}--- THE MIMIC: Server Fingerprinting ---{Colors.RESET}")
        target_url = input(f"{Colors.GREEN}Enter Target URL (e.g. http://example.com): {Colors.RESET}")
        
        if not target_url.startswith("http"):
            print(f"{Colors.RED}[!] Error: URL must start with http:// or https://{Colors.RESET}")
            return

        self.analyze(target_url)

# For standalone testing
if __name__ == "__main__":
    mimic = Fingerprinter()
    mimic.start()