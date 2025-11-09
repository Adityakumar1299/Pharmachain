from pydantic import BaseModel, EmailStr
from datetime import date
from .user import UserRead

# Schema for data coming IN
class PharmacistCreate(BaseModel):
    role: str = "pharmacist"
    fullName: str
    email: EmailStr
    password: str
    phone: str
    dateOfBirth: date
    gender: str
    licenseNumber: str      # Plain text
    qualification: str
    yearsOfExperience: int
    pharmacyName: str
    addressLine1: str
    addressLine2: str | None = None
    city: str
    state: str
    pincode: str
    gstNumber: str          # Plain text
    aadharNumber: str       # Plain text

# Schema for data going OUT
class PharmacistRead(BaseModel):
    user: UserRead
    qualification: str
    pharmacyName: str
    
    class Config:
        from_attributes = True