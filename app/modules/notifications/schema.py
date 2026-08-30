from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NotificationBase(BaseModel):
    title: str
    message: str


class NotificationCreate(NotificationBase):
    recipient_id: int


class NotificationResponse(NotificationBase):
    id: int
    recipient_id: int
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class NotificationReadUpdate(BaseModel):
    is_read: bool