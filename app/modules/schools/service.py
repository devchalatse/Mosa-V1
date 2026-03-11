from sqlalchemy.orm import Session
from .schemas import SchoolCreate
from .repository import SchoolRepository

class SchoolService:
    def __init__(self, db: Session): 
        self.repo = SchoolRepository(db)

    def get_all_schools(self):
        return self.repo.get_schools() 

    def get_school_by_id(self, school_id: int):
        school = self.repo.get_school_by_id(school_id)
        if not school:
            raise ValueError("School not found")
        return school

    def get_school_by_email(self, email: str):
        school = self.repo.get_school_by_email(email)
        if not school:
            raise ValueError("School not found")
        return school

    def create(self, data: SchoolCreate):
        return self.repo.create(data)

    def delete(self, school_id: int):
        school = self.repo.get_school_by_id(school_id)
        if not school:
            raise ValueError("School not found")
        return self.repo.delete(school_id) 