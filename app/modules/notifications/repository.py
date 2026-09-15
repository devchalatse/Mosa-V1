from .models import Notification
from .schema import NotificationCreate
from sqlalchemy.orm import Session


class NotificationRepository:
    def __init__(self, db:Session ):
        self.db = db

    # Get all the notifications
    def get_all_notifications(self):
        return self.db.query(Notification).all()

    # Get notifications by ID
    def get_notification_by_id(self, notification_id: int):
        return self.db.query(Notification).filter(Notification.id == notification_id).first()

    # Create Notifications
    def createNotification(self, data: NotificationCreate):
        not1 = Notification(**data.model_dump())
        self.db.add(not1)
        self.db.commit()
        self.db.refresh(not1)
        return not1

    # delete a Notification
    def deleteNotification(self, delete_id:int):
        delete1 = self.db.query(Notification).filter(Notification.id == delete_id).first()
        if not delete1:
            return None
        self.db.delete(delete1)
        self.db.commit()

    