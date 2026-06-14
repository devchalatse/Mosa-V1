from .repository import DashboardRepository
from sqlalchemy.orm import Session

class DashboardService:

    def __init__(self, db: Session):
        self.repo = DashboardRepository(db)


    def get_dashboard(self):

        return {
            "total_users": self.repo.total_users(),
            "total_schools": self.repo.total_schools(),
            "total_items": self.repo.total_items(),
            "total_donations": self.repo.total_donations(),
            "new_users_today": self.repo.new_users_today()
        }
    