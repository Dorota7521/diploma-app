from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key

def save_rsa_key_to_file(key, filename, password=None):
    with open(filename, 'wb') as key_file:
        if password:
            key_bytes = key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(password)
            )
        else:
            key_bytes = key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        key_file.write(key_bytes)

def load_rsa_key_from_file(filename, password=None):
    with open(filename, 'rb') as key_file:
        key_data = key_file.read()
        if password:
            private_key = serialization.load_pem_private_key(
                key_data,
                password=password,
                backend=default_backend()
            )
        else:
            private_key = serialization.load_pem_private_key(
                key_data,
                password=None,
                backend=default_backend()
            )
        return private_key

def encrypt_rsa(private_key, file_path):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    ciphertext = private_key.sign(
        plaintext,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)

    print(f'Encryption completed. Encrypted file saved to {encrypted_file_path}')

