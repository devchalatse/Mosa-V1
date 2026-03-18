from fastapi import APIRouter, Depends
from db.dependencies import get_db
from sqlalchemy.orm import Session
from .schemas import Items, ItemsResponse
from .controller import ControllerItems

router = APIRouter(prefix="/items", tags=["items"])

@router.get('/')
def get_all_items(db: Session = Depends(get_db)):
    return ControllerItems(db).get_all_items()

@router.get('/{item_id}')
def get_item_by_id(item_id: int, db:Session = Depends(get_db)):
    return ControllerItems(db).get_items_by_id(item_id)

@router.post("/items")
def create(data:Items, db:Session = Depends(get_db)):
    return ControllerItems(db).create_item(data)

@router.get('/{category_id}')
def get_item_by_category(category_id:str, db:Session =Depends(get_db)):
    return ControllerItems(db).get_item_by_category(category_id)

@router.delete('/{item_id}')
def delete(item_id:int, db:Session = Depends(get_db)):
    return ControllerItems(db).get_items_by_id(item_id)

