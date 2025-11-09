import enum
from sqlalchemy import Column, Integer, String, Date, Enum
from app.db.base import Base # Import from Step 3

class UserRole(str, enum.Enum):
    doctor = "doctor"
    pharmacist = "pharmacist"
    patient = "patient"

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    # --- ADDED LENGTHS ---
    fullName = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    phone = Column(String(50), unique=True, index=True)
    dateOfBirth = Column(Date)
    gender = Column(String(50))
    # ---------------------
    role = Column(Enum(UserRole), nullable=False)

