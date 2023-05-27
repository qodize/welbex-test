from pydantic import BaseModel


class CreateShipment(BaseModel):
    pick_up_zipcode: str
    delivery_zipcode: str
    weight: int
    description: str


CreateShipment.update_forward_refs()
