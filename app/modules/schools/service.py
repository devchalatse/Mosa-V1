from sqlalchemy.orm import Session
from .schemas import SchoolCreate  
from .repository import RepositorySchools

class ServiceSchools:
    def __init__(self, db: Session):
        self.repo = RepositorySchools(db)

    def get_all_schools(self):
        return self.repo.get_schools()

    def get_school_by_id(self, school_id: int):
        school = self.repo.get_school_by_id(school_id)
        if not school:
            raise ValueError("School not found")
        return school  

    def get_school_by_email(self, email_id: str):
        email = self.repo.get_email_by_id(email_id)
        if not email:
            raise ValueError("Email not found")
        return email

    def create(self, data: SchoolCreate):
        return self.repo.create_school(data)

    def delete(self, school_id: int):
        delete_school = self.repo.get_school_by_id(school_id)
        if not delete_school:
            raise ValueError("Invalid school details")
        return self.repo.delete(school_id)