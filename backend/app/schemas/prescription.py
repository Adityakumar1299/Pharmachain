from pydantic import BaseModel
from datetime import date
from .patient import PatientSimpleRead
from .doctor import DoctorSimpleRead
from .pharmacist import PharmacistSimpleRead

class PrescriptionBase(BaseModel):
    medication_name: str
    dosage: str
    instructions: str | None = None

class PrescriptionCreate(PrescriptionBase):
    patient_id: int 
class PrescriptionRead(PrescriptionBase):
    id: int
    date_issued: date
    is_filled: bool
    
    patient: "PatientSimpleRead"
    doctor: "DoctorSimpleRead"
    pharmacist: "PharmacistSimpleRead" | None = None 
    
    class Config:
        from_attributes = True

PrescriptionRead.model_rebuild()
