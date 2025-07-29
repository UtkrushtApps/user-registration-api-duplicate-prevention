from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate, UserOut
from app.services.user_service import create_user
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_user = await create_user(db, user)
        return new_user
    except IntegrityError:
        raise HTTPException(status_code=400, detail="A user with this email already exists.")
