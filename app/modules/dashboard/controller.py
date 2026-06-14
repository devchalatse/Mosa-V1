from sqlalchemy.orm import Session
from fastapi import Depends  # Optional: Include if using FastAPI dependency injection
from .service import DashboardService  # Adjust this import based on your actual file name

class DashboardController:
    def __init__(self, db: Session):
        """
        Initializes the controller with a database session.
        Passes the session directly to the DashboardService.
        """
        self.service = DashboardService(db)

    def get_dashboard_stats(self):
        """
        Handles the request to fetch all dashboard metrics.
        """
        return self.service.get_dashboard()
