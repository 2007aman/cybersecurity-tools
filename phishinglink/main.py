import tldextract
from Levenshtein import ratio

# List of legitimate domains to compare against
legitimate_domains = ['example.com', 'google.com', 'facebook.com']

# List of URLs to test for potential phishing
test_urls = [
    'http://exampel.com',
    'https://google-login.com',
    'http://faceb00k.com/login',
    'https://g00gle.com',
    'https://google.com'
]

def extract_domain_parts(url):
    """Extracts subdomain, domain, and suffix from a URL."""
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def is_misspelled_domain(domain, legitimate_domains, threshold=0.9):
    """Checks if a domain is a misspelled version of a legitimate domain."""
    for leg_domain in legitimate_domains:
        # Get only the domain name part (e.g., 'google' from 'google.com')
        leg_domain_name = tldextract.extract(leg_domain).domain
        similarity_score = ratio(domain, leg_domain_name)
        
        # If very similar but not identical, it's likely a phishing attempt
        if similarity_score >= threshold:
            return True
    return False

def is_fishing_url(url, legitimate_domains):
    """Main logic to determine if a URL is a potential phishing link."""
    subdomain, domain, suffix = extract_domain_parts(url)
    full_domain = f"{domain}.{suffix}"

    # 1. If the exact domain is in the legitimate list, it's safe
    if full_domain in legitimate_domains:
        return False
    
    # 2. Check if the domain name itself is a misspelled version of a trusted one
    if is_misspelled_domain(domain, legitimate_domains):
        return True
    
    # 3. If it's not recognized and looks suspicious (optional extra logic)
    return True

def main():
    for url in test_urls:
        if is_fishing_url(url, legitimate_domains):
            print(f"[!] Potential phishing detected: {url}")
        else:
            print(f"[+] Legitimate URL: {url}")

if __name__ == "__main__":
    main()
