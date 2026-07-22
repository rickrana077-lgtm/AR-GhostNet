import requests
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class NetworkManager:
    def __init__(self):
        # A wide list of User-Agents to mimic different browsers and OS
        # This prevents the target server from seeing a pattern (Stealth Mode)
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        ]
        
        # Setup a persistent session for better performance (Keep-Alive)
        self.session = requests.Session()
        
        # Setup Retry Strategy: If the server is lagging, it will try 3 times before giving up
        retry_strategy = Retry(
            total=3,
            backoff_factor=1, 
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get_random_ua(self):
        """Returns a random User-Agent from the list."""
        return random.choice(self.user_agents)

    def send_request(self, method, url, params=None, data=None, timeout=10):
        """
        The universal request handler. Every module (The Blade, The Key) 
        should use this instead of calling requests.get() directly.
        """
        headers = {
            'User-Agent': self.get_random_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        try:
            if method.upper() == 'GET':
                response = self.session.get(url, params=params, headers=headers, timeout=timeout)
            elif method.upper() == 'POST':
                response = self.session.post(url, data=data, headers=headers, timeout=timeout)
            else:
                return None
            
            return response
        except requests.exceptions.Timeout:
            # Silently handle timeout to avoid crashing the main loop
            return None
        except requests.exceptions.RequestException:
            # Handle DNS failures, Connection refused, etc.
            return None

    def validate_response(self, response):
        """
        Checks if the response is a valid 200 OK. 
        Used by The Blade and The Key to confirm a page exists.
        """
        if response is not None and response.status_code == 200:
            return True
        return False