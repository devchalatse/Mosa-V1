from fastapi import FastAPI
from db.base import Base
from db.session import engine
from modules.users.router import router
# from modules.user.router import router
# from modules.users.router import router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(router)

