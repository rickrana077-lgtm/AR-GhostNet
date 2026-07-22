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

    # --- UPGRADED FEATURES ---

    @staticmethod
    def spinner(message="Loading", duration=3):
        """Shows a spinning animation while loading."""
        import sys, time
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f'\r{Colors.CYAN}{frames[i % 10]} {message}...')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        print()

    @staticmethod
    def progress_bar(current, total, message="Progress"):
        """Shows a visual progress bar."""
        percent = int((current / total) * 100)
        bar = '█' * (percent // 2) + '░' * (50 - (percent // 2))
        print(f"\r{Colors.CYAN}{message}: [{bar}] {percent}%", end="")

    @staticmethod
    def boxed_header(text, color=Fore.CYAN):
        """Prints a header inside a stylish box."""
        border = "+" + "-" * (len(text) + 2) + "+"
        print(f"{color}{border}")
        print(f"{color}| {text} |")
        print(f"{color}{border}{Style.RESET_ALL}")

    @staticmethod
    def hacker_mode():
        """Activates the classic hacker terminal vibe."""
        print(f"{Colors.RED}HACKER MODE ACTIVATED!{Colors.RESET}")

# Example Usage (Testing)
if __name__ == "__main__":
    print("Testing AR-GhostNet Color System with Upgrades...")
    Colors.log_success("System online and ready.")
    Colors.log_error("Connection failed: Target unreachable.")
    Colors.log_info("Scanning for open ports...")
    Colors.log_warning("High latency detected.")
    Colors.spinner("Loading enhanced modules", duration=2)
    Colors.progress_bar(50, 100, "Scanning")
    Colors.boxed_header(" THE HACKER TERMINAL ")
    Colors.hacker_mode()