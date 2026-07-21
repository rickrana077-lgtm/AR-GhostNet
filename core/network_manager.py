# AR-GhostNet | Core Engine: Network Management
# Location: core/network_manager.py

import requests
import random
from utils.colors import Colors

class NetworkManager:
    def __init__(self):
        # List of realistic User-Agents to avoid Bot Detection
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0"
        ]
        self.session = requests.Session()

    def get_random_agent(self):
        """Returns a random User-Agent to bypass basic bot filters."""
        return random.choice(self.user_agents)

    def send_request(self, method, url, data=None, params=None, timeout=10):
        """
        A stealthy wrapper for sending HTTP requests.
        Handles headers and timeouts automatically.
        """
        headers = {
            'User-Agent': self.get_random_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

        try:
            if method.upper() == 'GET':
                response = self.session.get(url, headers=headers, params=params, timeout=timeout)
            elif method.upper() == 'POST':
                response = self.session.post(url, headers=headers, data=data, timeout=timeout)
            else:
                return None
            
            return response
        except requests.exceptions.Timeout:
            Colors.log_error(f"Request timed out for: {url}")
        except requests.exceptions.ConnectionError:
            Colors.log_error(f"Connection failed: {url}")
        except Exception as e:
            Colors.log_error(f"Unexpected Error: {str(e)}")
        
        return None

    def check_connectivity(self, target_url):
        """Quickly checks if the target is alive before starting heavy modules."""
        Colors.log_info(f"Checking connectivity to {target_url}...")
        response = self.send_request('GET', target_url)
        if response and response.status_code == 200:
            Colors.log_success(f"Target {target_url} is ONLINE.")
            return True
        else:
            Colors.log_error(f"Target {target_url} is OFFLINE or blocking requests.")
            return False


# Testing the Network Manager (Only runs when executed directly)
if __name__ == "__main__":
    net = NetworkManager()
    # Testing with a common site to verify if stealth requests are working
    test_url = "https://www.google.com"
    if net.check_connectivity(test_url):
        Colors.log_success("Network Manager is fully operational and stealthy.")
    else:
        Colors.log_error("Network Manager failed the connectivity test.")