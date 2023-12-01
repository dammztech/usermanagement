# main.py

from fastapi import FastAPI
from api import user, auth
from db.base import Base, engine

# Create the FastAPI app
app = FastAPI()

# Include routers from the api module
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(auth.router, tags=["auth"])

# Create tables in the database
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
