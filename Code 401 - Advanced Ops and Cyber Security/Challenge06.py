# Script Name:                  File Encryption Script Part 1 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      05/06/2024
# Purpose:                      Script that Encrypt a file (mode 1), Decrypt a file (mode 2), Encrypt a message (mode 3), Decrypt a message (mode 4)
# Source1:                      https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# Source2:                      https://g.co/gemini/share/93435dff7736

from cryptography.fernet import Fernet
import os

def load_key():
    # Load the previously saved key or generate a new one
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

def encrypt_file(filepath, key):
    # Encrypt the file
    f = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    # Decrypt the file
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    # Encrypt a message
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Decrypt a message
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    key = load_key()
    f = Fernet(key)
    
    print("Select a mode:")
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    print("3 - Encrypt a message")
    print("4 - Decrypt a message")
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
        message = input("Enter the message you want to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print("Encrypted Message:", encrypted_message.decode())
    elif mode == "4":
        message = input("Enter the encrypted message you want to decrypt: ")
        decrypted_message = decrypt_message(message.encode(), key)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()
