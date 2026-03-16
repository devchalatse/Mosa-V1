from sqlalchemy.orm import Session
from .models import Schools
from .schemas import SchoolCreate

class RepositorySchools:
    def __init__(self, db:Session):
        self.db = db

    def get_schools(self):
        self.db.query(Schools).all()
    
    def get_school_by_id(self, school_id:int):
        return self.db.query(Schools).filter(Schools.id == school_id).first() 
    
    def get_email_by_id(self, email_id:str):
        return self.db.query(Schools).filter(Schools.email == email_id).first()

    def create_school(self, data:SchoolCreate):
        school_data = Schools(**data.model_dump())
        self.db.add(school_data)
        self.db.commit()
        self.db.refresh(school_data)
        return school_data
    
    def delete(self, school_id:int):
        school = self.db.query(Schools).filter(Schools.id == school_id).first()
        if not school:
            return None
        self.db.delete(school)
        self.db.commit()
        return school