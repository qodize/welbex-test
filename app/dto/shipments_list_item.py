from app.dto.shipment import Shipment


class ShipmentsListItem(Shipment):
    closest_transports_count: int


ShipmentsListItem.update_forward_refs()
