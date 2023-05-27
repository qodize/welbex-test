from pydantic import BaseModel

from app.dto.location import Location


class Transport(BaseModel):
    id: int
    number: str
    current_location: Location
    max_weight: int


Transport.update_forward_refs()
