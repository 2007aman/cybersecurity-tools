# Python File Encryptor 🔐

A secure file encryption and decryption tool built with Python and the `cryptography` library. This project demonstrates symmetric encryption, allowing users to protect sensitive text or binary files using the Fernet (AES-128) standard.

## 🚀 Features
- **Key Generation:** Automatically generates a unique 32-byte encryption key.
- **Symmetric Encryption:** Uses the same secure key for both encryption and decryption.
- **Binary Support:** Capable of encrypting not just text files, but any file format (images, PDFs, etc.).
- **Data Integrity:** Fernet ensures that the data cannot be manipulated or read without the original key.

## 🛠️ Requirements
- Python 3.x
- `cryptography` library

Install the dependency using pip:
```bash
pip install cryptography
