class BaseServiceError(Exception):
    """Base class for all exceptions raised by this module."""


class BaseUserServiceError(BaseServiceError):
    """Base class for all exceptions raise by User services"""


class UserAlreadyExists(BaseUserServiceError):
    """Raised when a user already exists."""


class UserNotFound(BaseUserServiceError):
    """Raised when a user doesn't exist."""
