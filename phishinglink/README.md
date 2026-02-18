# Phishing Link Scanner 🎣

A Python-based security tool that detects "typosquatting" and phishing attempts. It uses fuzzy string matching (Levenshtein distance) to identify URLs that are suspiciously similar to legitimate domains.

## 🚀 Features
- **Domain Extraction:** Uses `tldextract` to accurately parse subdomains, domains, and suffixes.
- **Similarity Analysis:** Implements the Levenshtein algorithm to calculate how close a test URL is to a trusted domain.
- **Custom Thresholds:** Adjustable sensitivity (default 0.9) to catch subtle character swaps (e.g., `faceb00k` vs `facebook`).
- **Domain Validation:** Instantly recognizes legitimate domains to avoid false positives.

## 🛠️ Requirements
- Python 3.x
- `tldextract`
- `Levenshtein`

## 📖 How to Use
1. Activate your virtual environment and install dependencies.
2. Run the scanner:
   ```bash
   python phishing_scanner.py
