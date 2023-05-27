from typing import Optional
from pydantic import BaseModel


class UpdateShipment(BaseModel):
    weight: Optional[int]
    description: Optional[str]
