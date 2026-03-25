from sqlalchemy.orm import Session
from sqlalchemy import text
from .models import Driver


class DriverRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Driver).all()

    def get_by_id(self, driver_id: int):
        return self.db.query(Driver).filter(Driver.id == driver_id).first()

    def get_by_email(self, email: str):
        return self.db.query(Driver).filter(Driver.email == email).first()

    def create(self, data):
        driver = Driver(**data.model_dump())
        self.db.add(driver)
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def update_location(self, driver_id: int, lat: float, lng: float):
        driver = self.get_by_id(driver_id)
        driver.current_lat = lat # type: ignore
        driver.current_lng = lng # pyright: ignore[reportOptionalMemberAccess]
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def update_status(self, driver_id: int, status: str):
        driver = self.get_by_id(driver_id)
        driver.status = status # type: ignore
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def get_nearest_available(self, lat: float, lng: float):
        query = text("""
            SELECT *,
            (
                6371 * acos(
                    cos(radians(:lat)) *
                    cos(radians(current_lat)) *
                    cos(radians(current_lng) - radians(:lng)) +
                    sin(radians(:lat)) *
                    sin(radians(current_lat))
                )
            ) AS distance
            FROM drivers
            WHERE status = 'available'
            AND current_lat IS NOT NULL
            AND current_lng IS NOT NULL
            ORDER BY distance
            LIMIT 1
        """)
        return self.db.execute(query, {"lat": lat, "lng": lng}).fetchone()