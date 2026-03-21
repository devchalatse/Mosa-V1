from pydantic import BaseModel
from .models import DonationStatus  

# What frontend sends when creating a donation
class DonationCreate(BaseModel):
    user_id: int
    school_id: int
    item_id: int
    quantity: int

# What we send back to frontend
class DonationResponse(BaseModel):
    id: int
    user_id: int
    school_id: int
    item_id: int
    quantity: int
    status: DonationStatus

    class Config:
        from_attributes = True

# For updating donation status
class DonationStatusUpdate(BaseModel):
    status: DonationStatus