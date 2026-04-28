from sqlalchemy.orm import Session
from .models import Dashboard
from .schema import createDashboard


class dashboardRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all_user_dashboard(self):
        return self.db.query(Dashboard).all()
    
    def get_dashboard_by_id(self, dashboard_id:int):
        return self.db.query(Dashboard).filter(Dashboard.id == dashboard_id).first()
    
    def get_dashboard_by_users(self, user_id:int):
        return self.db.query(Dashboard).filter(Dashboard.user_id == user_id).all()
    
    def get_dashboard_by_items(self, items_id:int):
        return self.db.query(Dashboard).filter(Dashboard.items_id == items_id).all()
    
    def get_dashboard_by_donation(self, donation_id:int):
        return self.db.query(Dashboard).filter(Dashboard.donation_id == donation_id).all()
    
    def get_dashboard_school(self, school_id:int):
        return self.db.query(Dashboard).filter(Dashboard.school_id == school_id).all()
    
    def create_dashboard(self, data:createDashboard):
        Dashboard = Dashboard(**data.model_dump())
        self.db.add(Dashboard)
        self.db.commit()
        self.db.refresh(Dashboard)
        return Dashboard
    
    def delete(self, dashboard_id:int):
        Dashboard = self.db.query(Dashboard).filter(Dashboard.donation_id == dashboard_id).first()
        if not Dashboard:
            return None
        self.db.delete(Dashboard)
        self.db.commit()
        self.db.refresh(Dashboard)
        return Dashboard
    
