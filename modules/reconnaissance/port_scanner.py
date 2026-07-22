import socket
from concurrent.futures import ThreadPoolExecutor
from utils.colors import Colors

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        self.target_ip = ""

    def scan_port(self, port):
        """একটি নির্দিষ্ট পোর্ট চেক করে তা খোলা কি না তা যাচাই করে"""
        try:
            # socket.AF_INET = IPv4, socket.SOCK_STREAM = TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # টাইমআউট ০.৫ সেকেন্ড রাখা হয়েছে যাতে স্পিড এবং একুরেসি ব্যালেন্স থাকে
                s.settimeout(0.5) 
                result = s.connect_ex((self.target_ip, port))
                if result == 0:
                    return port
        except Exception:
            pass
        return None

    def run(self):
        # ১. আইপি রেজোলিউশন (URL থেকে IP বের করা)
        print(f"{Colors.BLUE}[*] Resolving target {self.target}...")
        try:
            self.target_ip = socket.gethostbyname(self.target)
            print(f"{Colors.GREEN}[+] Target IP found: {self.target_ip}")
        except socket.gaierror:
            print(f"{Colors.RED}[!] Critical Error: Could not resolve hostname/URL.")
            return

        # ২. টার্গেট পোর্ট সিলেকশন
        # কমন গুরুত্বপূর্ণ পোর্ট + ১ থেকে ১০২৪ পর্যন্ত সব পোর্ট
        common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 1080, 3306, 3389, 8080, 8443]
        target_ports = sorted(list(set(list(range(1, 1025)) + common_ports)))

        print(f"{Colors.BLUE}[*] Initializing Deadly Scan on {len(target_ports)} ports...")
        print(f"{Colors.BLUE}[*] Mode: High-Speed Multi-Threading (100 workers)")
        
        # ৩. মাল্টি-থ্রেডেড এক্সিকিউশন
        try:
            with ThreadPoolExecutor(max_workers=100) as executor:
                # ম্যাপ ফাংশন দিয়ে সব পোর্ট একসাথে স্ক্যান করা শুরু হবে
                results = executor.map(self.scan_port, target_ports)

            for port in results:
                if port:
                    self.open_ports.append(port)

        except KeyboardInterrupt:
            print(f"{Colors.RED}\n[!] Scan interrupted by user.")
            return

        # ৪. ফাইনাল রেজাল্ট আউটপুট
        print("-" * 40)
        if self.open_ports:
            print(f"{Colors.GREEN}[+] SCAN COMPLETE! Found {len(self.open_ports)} open ports:")
            for p in sorted(self.open_ports):
                print(f"{Colors.GREEN}[!] Port {p} is OPEN")
        else:
            print(f"{Colors.RED}[!] No open ports found. Target is heavily shielded or offline.")
        print("-" * 40)
