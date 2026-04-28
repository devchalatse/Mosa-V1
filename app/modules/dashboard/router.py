from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.dependencies import get_db
from .controller import dashboardController
from .models import Dashboard
from .schema import createDashboard, DashboardResponse


router = APIRouter(prefix='/dashboard', tags=["Dashboard"])

@router.get("/")
def get_all_dashboard(db:Session = Depends(get_db)):
    return dashboardController(db).get_all_dashboard()

@router.get('/dashboard')
def get_the_dashboard(dashboard_id:int, db:Session =Depends(get_db)):
    return dashboardController(db).get_dashboard_by_id(dashboard_id)

@router.get("/dashboard/{user_id}")
def get_dashboard_by_id(user_id:int, db:Session =Depends(get_db)):
    return dashboardController(db).get_dashboard_by_userid(user_id)

@router.get("/dashboard/{item_id}")
def get_item_by_id(item_id:int, db:Session = Depends(get_db)):
    return dashboardController(db).get_dashboard_by_items(item_id)

@router.get("/dashboard/{user_id}")
def get_user_by_id(user_id:int, db:Session = Depends(get_db)):
    return dashboardController(db).get_dashboard_by_user(user_id)

@router.get("/dashboard/{school_id}")
def get_dashboard_by_school(school_id:int, db:Session = Depends(get_db)):
    return dashboardController(db).get_dashboard_by_school(school_id)

@router.get("/dashboard/{donation_id}")
def get_dashboard_by_donation(donation_id:int, db:Session = Depends(get_db)):
    return dashboardController(db).get_dashboard_donation(donation_id)

@router.post("/dashboard")
def create_dashboard(data:int, db:Session = Depends(get_db)):
    return dashboardController.create_dashboard(data)

@router.delete("/dashboard/{dashboard_id}")
def delete_dashboard(dashboard_id:int, db:Session = Depends(get_db)):
    return dashboardController(db).delete_dashboard(dashboard_id)






