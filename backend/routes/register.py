from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
import hashlib
import bcrypt
from dotenv import load_dotenv
from model import doctorModel, pharmaModel
from database import engine
from cryptography.fernet import Fernet, InvalidToken
router = APIRouter()
load_dotenv()
# secret_key="pharma_chain_key"
fernet = Fernet(SECRET_KEY.encode())


def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()  # store as string in DB

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against the stored bcrypt hash"""
    return bcrypt.checkpw(password.encode(), hashed.encode())

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def encrypt_data(data: str) -> str:
    """
    Encrypt plaintext and return a string (URL-safe base64).
    Store this string in the DB.
    """
    token = fernet.encrypt(data.encode('utf-8'))
    return token.decode('utf-8')

def verify_data(data: str, stored_hash: str) -> bool:
    return hash_data(data) == stored_hash


@router.post("/register")
def register_user(data: doctorModel):
    with Session(engine) as session:

        # condition to register doctor or pharma



        # check if user already registered
        statement = select(doctorModel).where(doctorModel.email == data.email)
        existing_user = session.exec(statement).first()

        if existing_user:
            raise HTTPException(status_code = 400, detail = "User already registered")
        
        doctor = doctorModel(
            fullname= data.fullname,
            email= data.email,
            password= hash_password(data.password),
            mobile_no= hash_data(data.mobile_no),
            aadhar_no= data.aadhar_no,
            pan_no= hash_data(data.pan_no),
            experience= data.experience,
            specialization= data.specialization,
            highest_degree= data.highest_degree
        )
        session.add(doctor)
        session.commit()
        session.refresh(doctor)

        return {"message":"Doctor registered sucessfully", "id": doctor.id}

