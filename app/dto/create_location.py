from pydantic import BaseModel


class CreateLocation(BaseModel):
    state: str
    zipcode: str
    latitude: float
    longitude: float


CreateLocation.update_forward_refs()
