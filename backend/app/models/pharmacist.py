from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Pharmacist(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # --- Encrypted Fields (with length) ---
    licenseNumber_encrypted = Column(String(512))
    gstNumber_encrypted = Column(String(512))
    aadharNumber_encrypted = Column(String(512))
    # ------------------------
    
    # --- Other Fields (with length) ---
    qualification = Column(String(255))
    yearsOfExperience = Column(Integer)
    pharmacyName = Column(String(255))
    addressLine1 = Column(String(512))
    addressLine2 = Column(String(512), nullable=True) 
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    # ----------------------------------
    
    user = relationship("User")
    filled_prescriptions = relationship("Prescription", back_populates="pharmacist")

