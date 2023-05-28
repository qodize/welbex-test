from pydantic import BaseModel


class UpdateTransport(BaseModel):
    current_zipcode: str


UpdateTransport.update_forward_refs()
