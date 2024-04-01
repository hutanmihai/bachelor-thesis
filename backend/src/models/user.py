import uuid

from sqlalchemy import VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID
from src.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(VARCHAR(255), nullable=False)
