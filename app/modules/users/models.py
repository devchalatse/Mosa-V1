from sqlalchemy import Column, String, Integer
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String, unique=True, nullable=False)
    fullname=Column(String)
    # hashed_password=Column(String)
    password = Column(String, nullable=False) 
    role=Column(String, default= "donor")

