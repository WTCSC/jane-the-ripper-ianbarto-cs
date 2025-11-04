from hashlib import md5
from hashlib import sha256
from hashlib import sha1
import hashlib


def main():
    hash_file_path = input("What is the path to your hash file? ")
    wordlist_path = input("What is the path to your list of words? ")
    algorithm = input("What hashing algorithm would you like to use? \n Choices: md5, sha256, sha1 \n Enter Here: ")
    if algorithm == "md5":
        md5(hash_file_path, wordlist_path)
    elif algorithm == "sha256":
        sha256(hash_file_path, wordlist_path)
    elif algorithm == "sha1":
        sha1(hash_file_path, wordlist_path)
    else:
        print("You did not")
    

def md5(hash_file_path, wordlist_path):
    with open(hash_file_path) as r:
        for hash_line in r:
            found = False
            hash_to_check = hash_line.strip()
            with open(wordlist_path)as f:
                for line in f:
                    hashed_words = hashlib.md5(line.strip().encode())
                    words_hex = hashed_words.hexdigest()
                    if words_hex == hash_line.strip():
                        print(f"[+] Cracked {words_hex} --> {line}")
                        found = True
            if not found:
                print(f"[-] Failed -- > {hash_to_check} \n")

def sha256(hash_file_path, wordlist_path):
    with open(hash_file_path) as r:
        for hash_line in r:
            found = False
            hash_to_check = hash_line.strip()
            with open(wordlist_path)as f:
                for line in f:
                    hashed_words = hashlib.sha256(line.strip().encode())
                    words_hex = hashed_words.hexdigest()
                    if words_hex == hash_line.strip():
                        print(f"[+] Cracked {words_hex} --> {line}")
                        found = True
            if not found:
                print(f"[-] Failed -- > {hash_to_check} \n")

def sha1(hash_file_path, wordlist_path):
    with open(hash_file_path) as r:
        for hash_line in r:
            found = False
            hash_to_check = hash_line.strip()
            with open(wordlist_path)as f:
                for line in f:
                    hashed_words = hashlib.sha1(line.strip().encode())
                    words_hex = hashed_words.hexdigest()
                    if words_hex == hash_line.strip():
                        print(f"[+] Cracked {words_hex} --> {line}")
                        found = True
            if not found:
                print(f"[-] Failed -- > {hash_to_check} \n")
            
                
    

if __name__ == "__main__":
    main()