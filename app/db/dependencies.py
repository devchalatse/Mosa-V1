from typing import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal 

def get_db() -> Generator[Session, None, None]:  #  Use Generator here!
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from .database import SessionLocal

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()