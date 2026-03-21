from sqlalchemy.orm import Session
from .models import Donation, DonationStatus  
from .schemas import DonationCreate           

class DonationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_donations(self):
        return self.db.query(Donation).all()

    def get_donation_by_id(self, donation_id: int):
        return self.db.query(Donation).filter(Donation.id == donation_id).first()

    def donation_by_user(self, user_id: int):
        return self.db.query(Donation).filter(Donation.user_id == user_id).all()

    def donation_by_item(self, item_id: int):
        return self.db.query(Donation).filter(Donation.item_id == item_id).all()

    def donation_by_school(self, school_id: int):
        return self.db.query(Donation).filter(Donation.school_id == school_id).all()

    def get_donation_by_status(self, status: DonationStatus):
        return self.db.query(Donation).filter(Donation.status == status).all()

    def create_donation(self, data: DonationCreate):
        donation = Donation(**data.model_dump())
        self.db.add(donation)
        self.db.commit()
        self.db.refresh(donation)
        return donation

    def update_status(self, donation_id: int, status: DonationStatus):
        donation = self.db.query(Donation).filter(Donation.id == donation_id).first()
        if not donation:
            return None
        donation.status = status # pyright: ignore[reportAttributeAccessIssue]
        self.db.commit()
        self.db.refresh(donation)
        return donation

    def delete_donation(self, donation_id: int):
        donation = self.db.query(Donation).filter(Donation.id == donation_id).first()
        if not donation:
            return None
        self.db.delete(donation)
        self.db.commit()
        return donation