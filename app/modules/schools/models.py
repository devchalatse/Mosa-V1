from sqlalchemy import Integer, String, Boolean, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base
from datetime import datetime

class Schools(Base):
    __tablename__ = "schools"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    address: Mapped[str] = mapped_column(String, nullable=False)
    latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True)

    emis_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # Fields from the PDF
    school_phase: Mapped[str | None] = mapped_column(String, nullable=True)        
    education_district: Mapped[str | None] = mapped_column(String, nullable=True)  
    quintile: Mapped[int | None] = mapped_column(Integer, nullable=True)           
    learner_numbers: Mapped[int | None] = mapped_column(Integer, nullable=True)    

    verified: Mapped[bool] = mapped_column(Boolean, default=False)
    verification_status: Mapped[str] = mapped_column(String, default="pending")

    source: Mapped[str] = mapped_column(String, default="manual")

    verified_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)