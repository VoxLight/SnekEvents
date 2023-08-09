import pytest
from eventful_delegate.system import CustomEventSystem
from eventful_delegate.exceptions import EventNotFoundError, PayloadMismatchError

def test_register_event():
    system = CustomEventSystem()
    event_name = "testEvent"
    system.on(event_name, lambda x: x)
    
    assert hasattr(system, event_name)

def test_fire_event():
    system = CustomEventSystem()
    event_name = "testEvent2"
    system.on(event_name, lambda x: x)
    
    @system.do(event_name)
    def trigger_event(x):
        return x
    
    # This should not raise any errors
    trigger_event(5)

def test_fire_unregistered_event():
    system = CustomEventSystem()
    
    with pytest.raises(EventNotFoundError):
        @system.do("nonexistentEvent")
        def trigger_event(x):
            return x

        trigger_event(5)

def test_event_with_invalid_payload():
    system = CustomEventSystem()
    event_name = "testEvent3"
    system.on(event_name, lambda x, y: (isinstance(x, int), isinstance(y, int)))
    
    @system.do(event_name)
    def trigger_event(x, y):
        return x + y
    
    with pytest.raises(PayloadMismatchError):
        trigger_event('1', 2)
