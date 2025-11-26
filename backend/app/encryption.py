from cryptography.fernet import Fernet
from app.config import settings

cipher_suite = Fernet(settings.ENCRYPTION_KEY)

def encrypt_data(data: str) -> str:
    if not data:
        return data
    encrypted_bytes = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_bytes.decode('utf-8')

def decrypt_data(encrypted_data: str) -> str:
    if not encrypted_data:
        return encrypted_data
    decrypted_bytes = cipher_suite.decrypt(encrypted_data.encode('utf-8'))
    return decrypted_bytes.decode('utf-8')