import requests
import threading
from concurrent.futures import ThreadPoolExecutor

class TheGhostMapper:
    def __init__(self, domain):
        # Ensure domain doesn't have http/https prefix for DNS lookup
        self.domain = domain.replace("http://", "").replace("https://", "").split('/')[0]
        self.discovered_subdomains = []
        
        # Deadly Sub-domain Wordlist: Focuses on dev, staging, and admin environments
        self.wordlist = [
            "www", "mail", "ftp", "smtp", "pop", "http", "https", "ns1", "ns2",
            "dev", "development", "staging", "test", "api", "admin", "webmail",
            "vpn", "remote", "portal", "cloud", "db", "sql", "private", "corp",
            "internal", "auth", "login", "app", "beta", "old", "new", "m", "mobile"
        ]

    def resolve_subdomain(self, sub):
        # Construct the full subdomain URL
        subdomain = f"{sub}.{self.domain}"
        try:
            # We use requests to check if the subdomain is actually reachable (HTTP/HTTPS)
            # This is more reliable than simple DNS lookup for web targets
            response = requests.get(f"http://{subdomain}", timeout=3)
            if response.status_code == 200:
                print(f"[+] Found Active Subdomain: {subdomain} (Status: 200)")
                self.discovered_subdomains.append(subdomain)
        except requests.exceptions.ConnectionError:
            # This means the subdomain doesn't exist or isn't reachable via HTTP
            pass
        except Exception:
            pass

    def run(self):
        print(f"\n[!] THE GHOST-MAPPER: ACTIVATING SUB-DOMAIN RECON")
        print(f"[*] Mapping Target: {self.domain}")
        print("-" * 60)
        
        # High-speed execution using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(self.resolve_subdomain, self.wordlist)
        
        print("-" * 60)
        if self.discovered_subdomains:
            print(f"[+] Total Sub-domains Discovered: {len(self.discovered_subdomains)}")
            for sub in self.discovered_subdomains:
                print(f" >> {sub}")
        else:
            print("[!] No public sub-domains found. Target is tight or using wildcards.")
        
        print("-" * 60)
        print("[+] Domain Mapping Complete.")

# Example for testing:
# mapper = TheGhostMapper("google.com")
# mapper.run()