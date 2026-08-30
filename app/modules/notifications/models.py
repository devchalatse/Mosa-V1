from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, Boolean
from datetime import datetime, timezone
from app.db.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True, 
        index=True
    )

    recipient_id:Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    message:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    title:Mapped[String] = mapped_column(
        String,
        nullable=False
    )

    is_read:Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    date_created:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )