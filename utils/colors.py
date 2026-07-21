# AR-GhostNet | Utility Layer: Visuals
# Location: utils/colors.py

from colorama import Fore, Back, Style, init

# Initialize colorama for Termux/Linux/Windows
init(autoreset=True)

class Colors:
    # Basic Colors
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    
    # UI Elements
    SUCCESS = Fore.GREEN + "[+]"
    ERROR = Fore.RED + "[!]"
    INFO = Fore.CYAN + "[*]"
    WARNING = Fore.YELLOW + "[?]"
    GHOST = Fore.MAGENTA + "👻 "

    @staticmethod
    def banner_text(text, color=Fore.CYAN):
        """Prints a formatted banner line"""
        print(f"{color}{'='*50}\n{text}\n{'='*50}{Style.RESET_ALL}")

    @staticmethod
    def log_success(message):
        print(f"{Colors.SUCCESS} {Fore.GREEN}{message}")

    @staticmethod
    def log_error(message):
        print(f"{Colors.ERROR} {Fore.RED}{message}")

    @staticmethod
    def log_info(message):
        print(f"{Colors.INFO} {Fore.CYAN}{message}")

    @staticmethod
    def log_warning(message):
        print(f"{Colors.WARNING} {Fore.YELLOW}{message}")

# Example Usage (Testing)
if __name__ == "__main__":
    print("Testing AR-GhostNet Color System...")
    Colors.log_success("System online and ready.")
    Colors.log_error("Connection failed: Target unreachable.")
    Colors.log_info("Scanning for open ports...")
    Colors.log_warning("High latency detected.")