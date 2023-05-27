from pydantic import BaseModel

from app.dto.shipment import Shipment


class TransportDistance(BaseModel):
    number: str
    distance: float


class SingleShipment(Shipment):
    transports_distances: list[TransportDistance]


SingleShipment.update_forward_refs()
