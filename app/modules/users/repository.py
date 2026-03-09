from sqlalchemy.orm import Session
from .models import User
from .schemas import UserSignUp

class UserRepository:
    def __init__(self, db:Session):
        self.db =db

    #Get all user
    def get_all_users(self):
        return self.db.query(User).all
    
    #Get user by id
    def get_user_id(self, user_id:int):
        return self.db.query(User).filter(User.id == user_id).first()

    #Get user by email
    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    #Create user and save the user
    def create(self, data:UserSignUp):
        user = User(**data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    