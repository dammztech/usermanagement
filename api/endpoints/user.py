# app/api/endpoints/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from security.token import get_current_user
from db.base import get_db
from models.user import UserInDB
from db.crud import get_user_by_email, get_all_users

router = APIRouter()

@router.get("/users/me", response_model=UserInDB)
async def read_users_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=current_user.get("sub"))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=list[UserInDB])
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users
