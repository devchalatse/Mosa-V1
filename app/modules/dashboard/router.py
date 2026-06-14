from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.dependencies import get_db
from .controller import DashboardController

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def get_dashboard_metrics(db: Session = Depends(get_db)):
    """
    Endpoint to fetch dashboard statistics.
    Instantiates the controller with the current DB session.
    """
    try:
        # 1. Instantiate the controller with the active DB session instance
        controller = DashboardController(db)
        
        # 2. Call the controller method and return the data dict
        return controller.get_dashboard_stats()
        
    except ValueError as e:
        # Catch any runtime ValueErrors safely and return a 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))
