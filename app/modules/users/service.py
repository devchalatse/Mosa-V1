from sqlalchemy.orm import Session
from .schemas import UserSignUp
from .repository import UserRepository

class UserService:
    def __init__(self, db:Session):
        self.repo = UserRepository(db)

    def get_users(self):
        return self.repo.get_all_users()
    
    def get_users_id(self, user_id:int):
        user = self.get_users_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user
    
    def create(self, data:UserSignUp):
        return self.repo.create(data)
    
    