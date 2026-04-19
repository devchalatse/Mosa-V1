from .model import dashboard
from .schema import createDashboard
from sqlalchemy.orm import Session
from .repository import dashboardRepository

class dashboardService:
    def __init__(self, db:Session):
        self.repo = dashboardRepository(db)

    def get_all_dashboard(self):
        return self.repo.get_all_user_dashboard()
    
    def get_dashboard_by_id(self, dashboard_id:int):
        dashboard = self.get_dashboard_by_id(dashboard_id)
        if not dashboard:
            raise ValueError("Dashboard not found")
        return dashboard
    
    def get_dashboard_by_school(self, school_id:int):
        School = self.repo.get_dashboard_school(school_id)
        if not School:
            raise ValueError ("School not found")
        return School

    def get_dashboard_by_item(self, item_id:int):
        Items = self.repo.get_dashboard_by_items(item_id)
        if not Items:
            raise ValueError ("Items not found")
        return Items

    def get_dashboard_by_donation(self, donation_id:int):
        donation = self.repo.get_dashboard_by_donation(donation_id)
        if not donation:
            raise ValueError ("donation nof found")
        return donation
    
    