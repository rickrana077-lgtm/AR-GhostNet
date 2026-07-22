import requests
import re
from concurrent.futures import ThreadPoolExecutor

class TheFingerprinter:
    def __init__(self, target_url):
        # Ensure the URL has a scheme
        if not target_url.startswith("http"):
            self.target = f"http://{target_url}"
        else:
            self.target = target_url
        
        self.intel = {}

    def analyze_headers(self):
        """Extracts server software and OS details from HTTP headers."""
        try:
            response = requests.get(self.target, timeout=5)
            headers = response.headers
            
            # Extracting Server and X-Powered-By headers
            server = headers.get("Server", "Unknown")
            powered_by = headers.get("X-Powered-By", "Unknown")
            
            self.intel['Server'] = server
            self.intel['Technology'] = powered_by
            
            # Checking for common CMS footprints
            page_content = response.text.lower()
            if "wp-content" in page_content or "wordpress" in page_content:
                self.intel['CMS'] = "WordPress"
            elif "drupal" in page_content:
                self.intel['CMS'] = "Drupal"
            elif "joomla" in page_content:
                self.intel['CMS'] = "Joomla"
            else:
                self.intel['CMS'] = "Unknown/Custom"

        except Exception as e:
            self.intel['Error'] = f"Connection failed: {str(e)}"

    def check_common_files(self):
        """Fingerprinting by checking for common files like robots.txt or generators."""
        common_files = ["robots.txt", "favicon.ico", "generator", "readme.html"]
        found_files = []
        
        for file in common_files:
            try:
                url = f"{self.target}/{file}"
                res = requests.get(url, timeout=3)
                if res.status_code == 200:
                    found_files.append(file)
            except:
                pass
        
        self.intel['Interesting_Files'] = found_files if found_files else "None found"

    def run(self):
        print(f"\n[!] THE FINGERPRINTER: ANALYZING TARGET DNA")
        print(f"[*] Target: {self.target}")
        print("-" * 60)
        
        self.analyze_headers()
        self.check_common_files()
        
        if 'Error' in self.intel:
            print(f"[!] Error: {self.intel['Error']}")
        else:
            print(f"{'FIELD':<20} | {'SENSITIVE DATA'}")
            print("-" * 60)
            print(f"{'Server Software':<20} | {self.intel.get('Server')}")
            print(f"{'Tech Stack':<20} | {self.intel.get('Technology')}")
            print(f"{'CMS Detection':<20} | {self.intel.get('CMS')}")
            print(f"{'Leaked Files':<20} | {self.intel.get('Interesting_Files')}")
        
        print("-" * 60)
        print("[+] Fingerprinting Complete. Target Profiled.")

# Example for testing:
# fp = TheFingerprinter("testphp.vulnweb.com")
# fp.run()