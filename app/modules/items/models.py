from sqlalchemy import Column, String, Integer, ForeignKey
from db.database import Base

class SchoolItems(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    school_id = Column(Integer, ForeignKey("schools.id"), nullable=False) 