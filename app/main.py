from fastapi import FastAPI
from sqlalchemy import text

from db.database import engine, Base

# Import models so SQLAlchemy registers them
from modules.users import models
from modules.schools import models
from modules.items import models
from modules.donations import models
from modules.drivers import models
from modules.dashboard import models

# Routers
from modules.users.router import router as users_router
from modules.schools.router import router as schools_router
from modules.items.router import router as items_router
from modules.donations.router import router as donation_router
from modules.drivers.router import router as drivers_router
from modules.dashboard.router import router as dashboard_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MOSA-V1 is UP"}

@app.on_event("startup")
def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("Database connected successfully")
    except Exception as e:
        print(f"Database connection failed: {e}")

# create tables
Base.metadata.create_all(bind=engine)

# routers
app.include_router(users_router)
app.include_router(schools_router)
app.include_router(items_router)
app.include_router(donation_router)
app.include_router(drivers_router)
app.include_router(dashboard_router)