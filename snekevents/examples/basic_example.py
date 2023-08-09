from snekevents import SnekEventSystem

event_system = SnekEventSystem()

# Register an event listener.
@event_system.listen
def on_my_event():
    print(f"My event was fired!")

# Fire the event.
event_system.on_my_event(message_data)
