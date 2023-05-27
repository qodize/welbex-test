from app.db.models.location_model import LocationModel
from app.dto.create_location import CreateLocation
from app.dto.location import Location

mappers = {
    LocationModel: {
        Location: lambda location_model: Location(
            location_id=location_model.location_id,
            state=location_model.state,
            zipcode=location_model.zipcode,
            latitude=location_model.latitude,
            longitude=location_model.longitude,
        )
    },
    CreateLocation: {
        LocationModel: lambda create_dto: LocationModel(
            state=create_dto.state,
            zipcode=create_dto.zipcode,
            latitude=create_dto.latitude,
            longitude=create_dto.longitude
        )
    },

}
