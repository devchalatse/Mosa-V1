from pydantic import EmailStr, BaseModel
from typing import Optional


class SchoolCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    emis_number: Optional[str] = None

    # PDF fields
    school_phase: Optional[str] = None
    education_district: Optional[str] = None
    quintile: Optional[int] = None
    learner_numbers: Optional[int] = None


class SchoolResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str
    address: str

    latitude: Optional[float]
    longitude: Optional[float]

    emis_number: Optional[str]

    # PDF fields/ Form inputs
    school_phase: Optional[str]
    education_district: Optional[str]
    quintile: Optional[int]
    learner_numbers: Optional[int]

    # Verification fields
    verified: bool
    verification_status: str
    source: str

    class Config:
        from_attributes = True


class NearbySchoolResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    distance: float

    class Config:
        from_attributes = True