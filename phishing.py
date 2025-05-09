import re


email_content = """
Subject: Urgent! Account Deactivation Warning

Dear user,

Your account has been flagged for suspicious activity. Click below to verify:
http://paypal-security-check.com/verify

Thanks,
The PayPal Team
"""


phishing_keywords = ["urgent", "verify", "account", "suspend", "click", "deactivation"]
suspicious_link_patterns = ["security", "verify", "login", "paypal", "bank", "netflix"]

def detect_phishing(email):
    score = 0

    
    for word in phishing_keywords:
        if word in email.lower():
            score += 1

    
    links = re.findall(r'http[s]?://\S+', email)
    for link in links:
        for word in suspicious_link_patterns:
            if word in link.lower():
                score += 1
                print(f"[!] Suspicious link found: {link}")

    
    if score >= 3:
        print("⚠️ This email looks PHISHY!")
    else:
        print("✅ This email looks safe-ish (but stay alert).")

detect_phishing(email_content)
