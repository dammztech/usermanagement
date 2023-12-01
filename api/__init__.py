# app/api/__init__.py

from fastapi import APIRouter
from api.endpoints import user  # Import your user router
from api.endpoints import auth  # Import your user router

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])