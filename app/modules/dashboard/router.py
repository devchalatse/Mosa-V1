from fastapi import APIRouter, Depends
from .service import DashboardService


router = APIRouter()


@router.get("/dashboard")
def get_dashboard(
    service: DashboardService = Depends(get_dashboard_service)
):

    return service.get_dashboard()