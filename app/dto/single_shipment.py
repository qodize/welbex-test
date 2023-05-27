from app.dto.shipment import Shipment


class SingleShipment(Shipment):
    closest_transports: list[str]


SingleShipment.update_forward_refs()
