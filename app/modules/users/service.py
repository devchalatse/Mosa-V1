from sqlalchemy.orm import Session
from .schemas import UserSignUp
from .repository import UserRepository
from datetime import datetime, timedelta
from passlib.context import CryptContext

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_users(self):
        return self.repo.get_all_users()

    def get_user_id(self, user_id: int):
        user = self.repo.get_user_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user
    
    def get_email_by_id(self, email:str):
        email_id = self.repo.get_email_by_id(email)
        if not email:
            raise ValueError("Invalid Credentials")
        

    def create(self, data: UserSignUp):
        return self.repo.create(data)