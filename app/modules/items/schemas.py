from pydantic import BaseModel

class SchoolItems(BaseModel):
    name:str
    quantity:int
    category:str
    school_id:int

class ItemsResponse(BaseModel):
    id:int
    name:str
    quantity:int
    category:str
    school_id:int

    class Config:
        from_attributes=True
