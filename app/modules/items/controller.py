from fastapi import HTTPException
from .service import ServiceItems
from sqlalchemy.orm import Session
from .schemas import Items

class ControllerItems:
    def __init__(self, db:Session):
        self.service = ServiceItems(db)

    def get_all_items(self):
        items = self.service.get_items()
        return {"status":"success", "data": items}
    
    def get_items_by_id(self, item_id:int):
        try:
            item = self.service.get_item_by_id(item_id)
            return {"status":"success", "data":item}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    def get_item_by_category(self, category_id:str):
        try:
            category = self.service.get_item_by_category(category_id)
            return {"status":"success", "data":category}
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
    
    def create_item(self, data:Items):
        try:
            item_create = self.service.create_items(data)
            return {"status":"success", "data":data}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    def delete(self, item_id:int):
        try:
            delete_item = self.service.delete(item_id)
            return {"status":"success", "data":item_id}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    