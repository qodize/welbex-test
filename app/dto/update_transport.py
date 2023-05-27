from pydantic import BaseModel


class UpdateTransport(BaseModel):
    location_zipcode: str


UpdateTransport.update_forward_refs()
