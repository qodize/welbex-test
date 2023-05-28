from typing import Optional

from pydantic import BaseModel


class CreateTransport(BaseModel):
    number: str
    current_zipcode: Optional[str]
    max_weight: int
