from sqlalchemy.orm import Session
from .schemas import DonationStatus, DonationCreate
from .repository import DonationRepository
class DonationService:
    def __init__(self, db:Session):
        self.repo = DonationRepository(db)

    def get_all_donations(self):
        return self.repo.get_all_donations()
    
    def get_donation_by_id(self, donation_id:int):
        donation = self.repo.get_donation_by_id(donation_id)
        if not donation:
            raise ValueError("User not found")
        return donation
    
    def get_donation_by_user(self, user_id:int):
        users = self.repo.get_donation_by_id(user_id)
        if not users:
            raise ValueError("No donations found on this User")
        return users
    
    def get_donation_by_item(self, item_id:int):
        items = self.repo.donation_by_item(item_id)
        if not items:
            raise ValueError("No donation found on this Item")
        return items
    
    def get_donation_by_status(self, status:DonationStatus):
        status_data = self.repo.get_donation_by_status(status)
        if not status_data:
            raise ValueError("No donation found on this Status")
        return status_data
    
    def create_donation(self, data:DonationCreate):
        return self.repo.create_donation(data)

    def update_status(self, donation_id: int, status: DonationStatus):
        return self.repo.update_status(donation_id, status)
    
    def delete_donation(self, donation_id:int):
        donation = self.repo.delete_donation(donation_id)
        if not donation:
            raise ValueError("Donation not found")
        return donation

        