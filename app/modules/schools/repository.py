from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from .models import Schools  # your schools table


class RepositorySchools:
    def __init__(self, db: Session):
        self.db = db

    #  GET ALL
    def get_schools(self):
        return self.db.query(Schools).all()

    #  GET BY ID
    def get_school_by_id(self, school_id: int):
        return self.db.query(Schools).filter(Schools.id == school_id).first()

    #  GET BY EMAIL
    def get_school_by_email(self, email: str):
        return self.db.query(Schools).filter(Schools.email == email).first()

    #  CREATE
    def create_school(self, data):
        school = Schools(**data.dict())
        self.db.add(school)
        self.db.commit()
        self.db.refresh(school)
        return school

    #  DELETE
    def delete(self, school_id: int):
        school = self.get_school_by_id(school_id)
        self.db.delete(school)
        self.db.commit()
        return {"message": "School deleted successfully"}

    # MANUAL VERIFY
    def verify_school(self, school_id: int):
        school = self.get_school_by_id(school_id)

        if not school:
            return None

        school.verified = True
        school.verification_status = "approved"
        school.verified_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(school)

        return school

    # AUTO VERIFY (EMIS MATCH)
    def match_school_by_emis(self, emis_number: str):
        query = text("""
            SELECT * FROM government_schools
            WHERE emis_number = :emis
        """)
        return self.db.execute(query, {"emis": emis_number}).fetchone()

    def set_auto_verified(self, school_id: int):
        school = self.get_school_by_id(school_id)

        school.verified = True # pyright: ignore[reportOptionalMemberAccess]
        school.source = "DBE" # type: ignore
        school.verification_status = "auto_verified" # pyright: ignore[reportOptionalMemberAccess]
        school.verified_at = datetime.utcnow() # type: ignore

        self.db.commit()
        self.db.refresh(school)

        return school

    # NEARBY SCHOOLS
    def get_nearby_schools(self, lat: float, lng: float, radius: float):
        query = text("""
        SELECT *,
        (
          6371 * acos(
            cos(radians(:lat)) *
            cos(radians(latitude)) *
            cos(radians(longitude) - radians(:lng)) +
            sin(radians(:lat)) *
            sin(radians(latitude))
          )
        ) AS distance
        FROM recipients
        WHERE verification_status IN ('approved', 'auto_verified')
        HAVING distance < :radius
        ORDER BY distance
        LIMIT 20;
        """)

        result = self.db.execute(query, {
            "lat": lat,
            "lng": lng,
            "radius": radius
        })

        return result.fetchall()