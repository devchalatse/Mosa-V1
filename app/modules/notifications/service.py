from .models import Notification
from .schema import NotificationCreate
from .repository import NotificationRepository
from sqlalchemy.orm import Session


class NotificationService:
    def __init__(self, db:Session):
        self.repo = NotificationRepository(db)

    # Get all the notifications
    def get_all_notifications(self):
        return self.repo.get_all_notifications()

    # Get notifications by id
    def get_notification_by_id(self, notification_id:int):
        not1 = self.repo.get_notification_by_id(notification_id)
        if not not1:
            raise ValueError("Notification ID not found")
        return not1

    # create notification
    def create_notification(self, data: NotificationCreate):
        return self.repo.createNotification(data)

    # Delete Notification
    def delete_notification(self, delete_id: int):
        not2 = self.repo.deleteNotification(delete_id)
        if not not2:
            raise ValueError("Unable to delete Notification ID")
        return not2


