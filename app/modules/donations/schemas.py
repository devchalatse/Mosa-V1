from pydantic import BaseModel
from .models import DonationStatus  

class DonationCreate(BaseModel):
    user_id: int
    school_id: int
    item_id: int
    quantity: int

class DonationResponse(BaseModel):
    id: int
    user_id: int
    school_id: int
    item_id: int
    quantity: int
    status: DonationStatus
    class Config:
        from_attributes = True

class DonationStatusUpdate(BaseModel):
    status: DonationStatus