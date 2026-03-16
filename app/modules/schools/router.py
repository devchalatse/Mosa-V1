from fastapi import APIRouter, Depends
from db.dependencies import get_db
from sqlalchemy.orm import Session
from .schemas import SchoolCreate, SchoolResponse
from .controller import schoolController

router = APIRouter(prefix="/schools", tags=["schools"])

@router.get('/')
def get_schools(db: Session = Depends(get_db)):
    return schoolController(db).get_all_schools()

@router.get('/{school_id}')
def get_school_id(school_id:int, db: Session = Depends(get_db)):
    return schoolController(db).get_schools_id(school_id)

@router.post('/')
def create_school (data:SchoolCreate, db: Session = Depends(get_db)):
    return schoolController(db).create(data)

@router.get('/{email_id}')
def get_school_by_email(email_id:str, db: Session = Depends(get_db)):
    return schoolController(db).get_email_id(email_id)

@router.delete('/{school_id}')
def delete(school_id:int, db: Session =Depends(get_db)):
    return schoolController(db).delete(school_id)
