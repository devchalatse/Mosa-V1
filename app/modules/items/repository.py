from sqlalchemy.orm import Session
from .models import SchoolItems
from .schemas import Items

class RepositoryItems:
    def __init__(self, db: Session):
        self.db = db

    def get_all_items(self):
        return self.db.query(SchoolItems).all()
    
    def get_item_by_id(self, item_id: int):
        return self.db.query(SchoolItems).filter(SchoolItems.id == item_id).first()
    
    def get_item_by_category(self, category_id:str):
        return self.db.query(SchoolItems).filter(SchoolItems.category == category_id).first()
    
    def create_items(self, data:Items):
        items = SchoolItems(**data.model_dump())
        self.db.add(items)
        self.db.commit()
        self.db.refresh(items)
        return items
    
    def delete_items(self, delete_id:int):
        item = self.db.query(Items).filter(SchoolItems.id == delete_id).first()
        if not item:
            return None
        self.db.delete(item)
        self.db.commit()
        
