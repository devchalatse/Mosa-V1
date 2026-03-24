from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
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
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str]= mapped_column(String, nullable=False)
    category:Mapped[int]= mapped_column(Enum(CategoryEnum), nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    school_id:Mapped[int] = mapped_column(Integer, ForeignKey("schools.id"), nullable=False)