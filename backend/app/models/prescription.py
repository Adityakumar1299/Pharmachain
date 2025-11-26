from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Prescription(Base):
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    pharmacist_id = Column(Integer, ForeignKey("pharmacists.id"), nullable=True)
    medication_name = Column(String(255), nullable=False)
    dosage = Column(String(255), nullable=False)
    instructions = Column(Text)
    date_issued = Column(Date, nullable=False)
    is_filled = Column(Boolean, default=False)
    patient = relationship("Patient", back_populates="prescriptions")
    doctor = relationship("Doctor", back_populates="prescriptions")
    pharmacist = relationship("Pharmacist", back_populates="filled_prescriptions")