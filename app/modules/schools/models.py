from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

class Schools(Base):
    __tablename__ = "schools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    items: Mapped[str] = mapped_column(String, nullable=True)