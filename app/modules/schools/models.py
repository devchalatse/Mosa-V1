from sqlalchemy import Column, String, Integer
from db.database import Base

class Schools(Base):
    __tablename__ = "schools"  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)               
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)  
    items = Column(String)
    location = Column(String, nullable=False)