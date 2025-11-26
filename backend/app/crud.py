from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import user as user_model

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(
        select(user_model.User).filter(user_model.User.email == email)
    )
    return result.scalars().first()