from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base


class Dashboard(Base):
    __tablename__ = "dashboard"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    school_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("schools.id"),
        nullable=False
    )

    items_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("items.id"),
        nullable=False
    )

    donation_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("donations.id"),
        nullable=False
    )