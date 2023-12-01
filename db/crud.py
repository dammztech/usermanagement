# app/db/crud.py

from sqlalchemy.orm import Session
from typing import List
from models.user import UserCreate, UserInDB
from db.models import User as DBUser

def create_user(db: Session, user: UserCreate) -> UserInDB:
    db_user = DBUser(**user.dict(), hashed_password="fakehash")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> UserInDB:
    return db.query(DBUser).filter(DBUser.email == email).first()

def get_all_users(db: Session) -> List[UserInDB]:
    return db.query(DBUser).all()
