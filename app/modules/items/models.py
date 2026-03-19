from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from db.database import Base
import enum

class CategoryEnum(str, enum.Enum):
    UNIFORM = "Uniform"
    STATIONERY = "Stationery"
    BOOKS = "Books"
    SHOES = "Shoes"
    FOOD = "Food"
    OTHER = "Other"

class SchoolItems(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    quantity = Column(Integer, nullable=False)
    school_id = Column(Integer, ForeignKey("schools.id"), nullable=False)