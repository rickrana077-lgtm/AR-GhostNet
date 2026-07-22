import requests
import concurrent.futures
import socket

class TheGhostMapper:
    def __init__(self):
        # High-power wordlist for subdomain discovery
        # In a real scenario, we can load a .txt file with 10k+ words
        self.wordlist = ['dev', 'test', 'api', 'admin', 'vpn', 'mail', 'staging', 'db', 'internal', 'cloud', 'app', 'portal']
        self.timeout = 2

    def resolve_subdomain(self, domain, subdomain):
        """
        Checks if a subdomain resolves to an IP address.
        """
        target = f"{subdomain}.{domain}"
        try:
            # Using socket.gethostbyname is faster than requests for DNS checks
            ip = socket.gethostbyname(target)
            return f"[+] Found Subdomain: {target} -> IP: {ip}"
        except socket.gaierror:
            return None

    def map_the_ghosts(self, main_domain):
        """
        The 'Deadly' part: Scans the domain for hidden infrastructure.
        """
        print(f"[*] Mapping the ghosts of: {main_domain}...")
        found_subdomains = []

        # Using ThreadPoolExecutor for high-speed DNS resolution
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            # Creating a list of tasks for each word in the wordlist
            futures = [executor.submit(self.resolve_subdomain, main_domain, sub) for sub in self.wordlist]
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    print(result)
                    found_subdomains.append(result)
        
        if not found_subdomains:
            print("[-] No hidden subdomains discovered.")
        
        return found_subdomains

# Example Usage:
# mapper = TheGhostMapper()
# mapper.map_the_ghosts("google.com")