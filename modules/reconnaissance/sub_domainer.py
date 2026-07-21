# AR-GhostNet | Sub-Domain Discovery Engine (UPGRADED)
# Location: modules/reconnaissance/sub_domainer.py

import os
import requests
from concurrent.futures import ThreadPoolExecutor
from utils.colors import Colors
from config.settings import Settings

class SubDomainer:
    def __init__(self, wordlist_path=None, threads=30):
        self.timeout = Settings.DEFAULT_TIMEOUT
        self.threads = threads
        self.found_subdomains = []
        
        # Load wordlist
        if wordlist_path and os.path.exists(wordlist_path):
            with open(wordlist_path, 'r', errors='ignore') as f:
                self.common_subdomains = [line.strip() for line in f if line.strip()]
        else:
            # Default internal list
            self.common_subdomains = [
                "www", "mail", "ftp", "admin", "dev", "test", "staging", "api", 
                "blog", "vpn", "remote", "portal", "db", "jenkins", "git",
                "login", "dashboard", "panel", "cpanel", "webmail", "cdn", "static",
                "images", "assets", "files", "download", "uploads", "backup"
            ]

    def check_subdomain(self, domain, sub):
        """Checks a single subdomain for both HTTP and HTTPS."""
        targets = [
            f"http://{sub}.{domain}",
            f"https://{sub}.{domain}"
        ]
        
        for url in targets:
            try:
                response = requests.get(url, timeout=self.timeout)
                if response.status_code == 200:
                    self.found_subdomains.append(sub)
                    print(f"{Colors.GREEN}[+] Found Active Subdomain: {sub}.{domain} ({url}){Colors.RESET}")
                    break  # Stop checking the other protocol if one works
            except requests.exceptions.RequestException:
                pass  # Silent fail

    def discover(self, domain):
        print(f"{Colors.CYAN}[*] Ghost-Mapper: Launching multi-threaded subdomain scan on {domain}...{Colors.RESET}")
        print(f"{Colors.CYAN}[*] Scanning {len(self.common_subdomains)} subdomains using {self.threads} threads.{Colors.RESET}")
        self.found_subdomains = []
        
        # Multi-threaded execution
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(lambda sub: self.check_subdomain(domain, sub), self.common_subdomains)
        
        if not self.found_subdomains:
            print(f"{Colors.YELLOW}[-] No common subdomains found.{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}[!] Total Subdomains Found: {len(self.found_subdomains)}{Colors.RESET}")
            for sub in self.found_subdomains:
                print(f"  {Colors.GREEN}➜{Colors.RESET} {sub}.{domain}")
        
        return self.found_subdomains

    def start(self):
        print(f"{Colors.CYAN}--- THE GHOST-MAPPER: Sub-Domain Discovery ---{Colors.RESET}")
        target_domain = input(f"{Colors.GREEN}Enter Target Domain (e.g., google.com): {Colors.RESET}")
        
        if not target_domain:
            print(f"{Colors.RED}[!] Domain cannot be empty.{Colors.RESET}")
            return

        self.discover(target_domain)

# For standalone testing
if __name__ == "__main__":
    mapper = SubDomainer()
    mapper.start()