import random
import requests

class TheMimic:
    def __init__(self):
        # Real-world browser headers to fool WAFs
        self.browser_profiles = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            },
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-GB,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            },
            {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
        ]

    def get_random_profile(self):
        """
        Returns a random browser header profile to bypass fingerprinting.
        """
        return random.choice(self.browser_profiles)

    def bypass_waf(self, url, session):
        """
        Attempts to access a URL using a mimicked profile.
        """
        profile = self.get_random_profile()
        try:
            # We send the request with a highly realistic header set
            response = session.get(url, headers=profile, timeout=10)
            return response
        except Exception as e:
            return None

    def analyze_waf(self, response):
        """
        Checks the response headers to identify which WAF is protecting the target.
        """
        waf_signatures = {
            'cloudflare': 'CF-RAY',
            'akamai': 'X-Akamai-Edge',
            'aws': 'X-Amz-Cf-Id',
            'sucuri': 'X-Sucuri-ID'
        }
        
        headers = response.headers
        for waf, sig in waf_signatures.items():
            if sig in headers:
                return f"WAF Detected: {waf.upper()}"
        
        return "No obvious WAF detected or bypassed successfully."

# Example Usage for Testing:
# from requests import Session
# mimic = TheMimic()
# session = Session()
# res = mimic.bypass_waf("https://google.com", session)
# if res:
#     print(mimic.analyze_waf(res))