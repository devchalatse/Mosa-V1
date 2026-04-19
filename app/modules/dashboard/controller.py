from sqlalchemy.orm import Session
from .model import dashboard
from .schema import createDashboard
from .service import dashboardService

class DonationController:
    def __init__(self, db:Session):
        self.service = dashboardService(db)

    def get_all_users(self):
        return self.service.get_all_dashboard()

    def get_dashboard_by_id(self, dashboard_id:int):
        return self.service.get_dashboard_by_id(dashboard_id)
    
    def get_dashboard_by_item(self, item_id:int):
        return self.service.get_dashboard_by_item(item_id)
    
    def get_dashboard_by_school(self, school_id:int):
        return self.service.get_dashboard_by_item(school_id)
    
    
    
    
        