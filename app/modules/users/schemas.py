from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    fullname: str     
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    email: EmailStr

    class Config:
        from_attributes = True