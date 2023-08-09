from snekevents import SnekEventSystem

class MyAlertSystem(SnekEventSystem):

    # Class-based decorator usage.

    # Register an event listener for the on_warning event.
    @SnekEventSystem.listen
    def on_warning(self, warning_message):
        print(warning_message)

    # Another listener for the same event.
    @SnekEventSystem.listen('on_warning')
    def another_warning_listener(self, warning_message):
        print(f"WARNING: {warning_message}")

alert_system = MyAlertSystem()
alert_system.on_warning("This is a class decorator showcase!")
