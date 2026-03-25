from pydantic import BaseModel, EmailStr
from typing import Optional


class DriverCreate(BaseModel):
    fullname: str
    email: EmailStr
    phone_number: str
    password: str
    vehicle_make: Optional[str] = None
    vehicle_model: Optional[str] = None
    vehicle_plate: Optional[str] = None


class DriverLocationUpdate(BaseModel):
    lat: float
    lng: float


class DriverResponse(BaseModel):
    id: int
    fullname: str
    email: EmailStr
    phone_number: str
    vehicle_make: Optional[str]
    vehicle_model: Optional[str]
    vehicle_plate: Optional[str]
    current_lat: Optional[float]
    current_lng: Optional[float]
    status: str
    is_verified: bool

    class Config:
        from_attributes = True