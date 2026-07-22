# AR-GhostNet | Command Center (The Brain Integration)
# Location: main.py

import sys
from utils.colors import Colors
from core.autopilot import AutoPilot
from modules.reconnaissance.port_scanner import PortScanner
from modules.reconnaissance.fingerprinter import Fingerprinter
from modules.exploitation.dir_bruter import DirBruter
from modules.exploitation.sqli_engine import SQLiEngine
from modules.stresser.stresser import Stresser

class GhostNetMain:
    def __init__(self):
        self.running = True
        self.target = ""

    def clear_screen(self):
        print("\033[H\033[J", end="")

    def main_menu(self):
        while self.running:
            self.clear_screen()
            print(f"""{Colors.CYAN}
    ██████╗ ██████╗   ██████╗ ██╗  ██╗   ██╗███╗   ██╗██████╗ ██╗  ██╗██╗   ██╗███████╗
    ██╔════╝ ██╔═══██╗██╔════╝ ██║  ██║   ██║████╗  ██║██╔══██╗██║  ██║██║   ██║██╔════╝
    ██║     ██║   ██║ ██║  ██╗ ██║  ██║   ██║██╔██╗ ██║██║  ██║███████║██║   ██║█████╗ 
    ██║     ██║   ██║ ██║   ██║ ██║  ██║   ██║██║╚██╗██║██║  ██║██╔══██║██║   ██║██╔══╝ 
    ██████╗ ██║   ██║ ███████╗  ██║  ██║   ██║██║ ╚████║██████╔╝██║  ██║╚██╗ ███║██████╗ 
    ╚═════╝ ╚════╝╚══╝ ╚══════╝ ╚═╝  ╚═╝   ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚══╝ ╚══╝╚═════╝
                                 [ ENTERPRISE EDITION ]
            {Colors.RESET}""")
            
            print(f"{Colors.WHITE}Select an Operation:{Colors.RESET}")
            print(f"{Colors.YELLOW} [1] The Eye (Port Scanner){Colors.RESET}")
            print(f"{Colors.YELLOW} [2] The Whisperer (Fingerprinter){Colors.RESET}")
            print(f"{Colors.YELLOW} [3] The Blade (Directory Bruter){Colors.RESET}")
            print(f"{Colors.YELLOW} [4] The Key (SQLi Engine){Colors.RESET}")
            print(f"{Colors.YELLOW} [5] The Hammer (Stresser){Colors.RESET}")
            print(f"{Colors.GREEN} [6] THE BRAIN (Auto-Pilot Mode){Colors.RESET}")
            print(f"{Colors.RED} [0] Shutdown GhostNet{Colors.RESET}")
            print(f"{Colors.CYAN}--------------------------------------------------{Colors.RESET}")
            
            choice = input(f"{Colors.WHITE}GhostNet > {Colors.RESET}")

            if choice == '0':
                print(f"{Colors.RED}[!] Shutting down GhostNet...{Colors.RESET}")
                self.running = False
                break
            
            if choice in ['1', '2', '3', '4', '5', '6']:
                self.target = input(f"{Colors.YELLOW}Enter Target URL/IP: {Colors.RESET}")
                if not self.target:
                    print(f"{Colors.RED}[!] Target cannot be empty!{Colors.RESET}")
                    continue

                if choice == '1':
                    PortScanner(self.target).run()
                elif choice == '2':
                    Fingerprinter().identify(self.target)
                elif choice == '3':
                    DirBruter().brute(self.target)
                elif choice == '4':
                    SQLiEngine().run(self.target)
                elif choice == '5':
                    Stresser().launch(self.target)
                elif choice == '6':
                    AutoPilot().run_full_scan(self.target)
                
                input(f"\n{Colors.CYAN}[!] Operation complete. Press Enter to return to menu...{Colors.RESET}")

if __name__ == "__main__":
    try:
        app = GhostNetMain()
        app.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Forced shutdown detected. Exiting...{Colors.RESET}")
        sys.exit()