from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import user as user_model
from app.models import doctor as doctor_model
from app.models import pharmacist as pharmacist_model
from app.models import patient as patient_model
from app.models import prescription as prescription_model
from app.routes import auth
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="PharmaTrack API")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"]) 

@app.get("/")
def read_root():
    return {"message": "PharmaTrack API"}