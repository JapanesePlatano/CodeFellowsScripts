# Script Name:                  File Encryption Script Part 2 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/06/2024
# Purpose:                      Script that Encrypt a file (mode 1), Decrypt a file (mode 2), Encrypt a message (mode 3), Decrypt a message (mode 4)
# Source1:                      https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-07/challenges/DEMO.md

from cryptography.fernet import Fernet
import os

def load_key():
    # Try to load an encryption key from a file. If the file doesn't exist, generate a new encryption key, save it, and return it.
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

def encrypt_file(filepath, key):
    # Encrypt the file located at filepath using the provided key, and overwrite the original file with the encrypted data.
    f = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    # Decrypt the file located at filepath using the provided key, and overwrite the encrypted file with the decrypted data.
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def encrypt_directory(directory, key):
    # Recursively encrypt all files in the specified directory and its subdirectories using the provided key.
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            encrypt_file(filepath, key)
    print(f"All files in {directory} have been encrypted.")

def decrypt_directory(directory, key):
    # Recursively decrypt all files in the specified directory and its subdirectories using the provided key.
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            decrypt_file(filepath, key)
    print(f"All files in {directory} have been decrypted.")

def main():
    # Main function to load the encryption key and provide the user with a menu to choose encryption or decryption tasks.
    key = load_key()
    
    print("Select a mode:")
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    print("3 - Encrypt a directory")
    print("4 - Decrypt a directory")
    mode = input("Enter mode (1/2/3/4): ")

    if mode == "1":
        filepath = input("Enter the path to the file you want to encrypt: ")
        encrypt_file(filepath, key)
        print("File encrypted successfully.")
    elif mode == "2":
        filepath = input("Enter the path to the file you want to decrypt: ")
        decrypt_file(filepath, key)
        print("File decrypted successfully.")
    elif mode == "3":
        directory = input("Enter the path to the directory you want to encrypt: ")
        encrypt_directory(directory, key)
    elif mode == "4":
        directory = input("Enter the path to the directory you want to decrypt: ")
        decrypt_directory(directory, key)
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()


