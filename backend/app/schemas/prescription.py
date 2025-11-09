from pydantic import BaseModel
from datetime import date

# --- REMOVE THE IMPORTS FROM HERE ---
# from .patient import PatientSimpleRead
# from .doctor import DoctorSimpleRead
# from .pharmacist import PharmacistSimpleRead
# ------------------------------------

# Base properties of a prescription
class PrescriptionBase(BaseModel):
    medication_name: str
    dosage: str
    instructions: str | None = None

# Schema for data coming IN (when a doctor creates one)
class PrescriptionCreate(PrescriptionBase):
    patient_id: int # Doctor specifies which patient this is for

# Schema for data going OUT (when API returns a prescription)
class PrescriptionRead(PrescriptionBase):
    id: int
    date_issued: date
    is_filled: bool
    
    # --- NESTED DATA (using string forward references) ---
    # We use strings ("...") to avoid the circular import
    patient: "PatientSimpleRead"
    doctor: "DoctorSimpleRead"
    pharmacist: "PharmacistSimpleRead" | None = None 
    # -----------------------------------------------------
    
    class Config:
        from_attributes = True

# --- ADD THIS BLOCK AT THE BOTTOM ---
# Now that PrescriptionRead is defined, we can import
# the other schemas and rebuild the model.
from .patient import PatientSimpleRead
from .doctor import DoctorSimpleRead
from .pharmacist import PharmacistSimpleRead

PrescriptionRead.model_rebuild()
# ----------------------------------