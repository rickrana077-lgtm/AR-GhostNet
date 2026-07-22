import socket
from concurrent.futures import ThreadPoolExecutor
from utils.colors import Colors

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        self.target_ip = ""
        # কমন পোর্ট এবং তাদের সম্ভাব্য সার্ভিস নেম
        self.service_map = {
            21: "FTP (File Transfer Protocol)",
            22: "SSH (Secure Shell)",
            23: "Telnet",
            25: "SMTP (Email)",
            53: "DNS (Domain Name System)",
            80: "HTTP (Web Server)",
            110: "POP3 (Email)",
            443: "HTTPS (Secure Web)",
            445: "SMB (Windows Share)",
            3306: "MySQL (Database)",
            3389: "RDP (Remote Desktop)",
            8080: "HTTP-Proxy",
            8443: "HTTPS-Alt"
        }

    def grab_banner(self, s):
        """সার্ভার থেকে ব্যানার বা সার্ভিস ইনফরমেশন চুরি করা"""
        try:
            s.settimeout(1)
            banner = s.recv(1024).decode().strip()
            return banner if banner else "No banner detected (Stealthy)"
        except:
            return "Unknown Service"

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.7) # অপ্টিমাইজড টাইমআউট
                result = s.connect_ex((self.target_ip, port))
                if result == 0:
                    # পোর্ট ওপেন পেলে সাথে সাথে ব্যানার গ্র্যাব করার চেষ্টা করবে
                    service = self.service_map.get(port, "Unknown Service")
                    # আমরা এখানে ব্যানার গ্র্যাব করার জন্য আলাদা কানেকশন ট্রাই করছি
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                            s2.settimeout(1)
                            s2.connect((self.target_ip, port))
                            banner = self.grab_banner(s2)
                    except:
                        banner = "Filtered/No Response"
                    
                    return (port, service, banner)
        except Exception:
            pass
        return None

    def run(self):
        # ১. আইপি রেজোলিউশন
        print(f"{Colors.BLUE}[*] Target Locked: {self.target}")
        try:
            self.target_ip = socket.gethostbyname(self.target)
            print(f"{Colors.GREEN}[+] IP Resolved: {self.target_ip}")
        except socket.gaierror:
            print(f"{Colors.RED}[!] Critical Error: Could not resolve hostname. Check your target!")
            return

        # ২. পোর্ট রেঞ্জ সিলেক্ট করা (১ থেকে ১০২৪ পর্যন্ত স্ক্যান করবে)
        # তুই চাইলে এই রেঞ্জ আরও বাড়াতে পারিস (যেমন ১ থেকে ৬৫৫৩৫)
        ports_to_scan = range(1, 1025)
        print(f"{Colors.BLUE}[*] Initializing God-Mode Scan on 1024 ports...")
        print(f"{Colors.BLUE}[*] Threads: 100 | Mode: Stealth-Aggressive\n")
        print("-" * 50)
        print(f"{'PORT':<10} {'SERVICE':<20} {'BANNER/INFO'}")
        print("-" * 50)

        # ৩. মাল্টি-থ্রেডিং দিয়ে সুপার-ফাস্ট স্ক্যান
        with ThreadPoolExecutor(max_workers=100) as executor:
            # সব পোর্টকে একবারে সাবমিট করে দিচ্ছি
            results = executor.map(self.scan_port, ports_to_scan)
            
            for res in results:
                if res:
                    port, service, banner = res
                    # ওপেন পোর্ট পাওয়া গেলে সেটাকে গ্রিন করে প্রিন্ট করবে
                    print(f"{Colors.GREEN}{port:<10} {service:<20} {banner}{Colors.RESET}")
                    self.open_ports.append(port)

        # ৪. ফাইনাল রিপোর্ট এবং ভ্যালুয়েশন
        print("-" * 50)
        if self.open_ports:
            print(f"{Colors.GREEN}[+] Scan Complete! Found {len(self.open_ports)} open ports.")
            print(f"{Colors.YELLOW}[!] Advice: Now use 'The Blade' or 'The Key' on these ports.")
        else:
            print(f"{Colors.RED}[!] No open ports found. Target is heavily shielded.")
        print("-" * 50)