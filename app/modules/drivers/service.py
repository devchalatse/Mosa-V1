from sqlalchemy.orm import Session
from .repository import DriverRepository
from .schemas import DriverCreate, DriverLocationUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class DriverService:
    def __init__(self, db: Session):
        self.repo = DriverRepository(db)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, driver_id: int):
        driver = self.repo.get_by_id(driver_id)
        if not driver:
            raise ValueError("Driver not found")
        return driver

    def create(self, data: DriverCreate):
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")

        data.password = pwd_context.hash(data.password)
        return self.repo.create(data)

    def update_location(self, driver_id: int, data: DriverLocationUpdate):
        driver = self.repo.get_by_id(driver_id)
        if not driver:
            raise ValueError("Driver not found")
        return self.repo.update_location(driver_id, data.lat, data.lng)

    def update_status(self, driver_id: int, status: str):
        driver = self.repo.get_by_id(driver_id)
        if not driver:
            raise ValueError("Driver not found")
        return self.repo.update_status(driver_id, status)

    def get_nearest_available(self, lat: float, lng: float):
        return self.repo.get_nearest_available(lat, lng)