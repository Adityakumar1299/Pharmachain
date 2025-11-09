from pydantic import BaseModel, EmailStr
from datetime import date
from .user import UserRead # Import the response model

# Schema for data coming IN from the React form
class DoctorCreate(BaseModel):
    role: str = "doctor"
    fullName: str
    email: EmailStr
    password: str
    phone: str
    dateOfBirth: date
    gender: str
    licenseNumber: str      # We receive plain text
    speciality: str
    yearsOfExperience: int
    qualification: str
    hospitalName: str
    hospitalAddress: str
    city: str
    state: str
    pincode: str
    aadharNumber: str       # We receive plain text
    panNumber: str          # We receive plain text

# Schema for data going OUT to the React app
class DoctorRead(BaseModel):
    user: UserRead  # Nested user info (id, email, name, etc.)
    speciality: str
    qualification: str
    hospitalName: str
    
    class Config:
        from_attributes = True