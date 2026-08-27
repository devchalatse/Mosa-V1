from fastapi import FastAPI
from sqlalchemy import text
from app.db.database import engine, Base
from app.modules.users import models
from app.modules.schools import models
from app.modules.items import models
from app.modules.donations import models
from app.modules.drivers import models
from app.modules.dashboard import models
from app.core.logging import setup_logging
import logging
setup_logging()
logger = logging.getLogger(__name__)
# logger.info("Mosa Application Start-UP")

# Routers
from app.modules.users.router import router as users_router
from app.modules.schools.router import router as schools_router
from app.modules.items.router import router as items_router
from app.modules.donations.router import router as donation_router
from app.modules.drivers.router import router as drivers_router
from app.modules.dashboard.router import router as dashboard_router

app = FastAPI()

@app.on_event("startup")
def check_start_up():
    logger.info("Mosa Application started")

@app.on_event("shutdown")
def check_shutdown():
    logger.info("Mosa Application shutted down")

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