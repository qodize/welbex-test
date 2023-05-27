from pydantic import BaseModel

from app.dto.location import Location


class Shipment(BaseModel):
    shipment_id: int
    pick_up_location: Location
    delivery_location: Location
    weight: int
    description: str


Shipment.update_forward_refs()
