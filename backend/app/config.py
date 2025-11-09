from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Loads all settings from the .env file."""
    DATABASE_URL: str
    ENCRYPTION_KEY: bytes  # Fernet key must be bytes
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env" # Tells pydantic to read from .env

# Create a single instance to be imported by other files
settings = Settings()