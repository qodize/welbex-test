from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.db.database import Base
from app.db.models.location_model import LocationModel


class TransportModel(Base):
    __tablename__ = 'transports'
    transport_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str]
    current_zipcode: Mapped[str] = mapped_column(ForeignKey('locations.zipcode'))
    max_weight: Mapped[int]

    current_location: Mapped['LocationModel'] = relationship(foreign_keys=current_zipcode)
