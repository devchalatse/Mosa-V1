from sqlalchemy.orm import Session
from fastapi import HTTPException
from .service import DriverService
from .schemas import DriverCreate, DriverLocationUpdate


class DriverController:
    def __init__(self, db: Session):
        self.service = DriverService(db)

    def get_all(self):
        return {"status": "success", "data": self.service.get_all()}

    def get_one(self, driver_id: int):
        try:
            return {"status": "success", "data": self.service.get_by_id(driver_id)}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def create(self, data: DriverCreate):
        try:
            return {"status": "success", "data": self.service.create(data)}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_location(self, driver_id: int, data: DriverLocationUpdate):
        try:
            return {"status": "success", "data": self.service.update_location(driver_id, data)}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def update_status(self, driver_id: int, status: str):
        try:
            return {"status": "success", "data": self.service.update_status(driver_id, status)}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def get_nearest(self, lat: float, lng: float):
        try:
            return {"status": "success", "data": self.service.get_nearest_available(lat, lng)}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))