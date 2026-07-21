# AR-GhostNet | The Brain
# Location: core/autopilot.py

from modules.reconnaissance.port_scanner import PortScanner
from modules.reconnaissance.fingerprinter import Fingerprinter
from modules.exploitation.dir_bruter import DirBruter
from core.report_manager import ReportManager
from utils.colors import Colors

class AutoPilot:
    def __init__(self):
        self.reporter = ReportManager()

    def run_full_scan(self, target):
        print(f"{Colors.YELLOW}[*] Auto-Pilot Engaged. Target: {target}{Colors.RESET}")
        print(f"{Colors.CYAN}[>] Initializing Sequential Attack Chain...{Colors.RESET}")

        # 1. Port Scanning
        print(f"\n{Colors.WHITE}[Step 1] Running Port Scanner...{Colors.RESET}")
        ps = PortScanner()
        # We assume ps.scan() returns the result as a string
        ports_result = ps.scan(target) 
        self.reporter.save_report(target, "Port Scanner", ports_result)

        # 2. Fingerprinting
        print(f"{Colors.WHITE}[Step 2] Running Fingerprinter...{Colors.RESET}")
        fp = Fingerprinter()
        finger_result = fp.identify(target)
        self.reporter.save_report(target, "Fingerprinter", finger_result)

        # 3. Directory Bruting
        print(f"{Colors.WHITE}[Step 3] Running Directory Bruter...{Colors.RESET}")
        db = DirBruter()
        dir_result = db.brute(target)
        self.reporter.save_report(target, "Directory Bruter", dir_result)

        print(f"\n{Colors.GREEN}[+] Full Scan Completed Successfully!{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] All logs have been archived by The Archivist.{Colors.RESET}")
        
        return f"Auto-Pilot sequence finished for {target}. Reports are in the /reports folder."

    def run_custom_chain(self, target, modules_to_run):
        """
        Allows the pal to define which modules they want to run in sequence.
        """
        print(f"{Colors.YELLOW}[*] Running Custom Chain for {target}...{Colors.RESET}")
        # Logic to loop through specified modules can be added here.
        pass