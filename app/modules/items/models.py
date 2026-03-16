from sqlalchemy import Column, String, Integer, ForeignKey
from db.database import Base

class SchoolItems(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    school_id = Column(Integer, ForeignKey=("school_id"), unique=True)
    
