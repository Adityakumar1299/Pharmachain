from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Doctor(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # --- Encrypted Fields (with length) ---
    licenseNumber_encrypted = Column(String(512))
    aadharNumber_encrypted = Column(String(512))
    panNumber_encrypted = Column(String(512))
    # ------------------------

    # --- Other Fields (with length) ---
    speciality = Column(String(255))
    yearsOfExperience = Column(Integer)
    qualification = Column(String(255))
    hospitalName = Column(String(255))
    hospitalAddress = Column(String(512)) # Addresses can be long
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    # ----------------------------------
    
    user = relationship("User")
    prescriptions = relationship("Prescription", back_populates="doctor")

