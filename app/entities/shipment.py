from pydantic import BaseModel

from app.entities.location import Location


class Shipment(BaseModel):
    id: int
    pick_up: Location
    delivery: Location
    weight: int
    description: str


Shipment.update_forward_refs()
