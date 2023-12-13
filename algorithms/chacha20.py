from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def encrypt_chacha20(key, file_path):
    backend = default_backend()

    # Generate a random nonce (Number used Once)
    nonce = os.urandom(16)

    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=backend)
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Save the encrypted data to a new file
    encrypted_file_path = file_path + '.enc_chacha20'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(nonce + ciphertext)

    print(f'Encryption completed. Encrypted file saved to {encrypted_file_path}')
