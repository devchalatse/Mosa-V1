from pydantic import BaseModel, EmailStr, field_validator

class UserSignUp(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    role:str = "user"

    @field_validator("password")
    @classmethod
    def password_max_length(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must be 72 characters or less")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    email: EmailStr
    role: str
    class Config:
        from_attributes = True
    
