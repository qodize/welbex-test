from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    state: str
    zipcode: str
    latitude: float
    longitude: float


Location.update_forward_refs()
