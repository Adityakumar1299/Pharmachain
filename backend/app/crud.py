from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import user as user_model

async def get_user_by_email(db: AsyncSession, email: str):
    """
    Fetches a user from the database by their email address.
    """
    result = await db.execute(
        select(user_model.User).filter(user_model.User.email == email)
    )
    return result.scalars().first()