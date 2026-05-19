from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .repository import Dashboard
from .service import DashboardService

router = APIRouter()


def get_dashboard_service(db: Session = Depends(get_db)):
    repo = Dashboard(db)
    return DashboardService(repo)


@router.get("/dashboard")
def get_dashboard(service: DashboardService = Depends(get_dashboard_service)):
    return service.get_dashboard()