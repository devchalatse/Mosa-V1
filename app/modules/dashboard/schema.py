from pydantic import BaseModel
from .models import Dashboard

class DashboardResponse(BaseModel):
    total_users:int
    total_schools:int
    total_items:int
    total_donations:int
    new_users:int


