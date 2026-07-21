import os
import sys
import time
from colorama import Fore, Style, init

# Initialize Colorama for professional terminal colors
init(autoreset=True)

# --- BRANDING & STYLING ---
BRAND = Fore.RED + Style.BRIGHT + "AR Made in INDIA"
TOOL_NAME = Fore.GREEN + Style.BRIGHT + "AR-GhostNet"
SLOGAN = Fore.CYAN + "The Ghost is in the Network..."

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print(Fore.RED + Style.BRIGHT + r"""
    ########################################################################
    #                                                                      #
    #    ██████  █████  ██████  ██████   ███    ███  █████  ███    ███       #
    #    ██  ██  ██    ██   ██ ██   ██  ████  ████  ██   ██ ██    ██        #
    #    ██  ██  ██    ██   ██ ██   ██  ██ ████ ██  ██   ██ ██    ██        #
    #    ██  ██  ██    ██   ██ ██   ██  ██  ██  ██  ██   ██ ██    ██        #
    #    ██████  █████  ██████ ██████   ██   ██ ██  █████  ████████         #
    #                                                                      #
    ########################################################################
    """)
    print(f"{Fore.YELLOW}  >> {BRAND} presents: {TOOL_NAME} <<")
    print(f"{Fore.WHITE}  >> {SLOGAN}")
    print(Fore.RED + "  ------------------------------------------------------------------")

def main_menu():
    while True:
        banner()
        print(f"\n{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] {Fore.YELLOW}Reconnaissance Layer (The Eye)")
        print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] {Fore.YELLOW}Exploitation Layer (The Blade)")
        print(f"{Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}] {Fore.YELLOW}Stresser Layer (The Hammer)")
        print(f"{Fore.WHITE}[{Fore.GREEN}4{Fore.WHITE}] {Fore.YELLOW}Ghost Mode (The Cloak)")
        print(f"{Fore.WHITE}[{Fore.GREEN}0{Fore.WHITE}] {Fore.RED}Exit the Arsenal")
        
        print(f"\n{Fore.CYAN}💀 {BRAND} | Select an Option: ", end="")
        choice = input()

        if choice == '1':
            print(f"\n{Fore.GREEN}[!] Loading Recon Modules...{Style.RESET_ALL}")
            time.sleep(1)
            try:
                from core.scanner import run_scanner
                run_scanner()
            except ImportError:
                print(f"{Fore.RED}[!] Error: Recon modules not found in /core/ directory.")
            input("\nPress Enter to return to menu...")
        
        elif choice == '2':
            print(f"\n{Fore.GREEN}[!] Initializing Exploitation Engine...{Style.RESET_ALL}")
            time.sleep(1)
            try:
                from modules.exploit import run_exploit
                run_exploit()
            except ImportError:
                print(f"{Fore.RED}[!] Error: Exploit modules not found in /modules/ directory.")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            print(f"\n{Fore.GREEN}[!] Preparing Stress Test...{Style.RESET_ALL}")
            time.sleep(1)
            try:
                from modules.stresser import run_stresser
                run_stresser()
            except ImportError:
                print(f"{Fore.RED}[!] Error: Stresser modules not found in /modules/ directory.")
            input("\nPress Enter to return to menu...")

        elif choice == '4':
            print(f"\n{Fore.GREEN}[!] Activating Ghost Mode...{Style.RESET_ALL}")
            time.sleep(1)
            try:
                from core.ghost import run_ghost
                run_ghost()
            except ImportError:
                print(f"{Fore.RED}[!] Error: Ghost modules not found in /core/ directory.")
            input("\nPress Enter to return to menu...")

        elif choice == '0':
            print(f"\n{Fore.RED}[!] Shutting down the Arsenal...{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Stay Invisible. Stay Deadly.")
            time.sleep(2)
            sys.exit()

        else:
            print(f"\n{Fore.RED}[!] Invalid selection. Try again, pal.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Forced Shutdown Detected. Exiting...")
        sys.exit()