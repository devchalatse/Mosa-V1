from .models import Notification
from .schema import NotificationCreate
from .service import NotificationService
from sqlalchemy.orm import Session
from fastapi import HTTPException

class controllerNotification:
    def __init__(self, db:Session):
        self.service = NotificationService(db)

    def get_all_notififactions(self):
        not1 = self.service.get_all_notifications()
        return{"status":"success", "data": not1}

    def get_notification_by_id(self, notification_id:int):
        try:
            not2 = self.service.get_notification_by_id(notification_id)
            return {"status":"success", "data": not2}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))

    