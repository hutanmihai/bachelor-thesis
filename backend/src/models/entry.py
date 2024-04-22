import uuid

from sqlalchemy import INT, TEXT, VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import BaseModel
from src.models.mixin import TimestampMixin


class Entry(TimestampMixin, BaseModel):
    __tablename__ = "entry"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(ForeignKey("user.id"), nullable=False)

    # categorical
    manufacturer = Column(VARCHAR(255), nullable=False)
    model = Column(VARCHAR(255), nullable=False)
    fuel = Column(VARCHAR(255), nullable=False)
    chassis = Column(VARCHAR(255), nullable=False)
    sold_by = Column(VARCHAR(255), nullable=False)
    gearbox = Column(VARCHAR(255), nullable=False)

    # numerical
    km = Column(INT(), nullable=False)
    power = Column(INT(), nullable=False)
    engine = Column(INT(), nullable=False)
    year = Column(INT(), nullable=False)

    # description
    description = Column(TEXT(), nullable=False)

    # prediction
    prediction = Column(INT(), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manufacturer = kwargs.get("manufacturer")
        self.model = kwargs.get("model")
        self.fuel = kwargs.get("fuel")
        self.chassis = kwargs.get("chassis")
        self.sold_by = kwargs.get("sold_by")
        self.gearbox = kwargs.get("gearbox")
        self.km = kwargs.get("km")
        self.power = kwargs.get("power")
        self.engine = kwargs.get("engine")
        self.year = kwargs.get("year")
        self.description = kwargs.get("description")
        self.prediction = kwargs.get("prediction")
        self.user_id = kwargs.get("user_id")
