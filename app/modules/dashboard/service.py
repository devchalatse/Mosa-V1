from .repository import Dashboard


class DashboardService:

    def __init__(self, repo: Dashboard):
        self.repo = repo


    def get_dashboard(self):

        return {
            "total_users": self.repo.total_users(),
            "total_schools": self.repo.total_schools(),
            "total_items": self.repo.total_items(),
            "total_donations": self.repo.total_donations(),
            "new_users_today": self.repo.new_users_today()
        }