#RSA Encryption and Decryption in Python

This Python program demonstrates RSA encryption and decryption using the rsa library. The program generates an RSA key pair, encrypts a message with the public key, and then decrypts the message with the private key.
Prerequisites

Ensure you have the rsa library installed. If not, you can install it using:

bash

pip install rsa

How to Run

    Open a terminal and navigate to the directory containing the Python script.

    Run the script:

    bash

    python your_script_name.py

Program Explanation

The Python script consists of the following functions:

    generate_key_pair(): Generates an RSA key pair (public key and private key) with a key size of 512 bits.

    encrypt_message(message, public_key): Encrypts a given message using the provided public key.

    decrypt_message(encrypted_message, private_key): Decrypts an encrypted message using the provided private key.

The main part of the script:

    Generates an RSA key pair.

    Defines an original message to be encrypted.

    Encrypts the original message using the public key.

    Prints the original message, encrypted message, and decrypted message.

Example Output

bash

Original Message: RSA encryption and decryption!
Encrypted Message: b'\x92\xb7\xa7\x18\x95o\xcbw\xae\xc7\x9b\xbf'
Decrypted Message: RSA encryption and decryption!
