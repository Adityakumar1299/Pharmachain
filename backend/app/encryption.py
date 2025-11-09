from cryptography.fernet import Fernet
from app.config import settings

# Initialize the cipher suite with your key from .env
# This key MUST be 32 bytes and stored as bytes
cipher_suite = Fernet(settings.ENCRYPTION_KEY)

def encrypt_data(data: str) -> str:
    """Encrypts a string and returns it as a string."""
    if not data:
        return data
    # Encrypt the data (must be bytes)
    encrypted_bytes = cipher_suite.encrypt(data.encode('utf-8'))
    # Decode back to a string to store in the database
    return encrypted_bytes.decode('utf-8')

def decrypt_data(encrypted_data: str) -> str:
    """Decrypts a string and returns it as a string."""
    if not encrypted_data:
        return encrypted_data
    # Encode the string back to bytes
    decrypted_bytes = cipher_suite.decrypt(encrypted_data.encode('utf-8'))
    # Decode the decrypted bytes back to a readable string
    return decrypted_bytes.decode('utf-8')