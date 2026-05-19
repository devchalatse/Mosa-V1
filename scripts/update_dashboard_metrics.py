from app.db.database import SessionLocal
from app.modules import users,schools,items,drivers, donations

def update_metrics():
    db = SessionLocal()

    Users = db.query(users).count()
    Schools = db.query(schools).count()
    Items = db.query(items).count()
    Drivers = db.query(drivers).count()
    Donation = db.query(donations).count()

    print("Users:", users)
    print("Schools:", schools)
    print("Items:", items)
    print("Donation", donations)
    print("Driver", drivers)
    

if __name__ == "__main__":
    update_metrics()