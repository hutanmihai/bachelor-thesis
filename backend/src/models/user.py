import uuid

from sqlalchemy import INT, VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import BaseModel
from src.models.mixin import TimestampMixin


class User(TimestampMixin, BaseModel):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    predictions = Column(INT(), nullable=False, server_default="3")

    def __init__(self, **kwargs):
        self.email = kwargs.get("email")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.predictions = kwargs.get("predictions")
