class EventEmitter:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name, callback):
        if event_name in self.listeners:
            self.listeners[event_name].remove(callback)

    def emit(self, event_name, data=None):
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(data)


def listener_a(data):
    print(f"A received: {data}")

def listener_b(data):
    print(f"B received: {data}")


if __name__ == "__main__":
    emitter = EventEmitter()
    emitter.subscribe("message", listener_a)
    emitter.subscribe("message", listener_b)

    emitter.emit("message", "Hello, world!")

    emitter.unsubscribe("message", listener_b)
    emitter.emit("message", "Second message")
