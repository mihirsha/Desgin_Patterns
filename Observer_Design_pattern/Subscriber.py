from channel import Channel as ch

class Subscribers:

    def __init__(self, name):
        self._name = name
        self._channel = ch()
    
    def update(self):
        print("Video uploaded {}".format(self._name))

    def subscribe(self, channel: ch):
        self._channel = channel