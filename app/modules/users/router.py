from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .controller import UserController
from db.dependencies import get_db
from .schemas import UserSignUp

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return UserController(db).get_users

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserController(db).get_one(user_id)

@router.post("/")
def createUser(data:UserSignUp, db:Session = Depends(get_db)):
    return UserController(db).create(data)


