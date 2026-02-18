import hashlib

def get_md5_hash(text):
    """Helper function to create an MD5 hash from plain text."""
    return hashlib.md5(text.strip().encode()).hexdigest()

def crack_password():
    print("--- Python Password Cracker (MD5) ---")
    
    # New Logic: Allow user to input a plain password OR a hash
    print("\n[1] I have an MD5 hash to crack")
    print("[2] I want to test a plain password (generate hash automatically)")
    mode = input("\nSelect mode (1 or 2): ").strip()

    if mode == "2":
        plain_text = input("[*] Enter the password to simulate: ")
        target_hash = get_md5_hash(plain_text)
        print(f"[!] Simulated target hash: {target_hash}")
    else:
        target_hash = input("[*] Enter MD5 Hash to Crack: ").strip().lower()

    wordlist_path = input("[*] Enter Path to Wordlist (e.g., wordlist.txt): ").strip()

    print(f"\n[*] Starting Dictionary Attack...")
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            count = 0
            for line in file:
                word = line.strip()
                # Hash the current word from the file
                hashed_word = get_md5_hash(word)
                count += 1
                
                # Check for match
                if hashed_word == target_hash:
                    print(f"\n[+] SUCCESS! Password Found: {word}")
                    print(f"[+] Attempts: {count}")
                    return
                
                # Visual feedback every 1000 attempts
                if count % 1000 == 0:
                    print(f"[*] Searched {count} passwords...", end='\r')

            print(f"\n[-] Finished. Searched {count} words. No match found.")

    except FileNotFoundError:
        print(f"\n[!] Error: The file '{wordlist_path}' was not found.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    crack_password()
