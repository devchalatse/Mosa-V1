from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
from db.database import Base
import enum

class DonationStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    school_id = Column(Integer, ForeignKey("schools.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(DonationStatus), default=DonationStatus.PENDING)  
    created_at = Column(DateTime, server_default=func.now())