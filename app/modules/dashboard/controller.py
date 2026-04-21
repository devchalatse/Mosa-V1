from sqlalchemy.orm import Session
from fastapi import HTTPException
from .model import dashboard
from .schema import createDashboard
from .service import dashboardService

class dashboardController:
    def __init__(self, db:Session):
        self.service = dashboardService(db)

    def get_all_dashboard(self):
        dashboard = self.service.get_all_dashboard()
        return {"status":"success", "data": dashboard}
    
    def get_dashboard_by_userid(self, user_id:int):
        try:
            user = self.service.get_dashboard_by_users(user_id)
            return {"status":"success", "data": user_id}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
    def get_dashboard_by_items(self, items_id:int):
        try:
            item = self.service.get_dashboard_by_item(items_id)
            return {"status":"success", "data": items_id}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
    
    def get_dashboard_by_school(self, school_id:int):
        try:
            school = self.service.get_dashboard_by_school(school_id)
            return {"status":"success", "data":school}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
    
    def get_dashboard_donation(self, donation_id:int):
        try:
            donation = self.service.get_dashboard_by_donation(donation_id)
            return {"status":"success", "data":donation}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        
    def create_dashboard(self, data:createDashboard):
        try:
            create_dashboard = self.service.create_dashboard(data)
            return {"status":"success", "data":data}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))

    
        
    
    