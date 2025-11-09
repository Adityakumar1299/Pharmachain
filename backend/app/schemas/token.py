from pydantic import BaseModel

class Token(BaseModel):
    """
    Schema for the access token response.
    This is what we send back to the user after a successful login.
    """
    access_token: str
    token_type: str = "bearer" # Always 'bearer'

class TokenData(BaseModel):
    """
    Schema for the data we embed inside the JWT.
    This is what we get back when we decode the token.
    """
    email: str | None = None
    role: str | None = None
    id: int | None = None