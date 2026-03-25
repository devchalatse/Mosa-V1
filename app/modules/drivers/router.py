from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from db.dependencies import get_db
from .controller import DriverController
from .schemas import DriverCreate, DriverLocationUpdate
from typing import Dict

router = APIRouter(prefix="/drivers", tags=["drivers"])

# Store active websocket connections
active_connections: Dict[int, WebSocket] = {}


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return DriverController(db).get_all()


@router.get("/{driver_id}")
def get_one(driver_id: int, db: Session = Depends(get_db)):
    return DriverController(db).get_one(driver_id)


@router.post("/")
def create(data: DriverCreate, db: Session = Depends(get_db)):
    return DriverController(db).create(data)


@router.patch("/{driver_id}/location")
def update_location(driver_id: int, data: DriverLocationUpdate, db: Session = Depends(get_db)):
    return DriverController(db).update_location(driver_id, data)


@router.patch("/{driver_id}/status")
def update_status(driver_id: int, status: str, db: Session = Depends(get_db)):
    return DriverController(db).update_status(driver_id, status)


@router.get("/nearest")
def get_nearest(lat: float, lng: float, db: Session = Depends(get_db)):
    return DriverController(db).get_nearest(lat, lng)


# WebSocket for real-time driver location
@router.websocket("/ws/{driver_id}")
async def driver_websocket(websocket: WebSocket, driver_id: int, db: Session = Depends(get_db)):
    await websocket.accept()
    active_connections[driver_id] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            lat = data["lat"]
            lng = data["lng"]

            # Update location in DB
            DriverController(db).update_location(
                driver_id,
                DriverLocationUpdate(lat=lat, lng=lng)
            )

            # Broadcast to all connected clients
            for cid, connection in active_connections.items():
                if cid != driver_id:
                    await connection.send_json({
                        "driver_id": driver_id,
                        "lat": lat,
                        "lng": lng
                    })
    except WebSocketDisconnect:
        del active_connections[driver_id]