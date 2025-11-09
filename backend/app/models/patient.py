from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Patient(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # --- Encrypted Fields (with length) ---
    aadharNumber_encrypted = Column(String(512))
    # ------------------------
    
    # --- Other Fields (with length) ---
    emergencyContactName = Column(String(255))
    emergencyContactPhone = Column(String(50))
    address = Column(String(512))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    # ----------------------------------

    allergies = Column(Text, nullable=True) # Text is fine, no length needed
    
    user = relationship("User")
    prescriptions = relationship("Prescription", back_populates="patient")

