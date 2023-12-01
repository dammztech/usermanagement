# app/models/user.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str

class UserInDB(User):
    hashed_password: str
