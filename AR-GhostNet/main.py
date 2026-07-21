#!/usr/bin/env python3
# AR-GhostNet | Command Center (The Brain)
# Location: main.py

import os
import sys
import time
from utils.colors import Colors

# Importing our deadly modules
try:
    from modules.reconnaissance.port_scanner import PortScanner
    from modules.reconnaissance.banner_grabber import BannerGrabber
    from modules.exploitation.dir_bruter import DirBruter
    from modules.stresser.http_hammer import HTTPHammer
except ImportError as e:
    print(f"Critical Error: {e}")
    print("Make sure all modules are in the correct folders!")
    sys.exit()

class GhostNetMain:
    def __init__(self):
        self.running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        print(Colors.CYAN + r"""
    ####################################################
    #                                                    #
    #    ___     ____  _____  _   _  ___   _   _   _      #
    #   / _ \   / ___||  ___|| | | |/ _ \ / \ / \ / \     #
    #  | (_) |  \___ \| |__  | |_| | | | | | | | | | |    #
    #   \___/    |___/|____|  \___/ \___/ \_/ \_/ \_/     #
    #                                                    #
    #              >> AR-GHOSTNET v1.0 <<                #
    #          Enterprise-Grade Network Framework       #
    ####################################################
        """ + Colors.RESET)

    def run(self):
        while self.running:
            self.clear_screen()
            self.show_banner()
            
            print(f"{Colors.YELLOW}[1]{Colors.RESET} The Eye (Reconnaissance)")
            print(f"{Colors.YELLOW}[2]{Colors.RESET} The Blade (Exploitation)")
            print(f"{Colors.YELLOW}[3]{Colors.RESET} The Hammer (Stresser)")
            print(f"{Colors.YELLOW}[4]{Colors.RESET} Ghost Mode (Exit)")
            print("\n" + "-"*50)
            
            choice = input(f"{Colors.GREEN}ghost@net:~# {Colors.RESET}")

            if choice == '1':
                self.menu_recon()
            elif choice == '2':
                self.menu_exploitation()
            elif choice == '3':
                self.menu_stresser()
            elif choice == '4':
                Colors.log_info("Ghosting out... System shutdown.")
                self.running = False
            else:
                Colors.log_error("Invalid choice! Try again.")
                input("Press Enter to continue...")

    def menu_recon(self):
        self.clear_screen()
        print(f"{Colors.CYAN}--- THE EYE: Reconnaissance Menu ---{Colors.RESET}")
        print("[1] Port Scanner")
        print("[2] Banner Grabber")
        print("[B] Back to Main Menu")
        
        sub_choice = input(f"{Colors.GREEN}select-tool:~# {Colors.RESET}")
        if sub_choice == '1':
            target = input("Enter Target IP/URL: ")
            scanner = PortScanner()
            scanner.scan(target)
            input("\nPress Enter to return...")
        elif sub_choice == '2':
            target = input("Enter Target IP/URL: ")
            grabber = BannerGrabber()
            grabber.grab(target)
            input("\nPress Enter to return...")
        elif sub_choice.lower() == 'b':
            return
        else:
            Colors.log_error("Invalid choice!")
            input("Press Enter to continue...")

    def menu_exploitation(self):
        self.clear_screen()
        print(f"{Colors.CYAN}--- THE BLADE: Exploitation Menu ---{Colors.RESET}")
        print("[1] Directory Bruter (Dir Bruteforce)")
        print("[B] Back to Main Menu")
        
        sub_choice = input(f"{Colors.GREEN}select-tool:~# {Colors.RESET}")
        if sub_choice == '1':
            target = input("Enter Target URL (e.g., http://example.com): ")
            bruter = DirBruter()
            bruter.start_brute(target)
            input("\nPress Enter to return...")
        elif sub_choice.lower() == 'b':
            return
        else:
            Colors.log_error("Invalid choice!")
            input("Press Enter to continue...")

    def menu_stresser(self):
        self.clear_screen()
        print(f"{Colors.CYAN}--- THE HAMMER: Stresser Menu ---{Colors.RESET}")
        print("[1] HTTP Hammer (DoS/Stress Test)")
        print("[B] Back to Main Menu")
        
        sub_choice = input(f"{Colors.GREEN}select-tool:~# {Colors.RESET}")
        if sub_choice == '1':
            target = input("Enter Target URL: ")
            try:
                seconds = int(input("Enter duration in seconds (e.g., 30): "))
            except ValueError:
                Colors.log_error("Invalid number! Defaulting to 30 seconds.")
                seconds = 30
            hammer = HTTPHammer(threads=100)
            hammer.start_hammer(target, duration=seconds)
            input("\nPress Enter to return...")
        elif sub_choice.lower() == 'b':
            return
        else:
            Colors.log_error("Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    app = GhostNetMain()
    app.run()