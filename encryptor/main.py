
 

from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it to a file."""
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the current directory named 'encryption_key.key'."""
    return open("encryption_key.key", "rb").read()

def encrypt_file(input_file, output_file, key):
    """Encrypts a file using the Fernet key."""
    f = Fernet(key)
    
    with open(input_file, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    """Decrypts a file using the Fernet key."""
    f = Fernet(key)
    
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # 1. Generate and save a key (only needs to be done once)
    generate_key()
    key = load_key()

    # 2. Files to process
    # Note: Create 'plain_text.txt' manually with some text before running
    input_filename = "plain_text.txt"
    encrypted_filename = "encrypted_file.txt"
    decrypted_filename = "decrypted_file.txt"

    # 3. Encrypt
    encrypt_file(input_filename, encrypted_filename, key)
    print(f"[*] {input_filename} encrypted to {encrypted_filename} [00:06:23]")

    # 4. Decrypt
    decrypt_file(encrypted_filename, decrypted_filename, key)
    print(f"[*] {encrypted_filename} decrypted to {decrypted_filename} [00:06:23]")
