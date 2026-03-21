from fastapi import FastAPI
from db.database import engine
from sqlalchemy import text
from modules.donations import models
from modules.users.router import router as users_router
from modules.schools.router import router as schools_router
from modules.schools.models import Base 
from modules.users.models import Base
from modules.items.models import Base
from modules.items.router import router as items_router

app = FastAPI()

@app.get("/")                   
def root():
    return {"message": "MOSA-V1 is UP "}


@app.on_event("startup")
def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("Database connected successfully")
    except Exception as e:
        print(f"Database connection failed: {e}")

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(schools_router)
app.include_router(items_router)

