from sqlalchemy.orm import Session
from .schemas import Items
from .repository import RepositoryItems

class ServiceItems:
    def __init__(self, db:Session):
        self.repo = RepositoryItems(db)

    def get_items(self):
        return self.repo.get_all_items()
    
    def get_item_by_id(self, item_id:int):
        items = self.repo.get_item_by_id(item_id)
        if not items:
            raise ValueError("Item not found")
        return items
    
    def get_item_by_category(self, category_id:str):
        category = self.repo.get_item_by_category(category_id)
        if not category:
            raise ValueError("Item not part of the category list")
        return category
    
    def create_items(self, data:Items):
        create = self.repo.create_items(data)
    
    def delete(self, item_id:int):
        item = self.repo.get_item_by_id(item_id)
        if not item:
            raise ValueError("Item not found")
        return self.repo.delete(item_id)
    
    
    

