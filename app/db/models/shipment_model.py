from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.db.database import Base
from app.db.models.location_model import LocationModel


class ShipmentModel(Base):
    __tablename__ = 'shipments'
    shipment_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pick_up_zipcode: Mapped[str] = mapped_column(ForeignKey('locations.zipcode'))
    delivery_zipcode: Mapped[str] = mapped_column(ForeignKey('locations.zipcode'))
    weight: Mapped[int]
    description: Mapped[str]

    pick_up_location: Mapped['LocationModel'] = relationship(foreign_keys=pick_up_zipcode, lazy=False)
    delivery_location: Mapped['LocationModel'] = relationship(foreign_keys=delivery_zipcode, lazy=False)
