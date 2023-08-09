"""
snek_event.py
-------------

Module containing the core event class for the `snekevents` library.
"""
import asyncio
from typing import Callable, List, Any, Union

from .snek_exceptions import SnekEventPayloadMismatchError

class SnekEvent:
    """
    This defines the behavior and attributes of a 
    single event and provides methods for event registration, firing, and interaction.
    """
    def __init__(self, signature: Callable[..., None] = None):
        """
        Initialize a new event.

        :param signature: Optional callable to validate event payload.
        """
        self._callbacks: List[Callable[..., Union[None, Any]]] = []
        self._signature: Callable[..., None] = signature or (lambda *args, **kwargs: None)
        self._tasks = []

    def register(self, callback: Callable[..., Union[None, Any]]) -> None:
        """
        Register a callback to be invoked when the event fires.

        :param callback: Callable to be added to the event's list of callbacks.
        """
        self._callbacks.append(callback)

    async def fire(self, *args, **kwargs) -> None:
        """
        Fire the event, invoking all registered callbacks.

        If a signature callable was provided during initialization, this method validates the event payload 
        against it. Coroutine callbacks are awaited asynchronously, while regular callables are invoked directly.

        :raises SnekEventPayloadMismatchError: If the provided payload doesn't match the expected signature.
        """
        # Check payload using signature function
        try:
            self._signature(*args, **kwargs)
        except Exception as error:
            # pylint: disable=raise-missing-from
            raise SnekEventPayloadMismatchError(str(error))

        await asyncio.gather(*self._callbacks)
        # Call non-coroutine callbacks


    def every(self, interval, times=1):
        """Method to periodically fire the event."""
        async def periodic_fire():
            runs = 0
            while runs <= times:
                await asyncio.sleep(interval)
                await self.fire()
                runs += 1
        self._tasks.append(asyncio.create_task(periodic_fire()))

    def cancel_periodic(self, event_name):
        """
        Cancels the periodic execution of an event.

        :param event_name: Name of the event to stop firing periodically.
        """
        task = self._scheduled_tasks.get(event_name)
        if task:
            task.cancel()
            self._scheduled_tasks.pop(event_name)

    async def __call__(self, *args, **kwargs) -> None:
        """
        Allow the event to be directly called, which in turn fires the event asynchronously.
        """
        await self.fire(*args, **kwargs)


import asyncio
from .snek_exceptions import SnekEventPayloadMismatchError

class SnekEvent:
    def __init__(self, signature=None):
        self._callbacks = []
        self._signature = signature or (lambda *args, **kwargs: None)
        self._tasks = []

    def register(self, callback):
        self._callbacks.append(callback)

    async def fire(self, *args, **kwargs):
        # Check payload using signature function
        try:
            self._signature(*args, **kwargs)
        except Exception as e:
            raise SnekEventPayloadMismatchError(str(e))

        coros = [callback(*args, **kwargs) for callback in self._callbacks if asyncio.iscoroutinefunction(callback)]
        await asyncio.gather(*coros)

        non_coros = [callback for callback in self._callbacks if not asyncio.iscoroutinefunction(callback)]
        for cb in non_coros:
            cb(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        asyncio.create_task(self.fire(*args, **kwargs))

    def every(self, interval):
        """Method to periodically fire the event."""
        async def periodic_fire():
            while True:
                await asyncio.sleep(interval)
                await self.fire()
        self._tasks.append(asyncio.create_task(periodic_fire()))

    def cancel_periodic(self):
        """Method to cancel all periodic tasks."""
        for task in self._tasks:
            task.cancel()
