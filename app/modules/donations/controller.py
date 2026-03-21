from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import DonationCreate, DonationResponse, DonationStatus
from .service import DonationService

class DonationController:
    def __init__(self, db:Session):
        self.service = DonationService(db)

    