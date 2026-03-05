from fastapi import FastAPI
from db.database import engine
from sqlalchemy import text
from modules.users.router import router as users_router 
from modules.users.models import Base

app = FastAPI()

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