from .models import Dashboard
from pydantic import BaseModel

class createDashboard(BaseModel):
    user_id:int
    school_id:int
    donation_id:int
    items_id:int
    
class DashboardResponse(BaseModel):
    user_id:int
    school_id:int
    donation_id:int

    class config:
        from_attributes = True