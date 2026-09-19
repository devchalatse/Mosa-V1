from fastapi import APIRouter, Depends
from app.db.dependencies import get_db
from .schema import NotificationCreate
from .controller import controllerNotification
from sqlalchemy.orm import Session


router = APIRouter(prefix="/items", tags=["Notification"])

@router.get('/')
def get_notifications(db: Session, Depends=(get_db)):
    return controllerNotification(db).get_all_notififactions()

@router.post("/")
def create_notifications(data:NotificationCreate, db:Session, Depends =(get_db)):
    return controllerNotification(db).create_notification(data)

@router.get("/{notification_id}")
def get_notification(notification_id:int, db:Session, Depends=(get_db)):
    return controllerNotification(db).get_notification_by_id(notification_id)

@router.delete("/{delete_id}")
def delete_notification(delete_id:int, db:Session, Depends=(get_db)):
    return controllerNotification(db).delete_notification(delete_id)



