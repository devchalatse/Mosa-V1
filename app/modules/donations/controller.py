from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import DonationCreate, DonationStatusUpdate
from .models import DonationStatus
from .service import DonationService

class DonationController:
    def __init__(self, db: Session):
        self.service = DonationService(db)

    def get_all_donations(self):
        donations = self.service.get_all_donations()  
        return {"status": "success", "data": donations}

    def get_donation_by_id(self, donation_id: int):
        try:
            donation = self.service.get_donation_by_id(donation_id)
            return {"status": "success", "data": donation} 
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def get_donation_by_user(self, user_id: int):
        try:
            users = self.service.get_donation_by_user(user_id)
            return {"status": "success", "data": users}  
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def get_donation_by_item(self, item_id: int):
        try:
            items = self.service.get_donation_by_item(item_id)
            return {"status": "success", "data": items}  
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def get_donation_by_status(self, status: DonationStatus):
        try:
            donations = self.service.get_donation_by_status(status)
            return {"status": "success", "data": donations}  
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def create_donation(self, data: DonationCreate):
        try:
            donation = self.service.create_donation(data)
            return {"status": "success", "data": donation}  
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_status(self, donation_id: int, status: DonationStatus):  
        try:
            donation = self.service.update_status(donation_id, status)
            return {"status": "success", "data": donation}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def delete_donation(self, donation_id: int):
        try:
            self.service.delete_donation(donation_id)
            return {"status": "success", "message": "Donation deleted"}  
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))