# AR-GhostNet | The Master Command Center
# Location: main.py

import os
import sys
from utils.colors import Colors
from config.settings import Settings

# Importing all modules
from modules.reconnaissance.port_scanner import PortScanner
from modules.reconnaissance.banner_grabber import BannerGrabber
from modules.reconnaissance.fingerprinter import Fingerprinter
from modules.exploitation.dir_bruter import DirBruter
from modules.exploitation.stresser import Stresser
from modules.exploitation.sqli_engine import SQLiEngine

class GhostNetMain:
    def __init__(self):
        self.version = "2.0 (Enterprise)"
        self.running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        banner = f"""
{Colors.CYAN}
  █████╗ ██████╗   ██████╗╗   ╗ ██████╗ ███╗   ██╗███████╗██████╗ 
 ██+   ███╗   ██  ██╔═══██╗ ╔╝ ██╔════╣ ████╗  ██║██╔════╝██╔══██╗
 ██   ███║   ██║  ██║   ██║ ║  ██║  ██║ ██lVert  ██║█████╗  ██████╗ 
 ██   ████║   ██║  ██║   ██║ ║  ██║  ██║ ██lVert  ██║██╔══╝  ██╔══██╗
 ╚█████╝╚██████╔╝  ╚██████╔╝ ╚╝ ╚██████╗ ██████╗██║██████╗ ██║  ██║
  ╚══════ ╚══════╝   ╚══════╝    ╚══════╝ ╚══════╝╚══════╝ ╚═╝  ╚═╝
           {Colors.YELLOW}>>> GHOST-NET FRAMEWORK {Colors.RESET} | Version: {self.version}
{Colors.RESET}"""
        print(banner)

    def main_menu(self):
        while self.running:
            self.clear_screen()
            self.show_banner()
            
            print(f"{Colors.WHITE}[+] Main Control Panel{Colors.RESET}")
            print(f"{Colors.YELLOW}--------------------------------------------------{Colors.RESET}")
            print(f"{Colors.CYAN} [1] {Colors.WHITE}The Eye (Port Scanner){Colors.RESET}")
            print(f"{Colors.CYAN} [2] {Colors.WHITE}The Whisperer (Banner Grabber){Colors.RESET}")
            print(f"{Colors.CYAN} [3] {Colors.WHITE}The Mimic (Fingerprinter){Colors.RESET}")
            print(f"{Colors.CYAN} [4] {Colors.WHITE}The Blade (Directory Bruter){Colors.RESET}")
            print(f"{Colors.CYAN} [5] {Colors.WHITE}The Key (SQLi Engine){Colors.RESET}")
            print(f"{Colors.CYAN} [6] {Colors.WHITE}The Hammer (Stresser/DDoS){Colors.RESET}")
            print(f"{Colors.RED} [0] {Colors.WHITE}Exit GhostNet{Colors.RESET}")
            print(f"{Colors.YELLOW}--------------------------------------------------{Colors.RESET}")
            
            choice = input(f"{Colors.GREEN}GhostNet-Shell > {Colors.RESET}")

            if choice == '1':
                PortScanner().start()
            elif choice == '2':
                BannerGrabber().start()
            elif choice == '3':
                Fingerprinter().start()
            elif choice == '4':
                DirBruter().start()
            elif choice == '5':
                SQLiEngine().start()
            elif choice == '6':
                Stresser().start()
            elif choice == '0':
                print(f"{Colors.RED}[!] Shutting down GhostNet...{Colors.RESET}")
                self.running = False
            else:
                print(f"{Colors.RED}[!] Invalid selection. Try again.{Colors.RESET}")
                input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

    def run(self):
        self.main_menu()

if __name__ == "__main__":
    app = GhostNetMain()
    app.run()