from fastapi import APIRouter, Depends
from app.db.dependencies import get_db
from .schema import NotificationCreate
from .controller import NotificationController
from sqlalchemy.orm import Session


router = APIRouter(prefix="/items", tags=["Notification"])

#  FIX: Changed ', Depends=(get_db)' to '= Depends(get_db)'
@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    return NotificationController(db).get_all_notififactions()

@router.post("/")
def create_notifications(data: NotificationCreate, db: Session = Depends(get_db)):
    return NotificationController(db).create_notification(data)

@router.get("/{notification_id}")
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    return NotificationController(db).get_notification_by_id(notification_id)

@router.delete("/{delete_id}")
def delete_notification(delete_id: int, db: Session = Depends(get_db)):
    return NotificationController(db).delete_notification(delete_id)


