from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.config import settings
from app.db.session import get_db
from app.security import get_password_hash
from app.encryption import encrypt_data
from app.security import verify_password
from app.security import create_access_token
from app.models import user as user_model
from app.models import doctor as doctor_model
from app.models import pharmacist as pharmacist_model
from app.models import patient as patient_model
from app.models import prescription as prescription_model
from app.schemas import doctor as doctor_schema
from app.schemas import pharmacist as pharmacist_schema
from app.schemas import patient as patient_schema
from app.schemas import user as user_schema
from app.schemas import token as token_schema 

router = APIRouter()

async def get_user_by_email(db: AsyncSession, email: str):
    """Check if a user with this email already exists."""
    result = await db.execute(select(user_model.User).filter(user_model.User.email == email))
    return result.scalars().first()

@router.post("/login", response_model=token_schema.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    
    user = await get_user_by_email(db, email=form_data.username)
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={
            "sub": user.email,
            "id": user.id,
            "role": user.role.value
        }, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup/doctor", response_model=doctor_schema.DoctorRead, status_code=status.HTTP_201_CREATED)
async def signup_doctor(
    doctor_in: doctor_schema.DoctorCreate,
    db: AsyncSession = Depends(get_db)
):

    #Check if user exists
    user = await get_user_by_email(db, email=doctor_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    
    hashed_password = get_password_hash(doctor_in.password)
    
    db_user = user_model.User(
        fullName=doctor_in.fullName,
        email=doctor_in.email,
        hashed_password=hashed_password,
        phone=doctor_in.phone,
        dateOfBirth=doctor_in.dateOfBirth,
        gender=doctor_in.gender,
        role=user_model.UserRole.doctor
    )
    db.add(db_user)
    await db.flush() 

    db_doctor = doctor_model.Doctor(
        user_id=db_user.id,
        speciality=doctor_in.speciality,
        yearsOfExperience=doctor_in.yearsOfExperience,
        qualification=doctor_in.qualification,
        hospitalName=doctor_in.hospitalName,
        hospitalAddress=doctor_in.hospitalAddress,
        city=doctor_in.city,
        state=doctor_in.state,
        pincode=doctor_in.pincode,
        
        licenseNumber_encrypted=encrypt_data(doctor_in.licenseNumber),
        aadharNumber_encrypted=encrypt_data(doctor_in.aadharNumber),
        panNumber_encrypted=encrypt_data(doctor_in.panNumber)
    )
    db.add(db_doctor)
    
    await db.commit()
    await db.refresh(db_doctor)
    await db.refresh(db_user) 

    return doctor_schema.DoctorRead(
        user=user_schema.UserRead.from_orm(db_user), 
        speciality=db_doctor.speciality,
        qualification=db_doctor.qualification,
        hospitalName=db_doctor.hospitalName,
    )


@router.post("/signup/pharmacist", response_model=pharmacist_schema.PharmacistRead, status_code=status.HTTP_201_CREATED)
async def signup_pharmacist(
    pharmacist_in: pharmacist_schema.PharmacistCreate,
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_email(db, email=pharmacist_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )

    hashed_password = get_password_hash(pharmacist_in.password)
    
    db_user = user_model.User(
        fullName=pharmacist_in.fullName,
        email=pharmacist_in.email,
        hashed_password=hashed_password,
        phone=pharmacist_in.phone,
        dateOfBirth=pharmacist_in.dateOfBirth,
        gender=pharmacist_in.gender,
        role=user_model.UserRole.pharmacist
    )
    db.add(db_user)
    await db.flush()
    
    db_pharmacist = pharmacist_model.Pharmacist(
        user_id=db_user.id,
        qualification=pharmacist_in.qualification,
        yearsOfExperience=pharmacist_in.yearsOfExperience,
        pharmacyName=pharmacist_in.pharmacyName,
        addressLine1=pharmacist_in.addressLine1,
        addressLine2=pharmacist_in.addressLine2,
        city=pharmacist_in.city,
        state=pharmacist_in.state,
        pincode=pharmacist_in.pincode,
        licenseNumber_encrypted=encrypt_data(pharmacist_in.licenseNumber),
        gstNumber_encrypted=encrypt_data(pharmacist_in.gstNumber),
        aadharNumber_encrypted=encrypt_data(pharmacist_in.aadharNumber)
    )
    db.add(db_pharmacist)
    
    await db.commit()
    await db.refresh(db_pharmacist)
    await db.refresh(db_user)
    
    return pharmacist_schema.PharmacistRead(
        user=user_schema.UserRead.from_orm(db_user),
        qualification=db_pharmacist.qualification,
        pharmacyName=db_pharmacist.pharmacyName,
    )


@router.post("/signup/patient", response_model=patient_schema.PatientRead, status_code=status.HTTP_201_CREATED)
async def signup_patient(
    patient_in: patient_schema.PatientCreate,
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_email(db, email=patient_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )

    hashed_password = get_password_hash(patient_in.password)
    
    db_user = user_model.User(
        fullName=patient_in.fullName,
        email=patient_in.email,
        hashed_password=hashed_password,
        phone=patient_in.phone,
        dateOfBirth=patient_in.dateOfBirth,
        gender=patient_in.gender,
        role=user_model.UserRole.patient
    )
    db.add(db_user)
    await db.flush()
    
    db_patient = patient_model.Patient(
        user_id=db_user.id,
        emergencyContactName=patient_in.emergencyContactName,
        emergencyContactPhone=patient_in.emergencyContactPhone,
        address=patient_in.address,
        city=patient_in.city,
        state=patient_in.state,
        pincode=patient_in.pincode,
        allergies=patient_in.allergies,
        aadharNumber_encrypted=encrypt_data(patient_in.aadharNumber)
    )
    db.add(db_patient)
    
    await db.commit()
    await db.refresh(db_patient)
    await db.refresh(db_user)
    
    return patient_schema.PatientRead(
        user=user_schema.UserRead.from_orm(db_user),
        address=db_patient.address,
        city=db_patient.city,
        state=db_patient.state,
        allergies=db_patient.allergies,
    )