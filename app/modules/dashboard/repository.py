from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from users.models import User
from items.models import SchoolItems
from schools.models import School
from donations.models import Donation

class Dashboard:
    def __init__(self, db:Session):
        self.db = db

    def total_users(self):
        return self.db.query(func.count(User.id)).scalar()
    
    def total_items(self):
        return self.db.query(func.count(SchoolItems.id)).scalar()
    
    def total_schools(self):
        return self.db.query(func.count(School.id)).scalar()
    
    def total_donations(self):
        return self.db.query(func.count(Donation.id)).scalar()
    
    def new_users_today(self):
        today = date.today()

        return (
            self.db.query(func.count(User.id))
            .filter(func.date(User.created_at) == today)
            .scalar()
        )