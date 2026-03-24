from sqlalchemy import String, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from db.database import Base
import enum

class DonationStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Donation(Base):
    __tablename__ = "donations"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    school_id:Mapped[int] = mapped_column(Integer, ForeignKey("schools.id"), nullable=False)
    item_id:Mapped[int] = mapped_column(Integer, ForeignKey("items.id"), nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    status = mapped_column(Enum(DonationStatus), default=DonationStatus.PENDING)  
    created_at = mapped_column(DateTime, server_default=func.now())