import uuid

from sqlalchemy import BOOLEAN, INT, TEXT, VARCHAR, Column, ForeignKey
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

    # boolean
    sold_by = Column(BOOLEAN(), nullable=False)
    gearbox = Column(BOOLEAN(), nullable=False)

    # numerical
    km = Column(INT(), nullable=False)
    power = Column(INT(), nullable=False)
    engine = Column(INT(), nullable=False)
    year = Column(INT(), nullable=False)

    # description
    description = Column(TEXT(), nullable=False)

    # prediction
    prediction = Column(VARCHAR(255), nullable=False)

    created_at = Column(VARCHAR(255), nullable=False)
