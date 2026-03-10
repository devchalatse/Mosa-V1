from pydantic import EmailStr, BaseModel

# For creating a school (request from frontend)
class SchoolCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str     
    location: str         
    items: str | None = None  

# For returning school data (response to frontend)
class SchoolResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str
    location: str

    class Config:
        from_attributes = True  