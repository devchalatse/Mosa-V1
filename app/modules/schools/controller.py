from fastapi import HTTPException
from .service import ServiceSchools
from .schemas import SchoolResponse, SchoolCreate
from sqlalchemy.orm import Session

class schoolController:
    def __init__(self, db:Session):
        self.service = ServiceSchools(db)

    def get_all_schools(self):
        schools = self.service.get_all_schools()
        return {"status":"success", "data":schools}
    
    def get_schools_id(self, school_id: int):
        try:
            school = self.service.get_school_by_id(school_id)
            return {"status":"success", "data": school}
        except ValueError as e:
            raise HTTPException(status_code=401,detail=str(e))
        
    def get_email_id(self, email:str):
        try:
            emails = self.service.get_school_by_email(email)
            return {"status":"success", "data":emails}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
    
    def create(self, data:SchoolCreate):
        try:
            create_data = self.service.create(data)
            return{"status":"success", "data": create_data}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    def delete(self, school_id:int):
        try:
            delete = self.service.delete(school_id)
            return {"status":"success", "data":self.delete}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
    def get_nearby_school(self, lat: float, lng: float, radius: float = 10):
        try:
            nearby = self.service.get_nearby_schools(lat, lng, radius)
            return{"status":"success", "data": nearby}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
    def verify_school(self, school_id:int):
        try:
            verify = self.service.verify_school(school_id)
            return {"status":"success", "data": verify}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
    
    
    
        

        
    