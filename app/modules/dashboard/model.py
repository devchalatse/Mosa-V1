from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from db.database import Base
import enum


class dashboard(Base):
    ___tablename__ = "Dashboard"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("user_id"), nullable=False)
    school_id:Mapped[int] = mapped_column(Integer, ForeignKey("school_id"),nullable=False)
        
