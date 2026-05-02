from sqlalchemy.orm import Session
from .models import Dashboard
from .schema import createDashboard


class dashboardRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_dashboard_by_id(self):
        return self.db.query(Dashboard).all()
    
    
