from sqlalchemy.orm import Session
from .models import Notification, NotificationStatus
from .schema import NotificationCreate

from app.modules.items.models import SchoolItems
from app.modules.schools.models import School
from app.modules.users.models import User

class NotificationRepository:
    def __init__(self, db:Session):
        self.db = db 

    def get_notification(self):
        return self.db.query(Notification).all()

    def get_notification_by_id(self, notification_id):
        return self.db.query(Notification).filter(Notification.id == notification_id).first()



    
    
