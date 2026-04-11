from sqlalchemy.orm import Session
from .model import dashboard
from .schema import createDashboard


class dashboardRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all_user_dashboard(self):
        return self.db.query(dashboard).all()
    
    def get_dashboard_by_id(self, dashboard_id:int):
        return self.db.query(dashboard).filter(dashboard.id == dashboard_id).first()
    
    def get_dashboard_by_users(self, user_id:int):
        return self.db.query(dashboard).filter(dashboard.user_id == user_id).all()
    
    def get_dashboard_by_items(self, items_id:int):
        return self.db.query(dashboard).filter(dashboard.items_id == items_id).all()
    
    def get_dashboard_by_donation(self, donation_id:int):
        return self.db.query(dashboard).filter(dashboard.donation_id == donation_id).all()
    
    def get_dashboard_school(self, school_id:int):
        return self.db.query(dashboard).filter(dashboard.school_id == school_id).all()
    
    def create_dashboard(self, data:createDashboard):
        Dashboard = dashboard(**data.model_dump())
        self.db.add(dashboard)
        self.db.commit()
        self.db.refresh(dashboard)
        return Dashboard
    
    def delete(self, dashboard_id:int):
        Dashboard = self.db.query(dashboard).filter(dashboard.donation_id == dashboard_id).first()
        if not Dashboard:
            return None
        self.db.delete(dashboard)
        self.db.commit()
        self.db.refresh(dashboard)
        return Dashboard
    
