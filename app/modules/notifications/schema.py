from pydantic import BaseModel
from .models import Notification, NotificationStatus

class NotificationCreate(BaseModel):
    driver_id: int
    school_id: int
    item_id: int
    user_id: int
    quantity: int

class NotificationResponse(BaseModel):
    id: int
    driver_id: int
    school_id: int
    item_id: int
    user_id: int
    status: int

    class Config:
        from_attribute=True

class NotificationUpdateStatus(BaseModel):
    status:NotificationStatus

    