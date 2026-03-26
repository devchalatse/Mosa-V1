from sqlalchemy.orm import Session
from .schemas import SchoolCreate
from .repository import RepositorySchools
from utils.email import send_school_verification_email
from utils.jwt_handler import create_access_token


class ServiceSchools:
    def __init__(self, db: Session):
        self.repo = RepositorySchools(db)

    # GET ALL
    def get_all_schools(self):
        return self.repo.get_schools()

    # GET BY ID
    def get_school_by_id(self, school_id: int):
        school = self.repo.get_school_by_id(school_id)
        if not school:
            raise ValueError("School not found")
        return school

    # GET BY EMAIL
    def get_school_by_email(self, email: str):
        school = self.repo.get_school_by_email(email)
        if not school:
            raise ValueError("School not found")
        return school

    # CREATE + AUTO VERIFY
    def create(self, data: SchoolCreate):
        school = self.repo.create_school(data)

        #TODO uncomment once government_schools table is populated
        # if school.emis_number:
        #     gov_school = self.repo.match_school_by_emis(school.emis_number)
        #     if gov_school:
        #         school = self.repo.set_auto_verified(school.id)

        return school

    # DELETE
    def delete(self, school_id: int):
        school = self.repo.get_school_by_id(school_id)
        if not school:
            raise ValueError("Invalid school details")
        return self.repo.delete(school_id)

    # MANUAL VERIFY
    def verify_school(self, school_id: int):
        school = self.repo.verify_school(school_id)

        if not school:
            raise ValueError("School not found")

        token = create_access_token({
        "school_id": school.id,
        "email": school.email
    })

        send_school_verification_email(school.email, school.name)
        print("Email triggered for:", school.email)  

        return {"access_token": token, "token_type": "bearer", "school": school}

    # NEARBY SCHOOLS
    def get_nearby_schools(self, lat: float, lng: float, radius: float = 10):
        schools = self.repo.get_nearby_schools(lat, lng, radius)

        if not schools:
            return []

        return schools