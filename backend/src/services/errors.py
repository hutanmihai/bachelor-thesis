class BaseServiceError(Exception):
    """Base class for all exceptions raised by this module."""


class BaseUserServiceError(BaseServiceError):
    """Base class for all exceptions raised by User services"""


class BaseEntryServiceError(BaseServiceError):
    """Base class for all exceptions raised by Entry services"""


class UserAlreadyExists(BaseUserServiceError):
    """Raised when a user already exists."""


class UserNotFound(BaseUserServiceError):
    """Raised when a user doesn't exist."""


class EntryNotFound(BaseEntryServiceError):
    """Raised when entry doesn't exist"""


class EntryNotCreatedByUser(BaseUserServiceError):
    """Raised when a user tries to mutate or fetch entry/entries that are not his"""
