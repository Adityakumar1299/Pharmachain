from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings 

# Create an async engine
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Create a sessionmaker
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db() -> AsyncSession:
    """
    FastAPI Dependency to get a DB session.
    This will be called on every API request.
    """
    async with AsyncSessionLocal() as session:
        yield session