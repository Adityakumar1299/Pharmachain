from pydantic import BaseModel, EmailStr
from datetime import date
from app.models.user import UserRole


class UserBase(BaseModel):
    email: EmailStr
    fullName: str
    phone: str
    dateOfBirth: date
    gender: str

class UserCreate(UserBase):
    password: str
    role: UserRole

class UserRead(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True


class UserSimpleRead(BaseModel):
    id: int
    fullName: str
    role: UserRole

    class Config:
        from_attributes = True