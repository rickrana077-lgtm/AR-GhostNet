# AR-GhostNet | Global Configuration
# Location: config/settings.py

class Settings:
    # --- Network Settings ---
    DEFAULT_TIMEOUT = 5              # Seconds to wait for response
    MAX_THREADS = 100               # Global thread limit for scanners/bruters
    USER_AGENT_ROTATION = True      # Enable/Disable UA rotation
    
    # --- Reconnaissance Settings ---
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]
    
    # --- Exploitation Settings ---
    DIR_WORDLIST_DEFAULT = "common.txt" # Default wordlist if none provided
    
    # --- Branding ---
    VERSION = "1.0.0"
    AUTHOR = "GhostNet-Team"
    
    # --- API Keys (Placeholders for future modules) ---
    SHODAN_API_KEY = "" 
    VIRUSTOTAL_API_KEY = ""