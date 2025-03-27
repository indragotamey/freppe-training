class EventManager:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notify(self, event_data):
        for subscriber in self.subscribers:
            subscriber.update(event_data)


class EventListener:
    def __init__(self, name):
        self.name = name

    def update(self, event_data):
        print(f"{self.name} received event: {event_data}")


if __name__ == "__main__":
    event_manager = EventManager()

    listener1 = EventListener("Listener 1")
    listener2 = EventListener("Listener 2")

    event_manager.subscribe(listener1)
    event_manager.subscribe(listener2)

    event_manager.notify("New Event: Data Updated!")

    event_manager.unsubscribe(listener1)

    event_manager.notify("New Event: User Logged In!")