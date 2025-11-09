# generate_key.py
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())   # copy the printed key into your .env
