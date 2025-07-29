from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.models.user import UserCreate
from app.db.tables import User

async def create_user(db: AsyncSession, user_data: UserCreate):
    stmt = insert(User).values(email=user_data.email, name=user_data.name).returning(User)
    result = await db.execute(stmt)
    await db.commit()
    return result.fetchone()
