class SnekEventError(Exception):
    """Base class for snek event system exceptions."""

class SnekEventNotFoundError(SnekEventError):
    """Raised when a snek event is not found."""
    def __init__(self, event_name):
        message = f"Event '{event_name}' not found."
        super().__init__(message)

class SnekEventPayloadMismatchError(SnekEventError):
    """Raised when the snek event payload doesn't match the expected signature."""
    def __init__(self, details=""):
        message = f"Payload mismatch. {details}"
        super().__init__(message)
