from pydantic import BaseModel


class CreateTransport(BaseModel):
    transport_id: int
    number: str
    current_location_zipcode: str
    max_weight: int
