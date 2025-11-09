from pydantic import BaseModel, EmailStr
from datetime import date
from app.models.user import UserRole # Import the enum from models

# Base properties shared by all
class UserBase(BaseModel):
    email: EmailStr
    fullName: str
    phone: str
    dateOfBirth: date
    gender: str

# Schema for creating a user (password is required)
class UserCreate(UserBase):
    password: str
    role: UserRole

# Schema for reading/returning a user (password is excluded)
class UserRead(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True # Allows Pydantic to read from ORM models


class UserSimpleRead(BaseModel):
    id: int
    fullName: str
    role: UserRole

    class Config:
        from_attributes = True