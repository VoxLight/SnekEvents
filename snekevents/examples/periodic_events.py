from snekevents import SnekEventSystem
import asyncio

event_system = SnekEventSystem()

@event_system.listen
def on_data(key):
    print(f"Processing data: {key}")

data_payload = {"key": "value"}
event_system.on_data.every(5, payload=data_payload)

async def main():
    await asyncio.sleep(20)  # Run for 20 seconds to see the periodic events.

asyncio.run(main())