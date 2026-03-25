from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import UserResponse, UserSignUp, UserLogin
from .service import UserService

class UserController:
    def __init__(self, db: Session):
        self.service = UserService(db)
    
    def get_users(self):
        users = self.service.get_users()
        return {"status": "success", "data": users}
    
    def get_one(self, user_id: int):
        try:
            user = self.service.get_user_id(user_id)
            return {"status": "success", "data": user}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        
    def login(self, email: str, password: str):  
        try:
            token = self.service.login(email, password)  
            return {"status": "success", "data": token}  
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))  
    
    def create(self, data: UserSignUp):
        try:
            createUser = self.service.create(data) 
            return {"status": "success", "data": createUser}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))