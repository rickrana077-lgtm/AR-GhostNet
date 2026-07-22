import socket
from concurrent.futures import ThreadPoolExecutor
from core.colors import Colors # তোর colors ফাইল থেকে কালার নিচ্ছি

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def scan_port(self, port):
        """একটি নির্দিষ্ট পোর্ট চেক করে তা খোলা কি না তা যাচাই করে"""
        try:
            # socket.AF_INET = IPv4, socket.SOCK_STREAM = TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5) # টাইমআউট কমিয়েছি যাতে স্পিড বাড়ে
                result = s.connect_ex((self.target, port))
                if result == 0:
                    return port
        except Exception:
            pass
        return None

    def run(self):
        print(f"{Colors.BLUE}[*] Resolving target {self.target}...")
        try:
            target_ip = socket.gethostbyname(self.target)
            print(f"{Colors.GREEN}[+] Target IP found: {target_ip}")
        except socket.gaierror:
            print(f"{Colors.RED}[!] Could not resolve hostname.")
            return

        # কমন পোর্টগুলোর একটা লিস্ট, তবে ইউজার চাইলে রেঞ্জ দিতে পারবে
        common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 1080, 3306, 3389, 8080]
        
        print(f"{Colors.BLUE}[*] Scanning common ports and range 1-1024...")
        
        # ১ থেকে ১০২৪ পর্যন্ত সব পোর্ট + কমন পোর্টগুলোর সেট
        target_ports = sorted(list(set(range(1, 1025) + common_ports)))

        with ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(self.scan_port, target_ports)

        for port in results:
            if port:
                self.open_ports.append(port)

        if self.open_ports:
            print(f"{Colors.GREEN}[+] Scan Complete! Found {len(self.open_ports)} open ports:")
            for p in sorted(self.open_ports):
                print(f"{Colors.GREEN}[!] Port {p} is OPEN")
        else:
            print(f"{Colors.RED}[!] No open ports found. Target is heavily shielded.")
