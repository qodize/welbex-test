from pydantic import BaseModel


class CreateTransport(BaseModel):
    number: str
    max_weight: int
