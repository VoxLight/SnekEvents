from snekevents import SnekEventSystem

event_system = SnekEventSystem()

# Inline decorator usage.

# Register an event listener for the on_alert event.
@event_system.listen
def on_alert(alert_message):
    print(alert_message)

# Another listener for the same event.
@event_system.listen('on_alert')
def another_alert_listener(alert_message):
    print(f"ALERT: {alert_message}")

# Fire the event.
event_system.on_alert("This is an inline decorator showcase!")
