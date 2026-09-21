from sqlalchemy import Integer, ForeignKey, Enum, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.database import Base
import enum


class NotificationStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Notification(Base):
    __tablename___ = "notification"

    id:Mapped[int]=mapped_column(Integer, primary_key=True, index=True)
    driver_id:Mapped[int]=mapped_column(Integer, ForeignKey("driver.id"), nullable=False)
    item_id:Mapped[int]=mapped_column(Integer, ForeignKey("item.id"), nullable=False)
    school_id:Mapped[int]=mapped_column(Integer, ForeignKey("school.id"), nullable=False)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("user.id"), nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    

    