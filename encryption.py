from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

# Replace with your key management implementation
KEY = os.urandom(32)  # Example key, replace with secure key management

def encrypt_file(input_file, output_file):
    cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_file, output_file):
    cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
