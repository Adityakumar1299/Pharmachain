from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.models import user as user_model
from app.models import doctor as doctor_model
from app.models import pharmacist as pharmacist_model
from app.models import patient as patient_model
from app.models import prescription as prescription_model
# Import our router from Step 7
from app.routers import auth
# Import our DB setup from Step 3
from app.db.base import Base
from app.db.session import engine


# --- ADD THIS BLOCK ---
# This explicitly imports all your models.
# This ensures that Base.metadata "knows" about all your tables
# *before* the `on_startup` event is called.

# -----------------------


app = FastAPI(title="Pharma Project API")

# --- Create Database Tables ---
# This will create all tables based on your models
# For production, you'd use Alembic migrations, but this is fine for dev

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all) # Uncomment to reset DB
        await conn.run_sync(Base.metadata.create_all)
# -----------------------------


# --- CORS Middleware ---
# This is CRITICAL for your React frontend (on localhost:3000)
# to talk to your backend (on localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Your React app's URL
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods
    allow_headers=["*"], # Allow all headers
)
# -------------------------


# --- Include API Routes ---
# All routes from app/routers/auth.py will now be
# available under the /auth prefix.
# e.g., /auth/signup/doctor
app.include_router(auth.router, prefix="/auth", tags=["Authentication"]) 

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pharma Project API"}