from app.db.models.location_model import LocationModel
from app.db.models.shipment_model import ShipmentModel
from app.dto.create_location import CreateLocation
from app.dto.create_shipment import CreateShipment
from app.dto.location import Location
from app.dto.shipment import Shipment

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
