from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from modules.users.models import User
from modules.items.models import SchoolItems
from modules.schools.models import School
from modules.donations.models import Donation

class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def total_users(self) -> int:
        return self.db.query(func.count(User.id)).scalar() or 0
    
    def total_items(self) -> int:
        return self.db.query(func.count(SchoolItems.id)).scalar() or 0
    
    def total_schools(self) -> int:
        return self.db.query(func.count(School.id)).scalar() or 0
    
    def total_donations(self) -> int:
        return self.db.query(func.count(Donation.id)).scalar() or 0
    
    def new_users_today(self) -> int:
        today = date.today()
        return (
            self.db.query(func.count(User.id))
            # 💡 Replace 'date_joined' with your actual User model field name
            .filter(func.date(User.date_joined) == today) 
            .scalar() or 0
        )
