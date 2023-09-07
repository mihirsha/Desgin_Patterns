

class Channel:

    def __init__(self):
        self.subscribers = []

    def register(self, sub):
        self.subscribers.append(sub)
    
    def unregister(self, sub):
        self.subscribers.remove(sub)
    
    def notify(self):
        for sub in self.subscribers:
            sub.update()

    def upload(self, title):
        self.title = title
        self.notify()
    