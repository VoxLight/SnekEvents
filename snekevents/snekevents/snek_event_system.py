# snek_event_system.py

import asyncio
from typing import Callable, Optional

from .snek_event import SnekEvent
from .snek_exceptions import SnekEventError, SnekEventNotFoundError

class SnekEventSystem:
    _declared_events = {}

    @classmethod
    def event(cls, signature=None):
        """
        Class decorator to declare an event.
        """
        def decorator(name):
            cls._declared_events[name] = signature or (lambda *args, **kwargs: None)
            return name
        return decorator

    def __init__(self):
        self._events = {}
        for event_name, signature in self._declared_events.items():
            self._events[event_name] = SnekEvent(signature)
            
            # Automatically register class methods as event listeners
            listener = getattr(self, event_name, None)
            if callable(listener):
                self._events[event_name].on(listener)

    def listen(self, event_name: Optional[str] = None) -> Callable[..., None]:
        """
        Decorator for registering a listener for an event.
        """
        def decorator(callback: Callable[..., None]) -> Callable[..., None]:
            name = event_name or callback.__name__

            if name not in self._events:
                self._events[name] = SnekEvent()

            self._events[name].on(callback)
            return callback
        return decorator   

    def __getattr__(self, event_name: str) -> SnekEvent:
        if event_name not in self._events:
            raise SnekEventNotFoundError(f"No event named '{event_name}' found.")
        return self._events[event_name]
