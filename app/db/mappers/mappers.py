from app.db.models.location_model import LocationModel
from app.db.models.shipment_model import ShipmentModel
from app.db.models.transport_model import TransportModel
from app.dto.create_location import CreateLocation
from app.dto.create_shipment import CreateShipment
from app.dto.create_transport import CreateTransport
from app.dto.location import Location
from app.dto.shipment import Shipment
from app.dto.transport import Transport

mappers = {}
mappers[LocationModel] = {}
mappers[LocationModel][Location] = lambda location_model: Location(
    location_id=location_model.location_id,
    state=location_model.state,
    zipcode=location_model.zipcode,
    latitude=location_model.latitude,
    longitude=location_model.longitude,
)
mappers[CreateLocation] = {}
mappers[CreateLocation][LocationModel] = lambda create_dto: LocationModel(
    state=create_dto.state,
    zipcode=create_dto.zipcode,
    latitude=create_dto.latitude,
    longitude=create_dto.longitude,
)
mappers[ShipmentModel] = {}
mappers[ShipmentModel][Shipment] = lambda shipment_model: Shipment(
    shipment_id=shipment_model.shipment_id,
    pick_up_location=mappers[LocationModel][Location](shipment_model.pick_up_location),
    delivery_location=mappers[LocationModel][Location](shipment_model.delivery_location),
    weight=shipment_model.weight,
    description=shipment_model.description,
)
mappers[CreateShipment] = {}
mappers[CreateShipment][ShipmentModel] = lambda create_dto: ShipmentModel(
    pick_up_zipcode=create_dto.pick_up_zipcode,
    delivery_zipcode=create_dto.delivery_zipcode,
    weight=create_dto.weight,
    description=create_dto.description,
)
mappers[CreateTransport] = {}
mappers[CreateTransport][TransportModel] = lambda create_dto: TransportModel(
    number=create_dto.number,
    current_zipcode=create_dto.current_zipcode,
    max_weight=create_dto.max_weight,
)
mappers[TransportModel] = {}
mappers[TransportModel][Transport] = lambda transport_model: Transport(
    transport_id=transport_model.transport_id,
    number=transport_model.number,
    current_location=mappers[LocationModel][Location](transport_model.current_location),
    max_weight=transport_model.max_weight,
)
