import pytest
from snekevents import SnekEventSystem
from snekevents import SnekEventPayloadMismatchError

def test_example():
    ses = SnekEventSystem()

    # We register a listener for the on_message event.
    @ses.listen
    async def on_messge(message):
        print(message)

    # A seperate event listener for the same event.
    @ses.listen('on_message')
    async def my_message_listener(message)
        print("I also heard the message!")

    # To fire the event:
    message = {"content":"Words go here!", "id":1234}
    await ses.on_message(message)

    # But we can also do
    await ses.on_message.fire(message)


    # but also

    class MyEventSystem(SnekEventSystem):

        def __init__():
            super().__init__()

        async def on_message(message):
            print("I got a message!:", message)

        async def on_ready():
            print("I am ready!")


    MyEventSystem.on_message() # or whatever

