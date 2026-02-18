# MD5 Password Cracker 🛡️

A professional Python-based security tool designed to perform dictionary attacks against MD5 hashes. This tool features a built-in hash generator for testing and a robust file-handling system for large wordlists.

## 🚀 Features
- **Dual Mode:** Crack an existing MD5 hash or simulate a target by providing a plain password.
- **Error Handling:** Gracefully handles missing files and encoding issues.
- **Progress Tracking:** Real-time feedback on the number of passwords searched.
- **Case Sensitivity:** Normalizes hashes to ensure accurate comparison.

## 🛠️ Requirements
- Python 3.x
- No external libraries required (uses built-in `hashlib`).

## 📖 How to Use
1. Clone this repository or copy the `cracker.py` file.
2. Prepare a wordlist (e.g., `wordlist.txt`) with one password per line.
3. Run the script:
   ```bash
   python cracker.py
