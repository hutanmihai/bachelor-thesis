from sqlalchemy import Column, DateTime, func


class TimestampMixin:
    """Mixin with timestamp for models"""

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
