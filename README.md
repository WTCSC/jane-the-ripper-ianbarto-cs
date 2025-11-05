# Python Hash Cracker

A simple, interactive Python script for cracking hashes using a wordlist attack. This tool is intended for educational purposes to demonstrate how hash collisions are found.

## 📜 Description

This script prompts the user for a file containing a list of hashes, a wordlist file (dictionary), and the hashing algorithm to use. It then iterates through each word in the wordlist, hashes it using the specified algorithm, and compares the result to each hash in the hash file.

If a match is found, it prints the cracked hash and the corresponding plaintext word.

## ✨ Features

* Supports four common hashing algorithms: **MD5**, **SHA256**, **SHA512** and **SHA1**.
* Interactive command-line prompts for ease of use.
* Reports successfully cracked hashes and failures in real-time.
* Built entirely with standard Python libraries (no `pip install` required).

## 🚀 Getting Started

### Requirements

* Python 3.x

### Installation

No installation is needed. Simply save the code as a Python file (e.g., `main.py`).

1.  Download or copy the `main.py` script.
2.  Ensure you have a hash file and a wordlist file ready.

---

## 🔧 How to Use

Run the script from your terminal:

```bash
python3 main.py