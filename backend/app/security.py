import bcrypt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer # <-- ADD THIS IMPORT
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from app.config import settings
from app.db.session import get_db
from app.models import user as user_model
from app.crud import get_user_by_email
from app.schemas import token as token_schema

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed one using bcrypt.
    """
    try:
        # We need to encode both for the library
        plain_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        
        # This is the bcrypt function to check a password
        return bcrypt.checkpw(plain_bytes, hashed_bytes)
    except Exception as e:
        # Log the error (in a real app) and fail safely
        print(f"Error verifying password: {e}")
        return False

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password using bcrypt.
    """
    # Encode the password, generate a salt, and hash it
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    
    # Decode back to a string to store in the DB
    return hashed_bytes.decode('utf-8')


# --- NEW: JWT (Token) Logic ---

# This tells FastAPI what the "token URL" is.
# Our login route will be at /auth/login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates a new JWT access token.
    """
    to_encode = data.copy()
    
    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Default to 15 minutes if no delta is provided
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    
    # Use secrets from our config.py
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt

async def get_current_user(
    db: AsyncSession = Depends(get_db), 
    token: str = Depends(oauth2_scheme)
) -> user_model.User:
    """
    This is a dependency that our protected routes will use.
    It decodes the token, validates it, and fetches the user from the DB.
    """
    
    # This is the error we'll raise if the token is invalid
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the token
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        
        # Get the email ("sub") from the token's payload
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
        
        # Validate the token data
        token_data = token_schema.TokenData(email=email)
    
    except JWTError:
        raise credentials_exception
    
    # Fetch the user from the database
    user = await get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    
    # Return the user model
    return user