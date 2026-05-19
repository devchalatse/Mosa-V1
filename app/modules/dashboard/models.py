from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from db.database import Base

class Dashboard(Base):
    ___tablename___= "dashboard"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    total_users:Mapped[int] = mapped_column(Integer)
    total_schools:Mapped[int] = mapped_column(Integer)
    total_items:Mapped[int] = mapped_column(Integer)
    total_donations:Mapped[int] = mapped_column(Integer)
    created_time:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

