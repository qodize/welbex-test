from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class LocationModel(Base):
    __tablename__ = 'locations'
    location_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    state: Mapped[str]
    zipcode: Mapped[str] = mapped_column(unique=True)
    latitude: Mapped[float]
    longitude: Mapped[float]
