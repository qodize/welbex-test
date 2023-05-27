from pydantic import BaseModel


class Location(BaseModel):
    id: int
    state: str
    zipcode: str
    latitude: float
    longitude: float


Location.update_forward_refs()
