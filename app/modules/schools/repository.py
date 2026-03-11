from sqlalchemy.orm import Session
from .models import Schools
from .schemas import SchoolCreate

class SchoolRepository:
    def __init__(self, db: Session):  
        self.db = db

    def get_schools(self):
        return self.db.query(Schools).all()  

    def get_school_by_id(self, school_id: int):
        return self.db.query(Schools).filter(Schools.id == school_id).first()

    def get_school_by_email(self, email: str):
        return self.db.query(Schools).filter(Schools.email == email).first()  

    def create(self, data: SchoolCreate):
        school = Schools(**data.model_dump())
        self.db.add(school)        
        self.db.commit()
        self.db.refresh(school)   
        return school
    
    def delete(self, school_id:int):
        school = self.db.query(Schools).filter(Schools.id == school_id).first()
        if not school:
            return None
            self.db.delete(school)
            self.db.commit()
            return school
        
        