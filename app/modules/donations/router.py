from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.dependencies import get_db
from .controller import DonationController
from .schemas import DonationCreate, DonationStatusUpdate
from .models import DonationStatus

router = APIRouter(prefix="/donations", tags=["Donations"])

@router.get("/")
def get_all_donations(db: Session = Depends(get_db)):
    return DonationController(db).get_all_donations()

@router.get("/user/{user_id}")
def get_donation_by_user(user_id: int, db: Session = Depends(get_db)):
    return DonationController(db).get_donation_by_user(user_id)

@router.get("/item/{item_id}")
def get_donation_by_item(item_id: int, db: Session = Depends(get_db)):
    return DonationController(db).get_donation_by_item(item_id)

@router.get("/status/{status}")
def get_donation_by_status(status: DonationStatus, db: Session = Depends(get_db)):
    return DonationController(db).get_donation_by_status(status)

@router.get("/{donation_id}")
def get_donation_by_id(donation_id: int, db: Session = Depends(get_db)):
    return DonationController(db).get_donation_by_id(donation_id)

@router.post("/")
def create_donation(data: DonationCreate, db: Session = Depends(get_db)):
    return DonationController(db).create_donation(data)

@router.patch("/{donation_id}/status")
def update_status(donation_id: int, data: DonationStatusUpdate, db: Session = Depends(get_db)):
    return DonationController(db).update_status(donation_id, data.status)

@router.delete("/{donation_id}")
def delete_donation(donation_id: int, db: Session = Depends(get_db)):
    return DonationController(db).delete_donation(donation_id)