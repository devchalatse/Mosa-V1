from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import UserResponse, UserSignUp
from .service import UserService

class UserController:
    def __init__(self, db:Session):
        self.service = UserService(db)
    
    def get_users(self):
        users = self.service.get_users()
        return {"status":"success", "data":users}
    
    def get_one(self, user_id:int):
        try:
            user = self.service.get_user_id(user_id)
            return {"status":"success", "data":user}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
    
    def get_email_id(self, email:str):
        try:
            email = self.service.get_email_by_id(email) # type: ignore
            return{"status":"success", "data": email}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        return {
        "access_token": token,
        "token_type": "bearer"
    }
    
    def create(self, data:UserSignUp):
        try:
            createUser = self.service.create(data)
            return {"status":"success", "data":createUser}
        except ValueError as e:
             raise HTTPException(status_code=400, detail=str(e))

    


